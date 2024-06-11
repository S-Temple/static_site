class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag=tag # type of tag
        self.value=value # contents
        self.children=children # child node
        self.props=props # dict of key-val representing attribute of tag

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        string = ""
        for key, val in self.props.items():
            string += f' {key}=\"{val}\"'
        return string

    def __repr__(self):
        return f"tag:{self.tag}, \nvalue/contents={self.value}, \nsubnode/child={self.children}, properties={self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
 
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no Tag")
        if self.children is None:
            raise ValueError("Parent Node must have child node")
        string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            string += child.to_html()
        string += f"</{self.tag}>"
        return string

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value},\n{self.children},\n {self.props})"
   

