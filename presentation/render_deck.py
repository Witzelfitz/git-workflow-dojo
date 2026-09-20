#!/usr/bin/env python3
"""Render PDF + overview and check the browser player. Requires Playwright + Pillow."""
import argparse
from pathlib import Path
import tempfile
from playwright.sync_api import sync_playwright
from PIL import Image

root=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--chrome',help='Optional path to an installed Chrome/Chromium executable')
args=parser.parse_args()
with tempfile.TemporaryDirectory(prefix='dojo-slide-previews-') as folder:
    previews=Path(folder)
    with sync_playwright() as p:
        browser=p.chromium.launch(**({'executable_path':args.chrome} if args.chrome else {}),headless=True)
        page=browser.new_page(viewport={'width':1600,'height':900},device_scale_factor=1)
        errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.goto((root/'print.html').as_uri())
        issues=page.evaluate('''() => [...document.querySelectorAll('.slide')].flatMap((s,i)=>[...s.querySelectorAll('text')].flatMap(t=>{let b=t.getBBox(),m=Number(t.dataset.maxWidth);return b.width>m+2||b.x<0||b.x+b.width>1600||b.y<0||b.y+b.height>900?[{slide:i+1,text:t.textContent}]:[]}))''')
        assert not issues,issues
        assert page.locator('.slide').count()==25
        for i,slide in enumerate(page.locator('.slide').all(),1):slide.screenshot(path=str(previews/f'{i:02}.png'))
        page.pdf(path=str(root/'git-dojo.pdf'),prefer_css_page_size=True,print_background=True)
        page.goto((root/'git-dojo.html').as_uri())
        assert page.locator('.slide.active').get_attribute('id')=='slide-1'
        page.keyboard.press('ArrowRight');assert page.locator('.slide.active').get_attribute('id')=='slide-2'
        page.keyboard.press('End');assert page.locator('.slide.active').get_attribute('id')=='slide-25'
        page.keyboard.press('n');assert page.locator('#notes').is_visible()
        page.keyboard.press('n');assert not page.locator('#notes').is_visible()
        page.select_option('#jump','17');page.click('#timerToggle')
        page.wait_for_timeout(1400)
        seconds=page.evaluate('remaining')
        assert 1197<=seconds<=1199,seconds
        page.keyboard.press('ArrowRight');assert page.locator('#timerToggle').inner_text()=='Pause'
        page.click('#timerReset');assert page.locator('#timer output').inner_text()=='20:00'
        for width,height in [(1600,900),(960,540)]:
            page.set_viewport_size({'width':width,'height':height})
            box=page.locator('.slide.active').bounding_box();nav=page.locator('nav').bounding_box()
            assert box['y']>=-1 and box['y']+box['height']<nav['y'],(box,nav)
            assert nav['x']>=0 and nav['x']+nav['width']<=width,(width,nav)
        assert not errors,errors
        browser.close()
    overview=Image.new('RGB',(2000,1125),(245,243,234))
    for i in range(25):
        im=Image.open(previews/f'{i+1:02}.png').convert('RGB').resize((400,225))
        overview.paste(im,((i%5)*400,(i//5)*225))
    overview.save(root/'overview.jpg',quality=92)
print('25 slides rendered; geometry, navigation, notes, timer and toolbar checks passed.')
