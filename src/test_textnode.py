import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("Hello World!", TextType.BOLD)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node2, node3)

if __name__ == "__main__":
    unittest.main()