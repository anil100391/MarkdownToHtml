from textnode import *
from htmlnode import *

def main():
    txt = TextNode("Hello World", TextType.BOLD)
    print(txt)
    print(LeafNode("p", "This is a paragraph of text.").tohtml())
    print(LeafNode("a", "Click me!", {"href": "https://www.google.com", "border": "blank" }).tohtml())
    print(ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
    ).tohtml())

main()
