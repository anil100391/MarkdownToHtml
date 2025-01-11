import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):

    def test_eq(self):
        n0 = HTMLNode(tag = "a", value = "HTML is great", props = {"href": "https://www.google.com"})
        n1 = HTMLNode(tag = "a", value = "HTML is great", props = {"href": "https://www.google.com"})
        self.assertEqual(n0, n1)
        l0 = LeafNode(tag = "a", value = "I am a leaf node", props = {"href": "https://www.google.com"})
        self.assertEqual(l0.tohtml(), '<a href="https://www.google.com">I am a leaf node</a>')
        p0 = ParentNode(tag = "p", children = [l0], props = {"color": "red"})
        self.assertEqual(p0.tohtml(), '<p color="red"><a href="https://www.google.com">I am a leaf node</a></p>')
