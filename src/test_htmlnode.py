import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_initialization(self):
        node = HTMLNode(tag='div', value='Hello', children=None, props={'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {'class': 'container'})

    def test_props_to_html(self):
        node = HTMLNode(tag='div', value='Hello', children=None, props={'class': 'container', 'id': 'main'})
        props_html = node.props_to_html()
        self.assertIn('class="container"', props_html)
        self.assertIn('id="main"', props_html)

    def test_repr(self):
        node = HTMLNode(tag='div', value='Hello', children=None, props={'class': 'container'})
        repr_str = repr(node)
        self.assertIn('tag:div', repr_str)
        self.assertIn('value/contents=Hello', repr_str)
        self.assertIn("properties={'class': 'container'}", repr_str)

    # leafnode tests

    def test_initialization(self):
        node = LeafNode('div', 'Hello', {'class': 'container'})
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {'class': 'container'})

    def test_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(),"<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(),"<a href=\"https://www.google.com\">Click me!</a>")

    # parent node tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
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

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()
