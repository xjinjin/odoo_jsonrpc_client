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

from odooClient import ODOO
from datetime import datetime,timedelta
import json
odoo230 =ODOO('http://192.168.1.230:8069',timeout=600)
odoo230.login('cic_oa','admin','cic_admin')
cic_tools = odoo230.env['cic_tools.cic_finance']

res = cic_tools.get_declaration_data('91320214MA1NYKMBXK','2019-07-01','2019-09-30')
print(json.dumps(res,indent=1))
# get_value_func

