class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag=tag # type of tag
        self.value=value # contents
        self.children=children # child node
        self.props=props # dict of key-val representing attribute of tag

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        string = ""
        for key, val in self.props.items():
            string += f'{key}=\"{val}\" '
        return string

    def __repr__(self):
        return f"tag:{self.tag}, \nvalue/contents={self.value}, \nsubnode/chil={self.children}, properties={self.props}"

    
