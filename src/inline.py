import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)



def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


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
    return new_nodes

    

def split_nodes_image(old_nodes):
    final_nodes = []
    for node in old_nodes:
        new_nodes = []
        if node.text_type != text_type_text:
            final_nodes.append(node)
        else:
            string = node.text
            nonimage_strings = re.split(r"!\[.*?\]\(.*?\)", string)
            image_data = extract_markdown_images(string)
            i=0
            while nonimage_strings[i] != '' and len(image_data) > i:
                new_nodes.append(nonimage_strings[i])
                new_nodes.append(image_data[i])
                i+=1
            if nonimage_strings[i] != '':
                new_nodes.append(nonimage_strings[i])
            elif len(image_data) > i:
                new_nodes.append(image_data[i])
            for node in new_nodes:
                if isinstance(node, str):
                    final_nodes.append(TextNode(node, text_type_text))
                elif isinstance(node, tuple):
                    final_nodes.append(TextNode(node[0],text_type_image,node[1]))
    return final_nodes


def split_nodes_link(old_nodes):
    final_nodes = []
    for node in old_nodes:
        new_nodes = []
        if node.text_type != text_type_text:
            final_nodes.append(node)
        else:
            string = node.text
            nonlink_strings = re.split(r"\[.*?\]\(.*?\)", string)
            link_data = extract_markdown_links(string)
            i=0
            while nonlink_strings[i] != '' and len(link_data) > i:
                new_nodes.append(nonlink_strings[i])
                new_nodes.append(link_data[i])
                i+=1
            if nonlink_strings[i] != '':
                new_nodes.append(nonlink_strings[i])
            elif len(link_data) > i:
                new_nodes.append(link_data[i])
            for node in new_nodes:
                if isinstance(node, str):
                    final_nodes.append(TextNode(node, text_type_text))
                elif isinstance(node, tuple):
                    final_nodes.append(TextNode(node[0],text_type_link,node[1]))
    return final_nodes

# Takes raw text and returns a list of tuples. 
# Each tuple should contain the alt text and the URL of any markdown images. 
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


