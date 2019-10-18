# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.240:8069')
c0.login('test','admin','admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表

shenbaosheet.browse(1).cells.write({'sheet_id':32})
shenbaosheet.browse(37).cells.write({'sheet_id':34})
shenbaosheet.browse(32).cells.write({'sheet_id':1})
shenbaosheet.browse(34).cells.write({'sheet_id':37})

shenbaosheetwizard.browse(6).create_shenbao_sheet()
shenbaosheetwizard.browse(6).xml
shenbaosheetwizard.browse(6).temp_dict