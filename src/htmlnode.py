from textnode import TextNode

class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def tohtml(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join([f' {k}="{v}"' for k, v in self.props.items()])

    def __repr__(self):
        print(f'tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}')

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def tohtml(self):
        if not self.value:
            raise ValueError

        if not self.tag:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def tohtml(self):
        if not self.tag:
            raise ValueError

        if not self.children:
            raise ValueError('Children cannot be empty')

        children = "".join([child.tohtml() for child in self.children])
        return f'<{self.tag}{self.props_to_html()}>{children}</{self.tag}>'

def text_node_to_html(text_node):

    if text_node.text_type == 'normal':
        return LeafNode(None, text_node.text)

    if text_node.text_type == 'bold':
        return LeafNode('b', text_node.text)

    if text_node.text_type == 'italic':
        return LeafNode('i', text_node.text)

    if text_node.text_type == 'code':
        return LeafNode('code', text_node.text)

    if text_node.text_type == 'link':
        return LeafNode('a', text_node.text, {'href': text_node.url})

    if text_node.text_type == 'image':
        return LeafNode('img', None, {'src': text_node.url})


