import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        splits = node.text.split(delimiter)

        # Should always have an odd number of elements after splitting
        if len(splits) % 2 != 1:
            raise Exception(f"invalid markdown sytax: {node.text}")

        for i in range(0,len(splits)):
            # Ignore empty strings
            if splits[i] == "":
                continue

            # Default to normal text type
            current_text_type = TextType.TEXT

            # All odd elements should be new text_type
            if i % 2 == 1:
                current_text_type = text_type

            new_nodes.append(TextNode(splits[i], current_text_type))

    return new_nodes

    
def extract_markdown_images(text):
    image_regex_match = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex_match, text)
    return matches


def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_text = node.text
        img_tuple_list = extract_markdown_images(current_text)

        for img_tuple in img_tuple_list:
            alt_text = img_tuple[0]
            img_url = img_tuple[1]
            splits = current_text.split(f"![{alt_text}]({img_url})")

            if len(splits) != 2:
                raise Exception(f"Failed to parse image in markdown from text: {current_text}")

            new_nodes.append(TextNode(splits[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_url))
            current_text = splits[1]

        if current_text == "":
            continue

        new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes

def extract_markdown_links(text):
    link_regex_match = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_regex_match, text)
    return matches

