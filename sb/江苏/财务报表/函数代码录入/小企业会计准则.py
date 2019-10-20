# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.240:8069')
c0.login('test','admin','admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表


get_value_func_zcfzb = '''zcfzb = res.get('资产负债表')
def get_value():
    # dqjkqmye_value = zcfzb.get('line33CurrentEnd')
    # dqjkncye_value = zcfzb.get('line33CurrentBegin')
    if cell.tagname[-4:] == ncye:
        BeginOREnd = 'CurrentBegin'
    if cell.tagname[-4:] == qmye:
        BeginOREnd = 'CurrentEnd'
    value = zcfzb.get('line'+cell.line_num+BeginOREnd)
    return value
get_value()'''

zcfzb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_zcfzb')])[0]
for cell in shenbaosheet.browse(zcfzb_id).cells:
    cell.write({'get_value_func':get_value_func_zcfzb})

get_value_func_lrb = '''lrb = res.get('利润表')
def get_value():
    # 'line1CurrentPrior': 385474.33,
    # 'line1CurrentCurrent': 0.0,
    if cell.tagname[-4:] == 'byje':
        PriorORCurren = 'CurrentBegin'
    if cell.tagname[-6:] == 'bnljje':
        PriorORCurren = 'CurrentEnd'
    value = zcfzb.get('line'+cell.line_num+PriorORCurren)
    return value
get_value()'''

lrb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_lrb')])[0]
for cell in shenbaosheet.browse(lrb_id).cells:
    cell.write({'get_value_func':get_value_func_lrb})