import os
import unittest
from tempfile import TemporaryDirectory
from unittest.mock import patch

from infragit.__main__ import main


class TestInit(unittest.TestCase):
    def test_create_igit_self_folder(self):
        with TemporaryDirectory() as temp_dir:
            # temp_dir = "tests\example-infra"
            with patch("sys.argv", ["file.py", "init", "--directory", temp_dir]):
                ret_code = main()

                # No terraform configuration files in the dir, do not initialize
                self.assertFalse(os.path.isdir(os.path.join(temp_dir, ".igit")))
                self.assertEqual(ret_code, 1)

                with open(os.path.join(temp_dir, "main.tf"), "w") as fo:
                    fo.write(
                        """
                    resource "null_resource" "cluster" {}
                    """
                    )

                self.assertTrue(os.path.isfile(os.path.join(temp_dir, "main.tf")))
                ret_code = main()

                self.assertTrue(os.path.isdir(os.path.join(temp_dir, ".igit")))
                self.assertTrue(os.path.isfile(os.path.join(temp_dir, ".terraform.lock.hcl")))
                self.assertEqual(ret_code, 0)
