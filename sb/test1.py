

# -*- coding: utf-8 -*-

# 生成所有的报文结构，对比是否正确

import os
from odooClient import  ODOO
c0 = ODOO('http://192.168.1.230:8069')
c0.login('cic_oa','admin','cic_admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell']    # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']             # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']   # 创建表

# sheet_id
for root, dirs, files in os.walk('D:\git_jst\project\odoo_jsonrpc_client\sb\js\申报提交XML报文'):
    for file_name in files:
        file_name_no_extend, extension_name = os.path.splitext(file_name)
        shenbaosheet.search([('name','=',file_name_no_extend)])

shenbaosheetwizard.create({'dqbm': '32', 'sheet_id': 108,'account_id': 100, 'startdate': '2019-09-01', 'enddate': '2019-09-30'})
