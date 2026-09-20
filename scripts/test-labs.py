#!/usr/bin/env python3
"""End-to-end checks for the classroom scenarios; Python 3, Git and Bash only."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().with_name("create-labs.sh")


class LabTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dojo-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.labs = self.root / "labs with spaces"
        self.run_command("bash", str(SCRIPT), str(self.labs))

    def run_command(self, *args, cwd=None, expected=0, env=None):
        result = subprocess.run(
            args, cwd=cwd, text=True, capture_output=True, env=env
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result.stdout.strip()

    def git(self, lab, *args, expected=0, env=None):
        return self.run_command(
            "git", *args, cwd=self.labs / lab, expected=expected, env=env
        )

    def test_all_labs_are_clean_and_have_no_remote(self):
        for lab in ("conflict", "fast-forward", "rebase", "squash"):
            with self.subTest(lab=lab):
                self.assertEqual(self.git(lab, "status", "--porcelain"), "")
                self.assertEqual(self.git(lab, "remote"), "")
                self.git(lab, "fsck", "--no-dangling")

    def test_conflict_resolution_preserves_both_histories(self):
        self.git("conflict", "merge", "main", expected=1)
        self.assertEqual(
            self.git("conflict", "diff", "--name-only", "--diff-filter=U"),
            "program.md",
        )
        file = self.labs / "conflict" / "program.md"
        self.assertIn("<<<<<<< HEAD", file.read_text())
        file.write_text("- 12:30 Lunch in der Mensa mit vegetarischem Buffet\n")
        self.git("conflict", "diff", "--check")
        self.git("conflict", "add", "program.md")
        self.git("conflict", "commit", "-m", "merge: combine lunch requirements")
        self.assertEqual(len(self.git("conflict", "show", "-s", "--format=%P").split()), 2)
        self.git("conflict", "merge-base", "--is-ancestor", "main", "HEAD")
        self.git("conflict", "merge-base", "--is-ancestor", "team-a", "HEAD")
        self.assertEqual(self.git("conflict", "status", "--porcelain"), "")

    def test_merge_abort_restores_start(self):
        before = self.git("conflict", "rev-parse", "HEAD")
        content = (self.labs / "conflict" / "program.md").read_text()
        self.git("conflict", "merge", "main", expected=1)
        self.git("conflict", "merge", "--abort")
        self.assertEqual(self.git("conflict", "rev-parse", "HEAD"), before)
        self.assertEqual((self.labs / "conflict" / "program.md").read_text(), content)
        self.assertEqual(self.git("conflict", "status", "--porcelain"), "")

    def test_fast_forward_creates_no_commit(self):
        target = self.git("fast-forward", "rev-parse", "feature/info")
        count = self.git("fast-forward", "rev-list", "--all", "--count")
        self.git("fast-forward", "merge", "--ff-only", "feature/info")
        self.assertEqual(self.git("fast-forward", "rev-parse", "main"), target)
        self.assertEqual(self.git("fast-forward", "rev-list", "--all", "--count"), count)

    def test_divergence_then_rebase_enables_fast_forward(self):
        old_feature = self.git("rebase", "rev-parse", "feature/volunteers")
        old_main = self.git("rebase", "rev-parse", "main")
        self.git("rebase", "switch", "main")
        self.git("rebase", "merge", "--ff-only", "feature/volunteers", expected=128)
        self.assertEqual(self.git("rebase", "rev-parse", "main"), old_main)
        self.git("rebase", "switch", "feature/volunteers")
        self.git("rebase", "rebase", "main")
        new_feature = self.git("rebase", "rev-parse", "HEAD")
        self.assertNotEqual(old_feature, new_feature)
        self.assertEqual(self.git("rebase", "rev-parse", "HEAD^"), old_main)
        self.assertEqual(self.git("rebase", "diff", "before-rebase", "HEAD", "--", "volunteers.md"), "")
        self.assertTrue((self.labs / "rebase" / "weather.md").exists())
        self.git("rebase", "switch", "main")
        self.git("rebase", "merge", "--ff-only", "feature/volunteers")
        self.assertEqual(self.git("rebase", "rev-parse", "main"), new_feature)
        self.assertEqual(self.git("rebase", "status", "--porcelain"), "")

    def test_interactive_squash_preserves_content(self):
        before_tree = self.git("squash", "rev-parse", "HEAD^{tree}")
        self.assertEqual(self.git("squash", "rev-list", "--count", "main..HEAD"), "3")
        # Emulate the student's two todo edits; Git still performs the real rebase.
        editor = self.root / "sequence-editor.sh"
        editor.write_text(
            '#!/usr/bin/env bash\n'
            'awk \'BEGIN { n=0 } /^pick / { n++; if (n>1) sub(/^pick /,"squash ") } { print }\' '
            '"$1" > "$1.edited"\n'
            'mv "$1.edited" "$1"\n'
        )
        env = dict(os.environ, GIT_SEQUENCE_EDITOR=f'bash "{editor}"', GIT_EDITOR="true")
        self.git("squash", "rebase", "-i", "main", env=env)
        self.assertEqual(self.git("squash", "rev-list", "--count", "main..HEAD"), "1")
        self.assertEqual(self.git("squash", "rev-parse", "HEAD^{tree}"), before_tree)
        self.assertEqual(self.git("squash", "status", "--porcelain"), "")

    def test_existing_directory_is_never_overwritten(self):
        sentinel = self.labs / "keep.txt"
        sentinel.write_text("keep this content\n")
        before = self.git("conflict", "rev-parse", "HEAD")
        self.run_command("bash", str(SCRIPT), str(self.labs), expected=1)
        self.assertEqual(sentinel.read_text(), "keep this content\n")
        self.assertEqual(self.git("conflict", "rev-parse", "HEAD"), before)

    def test_default_invocation_creates_fresh_labs_each_time(self):
        env = dict(os.environ, TMPDIR=str(self.root))
        for _ in range(2):
            self.run_command("bash", str(SCRIPT), env=env)
        generated = list(self.root.glob("git-workflow-dojo.*"))
        self.assertEqual(len(generated), 2)
        for directory in generated:
            self.assertTrue((directory / "conflict" / ".git").is_dir())


if __name__ == "__main__":
    unittest.main(verbosity=2)
