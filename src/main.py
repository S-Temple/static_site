#TODO 
"""
Markdown parsers often support the nesting of inline elements. For example, you can have a bold word inside of italics:

This is an *italic and **bold** word*.

For simplicity's sake, we won't allow it! We will only support a single level of nesting when it comes to inline elements. If you want to extend the project to support multiple levels of nesting, you're welcome to do so! We just won't be covering it explicitly.
"""

from textnode import * 
node = TextNode(
    "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
    text_type_text, )
new_nodes = split_nodes_link([node])
print([
    TextNode("This is text with a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),
    TextNode(" and ", text_type_text),
    TextNode("another link", text_type_link, "https://blog.boot.dev"),
    TextNode(" with text that follows", text_type_text),
])
print(new_nodes)
