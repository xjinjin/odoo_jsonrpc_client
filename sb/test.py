
import os
import re

comment_re = re.compile(
    '(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
    re.DOTALL | re.MULTILINE
)

for root, dirs, files in os.walk('D:\git_jst\project\odoo_jsonrpc_client\sb\js\统一报文'):
    # print(root) # 'D:\git_jst\project\odoo_jsonrpc_client\sb\js\统一报文'
    # print(dirs) # []
    # print(files) # ['增值税一般纳税人交付报文_V20191018.json', '增值税小规模交附报文_V20191025.json', '附加税交付报文_V20191015.json']

    for file in files:
        file_name = os.path.join(root,file)
        # print(file_name)
        with open(file_name, 'r', encoding='utf-8') as f:
            content = ''.join(f.readlines())
            ## Looking for comments
            match = comment_re.search(content)
            while match:
                # single line comment
                content = content[:match.start()] + content[match.end():]
                match = comment_re.search(content)

            print(content)

            # Return json file
            # return json.loads(content)

