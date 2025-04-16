import unittest

from md_processor import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image
from textnode import TextNode, TextType


class TestMdProcessorSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with **bold text** in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
            TextNode(" in it", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with _italic text_ in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italic text", TextType.ITALIC),
            TextNode(" in it", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_new_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

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
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_at_start(self):
        node = TextNode("**bold text** started this is text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("bold text", TextType.BOLD),
            TextNode(" started this is text", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_at_end(self):
        node = TextNode("This is text with **bold text**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_new_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold text", TextType.BOLD),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

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
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_nodes_delimiter_with_invalid_markdown(self):
        with self.assertRaises(Exception):
            node = TextNode("This is text with **invalid markdown_ in it", TextType.TEXT)
            split_nodes_delimiter([node], "**", TextType.BOLD)


class TestMdProcessorExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        img_tuple_list = extract_markdown_images(text)
        expected_img_tuple_list = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertListEqual(img_tuple_list, expected_img_tuple_list)


class TestMdProcessorExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        link_tuple_list = extract_markdown_links(text)
        expected_link_tuple_list = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertListEqual(link_tuple_list, expected_link_tuple_list)


class TestMdProcessorSplitImages(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_new_nodes = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)
