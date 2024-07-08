import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"

def markdown_to_blocks(markdown):
    markdown = re.sub('\n\n\n+','\n\n',markdown)   
    return markdown.strip('\n').split("\n\n")

def block_to_block_type(block):
    if block[0] == '#':
        return block_type_heading
    elif block.find("```",) == 0 and block.find("```",len(block)-4) != -1:
        return block_type_code
    lines = block.split('/n') 
    passed = True
    for line in lines:
        line.strip()
        if line[0] != '>':
            passed = False
    if passed:
        return block_type_quote
    
    passed = True
    for line in lines:
        line.strip()
        if line[0] != '*' or line[0] != '-' and line[1] != ' ':
            passed = False
    if passed:
        return block_type_ulist

    passed = True
    for line_num in range(len(lines)):
        line = lines[line_num].strip()
        if line[0] != line_num+1 and line[1] != '.' and line[2] != ' ':
            passed = False
    if passed:
        return block_type_olist

    return block_type_paragraph


