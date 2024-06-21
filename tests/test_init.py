import os
from tempfile import TemporaryDirectory
import unittest

from unittest.mock import patch

from infragit.__main__ import main


class TestInit(unittest.TestCase):
    def test_create_igit_self_folder(self):
        with TemporaryDirectory() as temp_dir:
            with patch("sys.argv", ["file.py", "init", "--directory", temp_dir]):
                main()

                self.assertTrue(os.path.isdir(os.path.join(temp_dir, ".igit")))
            