import unittest

from block_markdown import BlockType, block_to_blocktype, is_code_block, is_heading, is_ordered_list, is_quote_block, is_unordered_list, markdown_to_blocks
 
class TestBlockMarkdownMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockMarkdownBlockToBlocktype(unittest.TestCase):
    def test_block_to_blocktype_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_blocktype(block),BlockType.HEADING)

    def test_block_to_blocktype_code_block(self):
        block = "```\nThis is a code block\n```"
        self.assertEqual(block_to_blocktype(block),BlockType.CODE)

    def test_block_to_blocktype_quote_block(self):
        block = "> This is a multi line quote block\n> Because here is the second line"
        self.assertEqual(block_to_blocktype(block),BlockType.QUOTE)

    def test_block_to_blocktype_unordered_list_block(self):
        block = "- This is a multi line unordered list block\n- Because here is the second line"
        self.assertEqual(block_to_blocktype(block),BlockType.UNORDERED_LIST)

    def test_block_to_blocktype_ordered_list_block(self):
        block = "1. This is a multi line ordered list block\n2. Because here is the second line"
        self.assertEqual(block_to_blocktype(block),BlockType.ORDERED_LIST)

    def test_block_to_blocktype_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(block_to_blocktype(block),BlockType.PARAGRAPH)


class TestBlockMarkdownIsHeading(unittest.TestCase):
    def test_is_heading_with_lv1_heading(self):
        block = "# This is a lv1 heading"
        self.assertTrue(is_heading(block))

    def test_is_heading_with_lv6_heading(self):
        block = "###### This is a lv6 heading"
        self.assertTrue(is_heading(block))

    def test_is_heading_with_bad_lv7_heading(self):
        block = "####### This is not a lv7 heading"
        self.assertFalse(is_heading(block))

    def test_is_heading_with_non_heading(self):
        block = "This is not a heading"
        self.assertFalse(is_heading(block))


class TestBlockMarkdownIsCodeBlock(unittest.TestCase):
    def test_is_code_block_with_code_block(self):
        block = "```\nprint('Hello world)\n```"
        self.assertTrue(is_code_block(block))

    def test_is_code_block_with_non_code_block(self):
        block = "This is not a code block"
        self.assertFalse(is_code_block(block))


class TestBlockMarkdownIsQuoteBlock(unittest.TestCase):
    def test_is_quote_block_with_single_line_quote_block(self):
        block = "> This is a single line quote block"
        self.assertTrue(is_quote_block(block))

    def test_is_quote_block_with_multi_line_quote_block(self):
        block = "> This is a multi line quote block\n> Because here is the second line"
        self.assertTrue(is_quote_block(block))

    def test_is_quote_block_with_non_quote_block(self):
        block = "This is not a quote block"
        self.assertFalse(is_quote_block(block))

    def test_is_quote_block_with_non_quote_block_with_special_character(self):
        block = "This is not a quote block but does have the > character"
        self.assertFalse(is_quote_block(block))

    def test_is_quote_block_with_non_quote_block_with_quote_as_part(self):
        block = ">This is not a quote block\nEven though the first line looked like it was"
        self.assertFalse(is_quote_block(block))


class TestBlockMarkdownIsUnorderedListBlock(unittest.TestCase):
    def test_is_unordered_list_with_single_line_unordered_list(self):
        block = "- This is a single line unordered_list block"
        self.assertTrue(is_unordered_list(block))

    def test_is_unordered_list_with_multi_line_unordered_list(self):
        block = "- This is a multi line unordered_list block\n- Because here is the second line"
        self.assertTrue(is_unordered_list(block))

    def test_is_unordered_list_with_non_unordered_list(self):
        block = "This is not a unordered_list block"
        self.assertFalse(is_unordered_list(block))

    def test_is_unordered_list_with_non_unordered_list_with_special_character(self):
        block = "This is not a unordered_list block but does have the - character"
        self.assertFalse(is_unordered_list(block))

    def test_is_unordered_list_with_non_unordered_list_with_unordered_list_as_part(self):
        block = "-This is not a unordered_list block\nEven though the first line looked like it was"
        self.assertFalse(is_unordered_list(block))


class TestBlockMarkdownIsOrderedListBlock(unittest.TestCase):
    def test_is_ordered_list_with_single_line_ordered_list(self):
        block = "1. This is a single line ordered_list block"
        self.assertTrue(is_ordered_list(block))

    def test_is_ordered_list_with_multi_line_ordered_list(self):
        block = "1. This is a multi line ordered_list block\n2. Because here is the second line"
        self.assertTrue(is_ordered_list(block))

    def test_is_ordered_list_with_non_ordered_list(self):
        block = "This is not a ordered_list block"
        self.assertFalse(is_ordered_list(block))

    def test_is_ordered_list_with_non_ordered_list_with_special_character(self):
        block = "This is not a ordered_list block but does have this number 1. that would otherwise indicate an ordered list"
        self.assertFalse(is_ordered_list(block))

    def test_is_ordered_list_with_non_ordered_list_with_ordered_list_as_part(self):
        block = "-This is not a ordered_list block\nEven though the first line looked like it was"
        self.assertFalse(is_ordered_list(block))

    def test_is_ordered_list_with_multi_line_non_ordered_list(self):
        block = "1. This looks like it is a multi line ordered_list block\n3. But it is not because this line starts with a 3 instead of a 2"
        self.assertFalse(is_ordered_list(block))
