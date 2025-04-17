from enum import Enum
from re import findall


class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for block in blocks:
        block = block.strip()

        if block == "":
            continue

        new_blocks.append(block)
    return new_blocks

def block_to_blocktype(block: str) -> BlockType:
    if is_heading(block):
        return BlockType.HEADING
    if is_code_block(block):
        return BlockType.CODE
    if is_quote_block(block):
        return BlockType.QUOTE
    if is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_heading(block: str) -> bool:
    heading_reg_filter = r"^(#{1,6} )"
    matches = findall(heading_reg_filter, block)
    return len(matches) == 1

def is_code_block(block: str) -> bool:
    code_block_reg_filter = r"^```[\s\S]*```$"
    matches = findall(code_block_reg_filter, block)
    return len(matches) == 1

def is_quote_block(block: str) -> bool:
    return check_all_lines(r"^>", block)

def is_unordered_list(block: str) -> bool:
    return check_all_lines(r"^- ", block)

def is_ordered_list(block: str) -> bool:
    ordered_list_reg_filter = r"^(\d+)\. "
    lines = block.split('\n')
    line_num = 1
    for line in lines:
        matches = findall(ordered_list_reg_filter, line.strip())
        if len(matches) != 1 or int(matches[0]) != line_num:
            return False
        line_num += 1
    return True

def check_all_lines(filter, block):
    lines = block.split('\n')
    for line in lines:
        matches = findall(filter, line.strip())
        if len(matches) != 1:
            return False
    return True

