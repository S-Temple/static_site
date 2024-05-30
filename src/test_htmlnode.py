import unittest

from htmlnode import HTMLNode

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

