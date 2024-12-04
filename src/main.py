from textnode import TextNode, TextType
from leafnode import LeafNode

def main():
    t1 = TextNode("this is a bold node", TextType.BOLD, "https://www.boot.dev")
    l1 = LeafNode("p", "This is a paragraph of text.")
    l2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(l1.to_html())
    print(l2.to_html())

if __name__ == "__main__":
    main()