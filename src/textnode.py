from enum import Enum

class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, obj1):
        return obj1.text == self.text and obj1.text_type == self.text_type and obj1.url == self.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}"
