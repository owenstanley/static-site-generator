import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_single_child(self):
        node = ParentNode("div", [LeafNode("i", "italic text")])
        self.assertEqual(node.to_html(), "<div><i>italic text</i></div>")

    def test_multiple_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_multiple_parents(self):
        grandchild = LeafNode("i", "grandchild")
        child = ParentNode("p", [grandchild])
        parent = ParentNode("div", [child])

        self.assertEqual(parent.to_html(), "<div><p><i>grandchild</i></p></div>")
