import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('p', 'some text', None, {"href": "https://www.google.com", "target": "_blank"})
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_values(self):
        node = HTMLNode('p', 'some text', None, None)
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'some text')

    def test_repr_for_no_args(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(node.__repr__(), expected_repr)

    def test_repr_for_args(self):
        node = HTMLNode('p', 'some text')
        expected_repr = "HTMLNode(tag=p, value=some text, children=None, props=None)"
        self.assertEqual(node.__repr__(), expected_repr)

    def test_repr_for_props(self):
        node = HTMLNode('p', 'some text', None, {"class": "primary"})
        expected_repr = "HTMLNode(tag=p, value=some text, children=None, props={'class': 'primary'})"
        self.assertEqual(node.__repr__(), expected_repr)


class TestLeafNode(unittest.TestCase):
    def test_props_to_html(self):
        node = LeafNode('a', 'some text', {"href": "https://www.google.com", "target": "_blank"})
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_values(self):
        node = LeafNode('p', 'some text', None)
        self.assertEqual(node.tag, 'p')
        self.assertEqual(node.value, 'some text')

    def test_repr(self):
        node = LeafNode('p', 'some text')
        expected_repr = "LeafNode(tag=p, value=some text, props=None)"
        self.assertEqual(node.__repr__(), expected_repr)

    def test_repr_for_props(self):
        node = LeafNode('p', 'some text', {"class": "primary"})
        expected_repr = "LeafNode(tag=p, value=some text, props={'class': 'primary'})"
        self.assertEqual(node.__repr__(), expected_repr)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Hello, world!")
        self.assertEqual(node.to_html(), "<i>Hello, world!</i>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()
