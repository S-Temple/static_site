import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2, f"test_eq failed : {node} should equal {node2}")

    def test_eq_none(self):
        node = TextNode("Testing", "itallic", None)
        node2 = TextNode("test", "ital", None)
        self.assertNotEqual(node,node2)

    def test_print(self):
        node = TextNode("Testing", "itallic", "http://test.ca")
        self.assertEqual(str(node), "TextNode(Testing, itallic, http://test.ca)")

if __name__ == "__main__":
    unittest.main()

