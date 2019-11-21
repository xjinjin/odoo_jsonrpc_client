
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    for root, dirs, files in os.walk('D:\git_jst\project\odoo_jsonrpc_client\sb\js\申报提交XML报文'):
        for file_name in files:
            file_name_no_extend, extension_name = os.path.splitext(file_name)
            if extension_name == '.xml' or extension_name == '.json':
                print(file_name)

