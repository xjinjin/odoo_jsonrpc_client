# -*- coding: utf-8 -*-
from odooClient import ODOO
# from datetime import datetime,timedelta

odoo230 =ODOO('http://192.168.1.230:8069',timeout=600)
odoo230.login('cic_oa','admin','cic_admin')
cic_tools = odoo230.env['cic_tools.cic_finance']

res = cic_tools.get_declaration_data('91320214MA1NYKMBXK','2019-07-01','2019-09-30')

# res = self.env['cic_tools.cic_finance'].get_declaration_data('91320214MA1NYKMBXK','2019-07-01','2019-09-30')

# 资产负债表
zcfzb = res.get('资产负债表')
def get_value():
    # dqjkqmye_value = zcfzb.get('line33CurrentEnd')
    # dqjkncye_value = zcfzb.get('line33CurrentBegin')
    if cell.tagname[-4:] == ncye:
        BeginOREnd = 'CurrentBegin'
    if cell.tagname[-4:] == qmye:
        BeginOREnd = 'CurrentEnd'
    value = zcfzb.get('line'+cell.line_num+BeginOREnd)
    return value
get_value()


# # 利润表
lrb = res.get('利润表')
def get_value():
    # 'line1CurrentPrior': 385474.33,
    # 'line1CurrentCurrent': 0.0,
    if cell.tagname[-4:] == 'byje':
        PriorORCurren = 'CurrentBegin'
    if cell.tagname[-6:] == 'bnljje':
        PriorORCurren = 'CurrentEnd'
    value = zcfzb.get('line'+cell.line_num+PriorORCurren)
    return value
get_value()

# 现金流量表
# xjllb = res.get('现金流量表')

