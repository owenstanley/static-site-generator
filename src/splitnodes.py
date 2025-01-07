from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_nodes = []
        split = node.text.split(delimiter)

        if len(split) % 2 == 0:
            raise ValueError("Invalid markdown syntax, no closing tag")

        for i in range(0, len(split)):
            if split[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(split[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(split[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes