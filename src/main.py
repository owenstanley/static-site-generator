from textnode import TextNode, TextType

def main():
    t1 = TextNode("this is a bold node", TextType.BOLD, "https://www.boot.dev")
    print(t1)


if __name__ == "__main__":
    main()
