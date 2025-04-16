import unittest

from md_processor import extract_markdown_images, extract_markdown_links, split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
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
        
    def test_split_images_with_no_images(self):
        node = TextNode(
            "This text has no images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_new_nodes = [
            TextNode("This text has no images", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_images_with_image_at_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) there is an image at the start of this node",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        expected_new_nodes = [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" there is an image at the start of this node", TextType.TEXT)
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_images_with_image_at_end(self):
        node = TextNode(
            "there is an image at the end of this node ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        expected_new_nodes = [
            TextNode("there is an image at the end of this node ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_images_with_just_two_images(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        expected_new_nodes = [
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)


class TestMdProcessorSplitLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_new_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_links_with_no_links(self):
        node = TextNode(
            "This text has no links",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_new_nodes = [
            TextNode("This text has no links", TextType.TEXT),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_links_with_link_at_start(self):
        node = TextNode(
            "[link](https://www.boot.dev) there is an link at the start of this node",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        expected_new_nodes = [
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode(" there is an link at the start of this node", TextType.TEXT)
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_links_with_link_at_end(self):
        node = TextNode(
            "there is an link at the end of this node [link](https://www.boot.dev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        expected_new_nodes = [
            TextNode("there is an link at the end of this node ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

    def test_split_links_with_just_two_links(self):
        node = TextNode(
            "[link](https://www.boot.dev)[second link](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        expected_new_nodes = [
            TextNode("link", TextType.LINK, "https://www.boot.dev"),
            TextNode("second link", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertListEqual(new_nodes, expected_new_nodes)

class TestMdProcessorTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        textnodes = text_to_textnodes(text)
        expected_textnodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(textnodes, expected_textnodes)

    def test_text_to_textnodes_empty_text(self):
        text = ""
        textnodes = text_to_textnodes(text)
        expected_textnodes = []
        self.assertListEqual(textnodes, expected_textnodes)

