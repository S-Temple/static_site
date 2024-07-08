#TODO 
"""
Markdown parsers often support the nesting of inline elements. For example, you can have a bold word inside of italics:

This is an *italic and **bold** word*.

For simplicity's sake, we won't allow it! We will only support a single level of nesting when it comes to inline elements. If you want to extend the project to support multiple levels of nesting, you're welcome to do so! We just won't be covering it explicitly.
"""

from blocks import * 
md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
blocks = markdown_to_blocks(md)
print(blocks)
print("\n-----\n")
print([
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
])

