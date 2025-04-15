import unittest

from md_processor import split_nodes_delimiter
from textnode import TextNode, TextType


class TestMdProcessor(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with **bold text** in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in it", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with _italic text_ in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in it", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_new_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_bold_and_italic(self):
        node = TextNode("This is text with **bold text** and _italic text_ in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in it", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_at_start(self):
        node = TextNode("**bold text** started this is text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("bold text", TextType.BOLD),
            TextNode(" started this is text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_at_end(self):
        node = TextNode("This is text with **bold text**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_multi(self):
        node = TextNode("This is text with **bold text** in it, and **more bold text** in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in it, and ", TextType.TEXT),
            TextNode("more bold text", TextType.BOLD),
            TextNode(" in it", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_with_invalid_markdown(self):
        with self.assertRaises(Exception):
            node = TextNode("This is text with **invalid markdown_ in it", TextType.TEXT)
            split_nodes_delimiter([node], "**", TextType.BOLD)
