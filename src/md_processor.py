from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type: TextType):
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
    
