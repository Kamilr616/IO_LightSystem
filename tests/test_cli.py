import argparse
import contextlib
import io
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

import main


class CommandLineTests(unittest.TestCase):
    def test_version_matches_release(self):
        output = io.StringIO()
        parser = main.create_argument_parser()
        parser.prog = 'main.py'

        with contextlib.redirect_stdout(output):
            with self.assertRaises(SystemExit) as exit_context:
                parser.parse_args(['--version'])

        self.assertEqual(exit_context.exception.code, 0)
        self.assertEqual(output.getvalue().strip(), 'main.py 1.1.0')

    def test_defaults_reference_the_bundled_model(self):
        args = main.create_argument_parser().parse_args([])

        self.assertTrue(Path(args.model).is_file())
        self.assertIsInstance(args.cameraId, int)
        self.assertIsInstance(args.minTrackingConfidence, float)

    def test_overrides_are_typed(self):
        args = main.create_argument_parser().parse_args([
            '--numHands', '1',
            '--frameWidth', '800',
            '--minTrackingConfidence', '0.75',
            '--mirrorImage', '1',
            '--barVisibility', '0',
            '--outputMode', '0',
        ])

        self.assertEqual(args.numHands, 1)
        self.assertEqual(args.frameWidth, 800)
        self.assertEqual(args.minTrackingConfidence, 0.75)
        self.assertEqual(args.mirrorImage, 1)
        self.assertEqual(args.barVisibility, 0)

    def test_confidence_rejects_values_outside_unit_interval(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            main.unit_interval('1.1')


if __name__ == '__main__':
    unittest.main()
