import unittest

from gencontent import extract_title


class TestGenContentExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = """
# This is a title that ends with spaces 
"""
        self.assertEqual(extract_title(md), "This is a title that ends with spaces")

    def test_split_nodes_delimiter_with_invalid_markdown(self):
        with self.assertRaises(Exception):
            md = """
This is not a title that ends with spaces 
"""
            extract_title(md)


