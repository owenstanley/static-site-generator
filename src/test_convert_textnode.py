import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestConvertTextNode(unittest.TestCase):
    def test_converttext(self):
        text_node = TextNode("This is a bold text node", TextType.BOLD)
        leaf_node = text_node_to_html_node(text_node)
        self.assertEqual(leaf_node.to_html(), "<b>This is a bold text node</b>")

    def test_convert_isequal(self):
        text_node1 = TextNode("This is a code text node", TextType.CODE)
        text_node2 = TextNode("This is a code text node", TextType.CODE)
        leaf_node1 = text_node_to_html_node(text_node1)
        leaf_node2 = text_node_to_html_node(text_node2)
        self.assertEqual(leaf_node1.to_html(), leaf_node2.to_html())

    def test_convert_isnotequal(self):
        text_node1 = TextNode("This is an italic text node", TextType.ITALIC)
        text_node2 = TextNode("This is a bold text node", TextType.BOLD)
        leaf_node1 = text_node_to_html_node(text_node1)
        leaf_node2 = text_node_to_html_node(text_node2)
        self.assertNotEqual(leaf_node1.to_html(), leaf_node2.to_html())

    def test_convertnone(self):
        text_node = TextNode("This is a text node", None)
        with self.assertRaises(Exception, msg="Error: invalid type"):
            leaf_node = text_node_to_html_node(text_node)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")