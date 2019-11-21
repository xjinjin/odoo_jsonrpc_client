
# -*- coding: utf-8 -*-
# 解析JSON文件,去除文件中的注释
import json
import re
# Regular expression for comments
comment_re = re.compile(
    '(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
    re.DOTALL | re.MULTILINE
)
def parse_json(filename):
    """ Parse a JSON file
        First remove comments and then use the json module package
        Comments look like :
            // ...
        or
            /*
            ...
            */
    """
    with open(filename,'r',encoding='utf-8') as f:
        # print(f.readlines())  # ['{\n', '  "doc": {\n', '    "taxParam":{ //申报参数对象\n',..]
        content = ''.join(f.readlines()) #读取每一行内容,存放于列表中.指定字符连接序列中元素
        # print(content)          #str
        # print(type(content))   #str
        ## Looking for comments
        match = comment_re.search(content)
        # print(match)
        while match:
            # single line comment
            content = content[:match.start()] + content[match.end():]
            match = comment_re.search(content)

        # print(content)       # 清除注释
        # print(type(content))
        # Return json file
        return json.loads(content)
if __name__ == '__main__':
    json_file_dict = parse_json('D:\git_jst\project\odoo_jsonrpc_client\sb\js\统一报文\增值税一般纳税人交付报文_V20191018.json')
    # print(type(json_file_dict))




