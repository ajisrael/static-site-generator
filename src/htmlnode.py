
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_props = ""
        
        if self.props == None:
            return html_props

        for prop in self.props:
            html_props += f" {prop}=\"{self.props[prop]}\""
        return html_props

    def __repr__(self) -> str:
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError('All leaf nodes must have a value')

        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError('All parent nodes must have a tag')

        if self.children == None:
            raise ValueError('All parent nodes must have children')

        html_str = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            html_str += child.to_html()

        html_str += f"</{self.tag}>"

        return html_str

    def __repr__(self) -> str:
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
