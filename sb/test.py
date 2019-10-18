# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.240:8069')
c0.login('test','admin','admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表

# 小企业会计准则   # 6
shenbaosheetwizard.create({'dqbm': '32',  'sheet_id': 33,  'startdate': '2019-09-01',  'enddate': '2019-09-30'})
# 企业会计制度     # 7
shenbaosheetwizard.create({'dqbm': '32',  'sheet_id': 38,  'startdate': '2019-09-01',  'enddate': '2019-09-30'})
# 企业会计准则2017 # 8
shenbaosheetwizard.create({'dqbm': '32',  'sheet_id': 45,  'startdate': '2019-09-01',  'enddate': '2019-09-30'})


shenbaosheetwizard.browse(8).create_shenbao_sheet()
shenbaosheetwizard.browse(7).xml
shenbaosheetwizard.browse(8).temp_dict