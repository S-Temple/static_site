
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if type(other) != TextNode:
            return False
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode('b', text_node.text)
        case "italic":
            return LeafNode('i', text_node.text)
        case "code":
            return LeafNode('code', text_node.text, text_node.url)
        case "link":
            return LeafNode('a', text_node.text, {'href':text_node.url})
        case "image":
            return LeafNode('img', "", {'src':text_node.url,'alt':text_node.text})
        case _:
            raise Exception("Unknown text type")



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts)%2!=1:
            raise Exception("Invalid Markdown syntax")
        for i in range(len(parts)):
            if parts[i]=='':
                continue
            if i % 2 ==0:
                new_nodes.append(TextNode(parts[i], text_type_text))
            else:
                new_nodes.append(TextNode(parts[i], text_type))
    print("\n\n\n") 
    print(new_nodes)
    print("\n\n\n")
    return new_nodes

