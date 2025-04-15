import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode('p', 'some text', None, {"href": "https://www.google.com", "target": "_blank"})
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(html_node.props_to_html(), expected_props)

    def test_values(self):
        html_node = HTMLNode('p', 'some text', None, None)
        self.assertEqual(html_node.tag, 'p')
        self.assertEqual(html_node.value, 'some text')

    def test_repr_for_no_args(self):
        html_node = HTMLNode()
        expected_repr = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(html_node.__repr__(), expected_repr)

    def test_repr_for_args(self):
        html_node = HTMLNode('p', 'some text')
        expected_repr = "HTMLNode(tag=p, value=some text, children=None, props=None)"
        self.assertEqual(html_node.__repr__(), expected_repr)

    def test_repr_for_props(self):
        html_node = HTMLNode('p', 'some text', None, {"class": "primary"})
        expected_repr = "HTMLNode(tag=p, value=some text, children=None, props={'class': 'primary'})"
        self.assertEqual(html_node.__repr__(), expected_repr)

if __name__ == "__main__":
    unittest.main()
