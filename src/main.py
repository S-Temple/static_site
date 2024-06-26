#TODO 
"""
Markdown parsers often support the nesting of inline elements. For example, you can have a bold word inside of italics:

This is an *italic and **bold** word*.

For simplicity's sake, we won't allow it! We will only support a single level of nesting when it comes to inline elements. If you want to extend the project to support multiple levels of nesting, you're welcome to do so! We just won't be covering it explicitly.
"""

from textnode import TextNode

test = TextNode("This is a node", "bol", "url")
test2 = 3 

print(test == test2)

print(test)
