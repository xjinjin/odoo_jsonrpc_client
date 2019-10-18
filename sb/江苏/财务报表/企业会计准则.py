
# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.240:8069')
c0.login('test','admin','admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表


#############财务报表-企业会计制度-江苏
# xml
xml_id = shenbaosheet.create({'name': '财务报表-企业会计制度-江苏',  'description': '财务报表-企业会计制度-江苏', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_kjzdxxVO'})

# forms
sbbinfo_id = shenbaosheet.create({'parent_id': xml_id,'name': '申报信息表',  'description': '申报信息表', 'dqbm': '32', 'tagname': 'sbbinfo'})
zcfzb_id = shenbaosheet.create({'parent_id': xml_id,'name': '资产负债表',  'description': '资产负债表', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_kjzd_zcfzb'})
lrb_id = shenbaosheet.create({'parent_id': xml_id,'name': '利润表',  'description': '利润表', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_kjzd_lrb'})
xjllb_id = shenbaosheet.create({'parent_id': xml_id,'name': '现金流量表',  'description': '现金流量表', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_kjzd_xjllb'})

# lines
zcfzb_line_id = shenbaosheet.create({'parent_id': zcfzb_id,'name': '资产负债表的行',  'description': '资产负债表的行', 'dqbm': '32', 'tagname': 'zcfzbGridlbVO'})
lrb_line_id = shenbaosheet.create({'parent_id': lrb_id,'name': '利润表的行',  'description': '利润表的行', 'dqbm': '32', 'tagname': 'lrbGridlbVO'})

## cells
# 申报信息表     单元格录入
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'sbzlbh'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'ssqq'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'ssqz'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'nsrsbh'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'area'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'nsqxdm'})
# 资产负债表     单元格录入
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'hbzjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'hbzjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'dqjkqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'dqjkncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'dqtzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'yfpjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'dqtzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'yfpjncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'yfzkncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'yfzkqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'yspjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'yspjqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'ysglncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'yszkncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'ysglqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'yszkqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yfgzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yslxqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yslxncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yfgzqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yfflfncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yfflfqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yszkncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yszkqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'yfglqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'qtyskncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'qtyskqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'yfglncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'yfzkqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'yjsjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'yjsjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'yfzkncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'ysbtkncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'qtyjkncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'qtyjkqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'ysbtkqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'chncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'qtyfkncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'chqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'qtyfkqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'ytfyncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'dtfyncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'ytfyqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'dtfyqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'ynndqdzqzqtzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'ynndqdzqzqtzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'yjfzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'yjfzqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'ynndqdzqfzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'ynndqdzqfzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'qtldzcqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'qtldzcncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'qtldfzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'ldzchjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'qtldfzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'ldzchjqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 15, 'tagname': 'zqgqtzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 15, 'tagname': 'ldfzhjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 15, 'tagname': 'zqgqtzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 15, 'tagname': 'ldfzhjncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 16, 'tagname': 'zqzqtzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 16, 'tagname': 'zqzqtzqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'zqjkqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'zqjkncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'zqtzhjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'zqtzhjqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 18, 'tagname': 'yfzqncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 18, 'tagname': 'yfzqqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'gdzcyjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'zqyfkqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'gdzcyjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'zqyfkncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'zxyfkqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'jljzjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'jljzjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'zxyfkncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'qtzqfzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'gdzcjzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'gdzcjzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'qtzqfzncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'zqfzhjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'jgdzcjzzbncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'jgdzcjzzbqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'zqfzhjncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 23, 'tagname': 'gdzcjeqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 23, 'tagname': 'gdzcjencs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'dyskdxqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'gcwzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'dyskdxncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'gcwzncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'zjgcqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'zjgcncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'fzhjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'fzhjqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 26, 'tagname': 'gdzcql1qms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 26, 'tagname': 'gdzcql1ncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 27, 'tagname': 'gdzchjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 27, 'tagname': 'gdzchjqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 28, 'tagname': 'sszbhgbncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 28, 'tagname': 'sszbhgbqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 29, 'tagname': 'wxzcncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 29, 'tagname': 'jyghtzncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 29, 'tagname': 'jyghtzqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 29, 'tagname': 'wxzcqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'zqdtfyqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'sszbhgbjencs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'sszbhgbjeqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'zqdtfyncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'qtzqzcncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'zbgjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'qtzqzcqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'zbgjncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'wxjqtzchjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'yygjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'yygjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'wxjqtzchjqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 33, 'tagname': 'qzfdgyjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 33, 'tagname': 'qzfdgyjncs'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 34, 'tagname': 'wfplrncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 34, 'tagname': 'wfplrqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 35, 'tagname': 'dyskjxncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 35, 'tagname': 'dyskjxqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 35, 'tagname': 'syzqyhgdqyhjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 35, 'tagname': 'syzqyhgdqyhjqms'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 36, 'tagname': 'fzhsyzqyhgdqyzjqms'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 36, 'tagname': 'fzhsyzqyhgdqyzjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 36, 'tagname': 'zchjncs'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 36, 'tagname': 'zchjqms'})

# 利润表         单元格录入
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 1, 'tagname': 'yzyywsrbys'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 1, 'tagname': 'yzyywsrbnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 2, 'tagname': 'jzyywcbbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 2, 'tagname': 'jzyywcbbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 3, 'tagname': 'zyywsjjfjbys'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 3, 'tagname': 'zyywsjjfjbnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 4, 'tagname': 'ezyywlrksyhtlbys'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 4, 'tagname': 'ezyywlrksyhtlbnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 5, 'tagname': 'jqtywlrksyhtlbys'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 5, 'tagname': 'jqtywlrksyhtlbnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 6, 'tagname': 'jyyfybnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 6, 'tagname': 'jyyfybys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 7, 'tagname': 'glfybnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 7, 'tagname': 'glfybys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 8, 'tagname': 'cwfybys'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 8, 'tagname': 'cwfybnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 9, 'tagname': 'syylrksyhtlbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 9, 'tagname': 'syylrksyhtlbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 10, 'tagname': 'jtzsyssyhtlbys'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 10, 'tagname': 'jtzsyssyhtlbnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 11, 'tagname': 'btsrbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 11, 'tagname': 'btsrbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 12, 'tagname': 'yywsrbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 12, 'tagname': 'yywsrbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 13, 'tagname': 'jyywzcbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 13, 'tagname': 'jyywzcbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 14, 'tagname': 'slrzeksyhtlbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 14, 'tagname': 'slrzeksyhtlbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 15, 'tagname': 'jsdsbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 15, 'tagname': 'jsdsbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 16, 'tagname': 'wjlrjksyhtlbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 16, 'tagname': 'wjlrjksyhtlbys'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 17, 'tagname': 'csczbmhbtzdwsdsysnsjs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 17, 'tagname': 'csczbmhbtzdwsdsybnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 18, 'tagname': 'zrzhfsdsssnsjs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 18, 'tagname': 'zrzhfsdssbnljs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 19, 'tagname': 'hjzcbgzjhjslrzebnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 19, 'tagname': 'hjzcbgzjhjslrzesnsjs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 20, 'tagname': 'hjgjbgzjhjslrzebnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 20, 'tagname': 'hjgjbgzjhjslrzesnsjs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 21, 'tagname': 'zwzzssbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 21, 'tagname': 'zwzzsssnsjs'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 22, 'tagname': 'qtbnljs'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 22, 'tagname': 'qtsnsjs'})



#############

# djxx = c0.env['cic_taxsb.djxx']# 创建表
# if not shenbaosheet.browse(35).child_ids:
#     print('空行')
# else:
#     print('有行')

# shenbaosheet.browse(range(1,32)).write({'parent_id':32})
# shenbaosheet.browse(range(2,32)).unlink()
# shenbaosheet.browse(32).child_ids[0].cells
# shenbaosheet.browse(1).cells
# shenbaosheet.browse(33).write({'description':'江苏-小企业会计准则-财务报表'})
# shenbaosheet.browse(1).write({'name':'资产负债表的行'})
# shenbaosheet.create({'name': '江苏-小企业会计准则-财务报表',  'description': 'jsxgs_cwbb_xqykjzzxxVO', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_xqykjzzxxVO'})
# shenbaosheet.create({'parent_id': 33,'name': '利润表',  'description': '利润表', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_xqykjzz_lrb'})
# shenbaosheet.create({'parent_id': 33,'name': '现金流量表',  'description': '现金流量表', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_xqykjzz_xjllb'})
# shenbaosheet.create({'parent_id': 33,'name': '申报信息',  'description': '申报信息', 'dqbm': '32', 'tagname': 'sbbinfo'})
# shenbaosheet.create({'parent_id': 34,'name': '利润表的行',  'description': '利润表的行', 'dqbm': '32', 'tagname': 'lrbGridlbVO'})
#
# shenbaosheetcell.browse(shenbaosheetcell.search([])).write({'sheet_id':1})
# shenbaosheetcell.search([]).write({'sheet_id':1})
# shenbaosheetcell.search([])
# shenbaosheetcell.create({'sheet_id': 36, 'tagname': 'sbzlbh'})
#
# shenbaosheetwizard.create({'dqbm': '32',  'sheet_id': 33,  'startdate': '2019-09-01',  'enddate': '2019-09-30'})
# shenbaosheetwizard.browse(6).create_shenbao_sheet()
# shenbaosheetwizard.browse(6).xml
# shenbaosheetwizard.browse(5).startdate
# shenbaosheetwizard.browse(5).sheet_id.cells

# 创建资产负债表 关联表（已创建id=32）
# shenbaosheet.create({'name': 'zcfzb', 'description': '资产负债表', 'dqbm': '32', 'tagname': 'jsxgs_cwbb_xqykjzz_zcfzb'})

# 创建行 31行 关联表（已创建id=32）
# shenbaosheetcell.browse(range(116,147)).unlink()
# for i in range(1,32):
#     shenbaosheetcell.create({'sheet_id': 32,  'line': i, 'tagname': 'zcfzbGridlbVO'})

# {'sheet_id': 37,'line': 1, 'tagname': 'yyysrbnljje'}
# {'sheet_id': 37,'line': 1, 'tagname': 'yyysrbyje'}
# {'sheet_id': 37,'line': 2, 'tagname': 'jyycbbnljje'}

# shenbaosheetcell.create({'sheet_id': 37,'line': 1, 'tagname': 'yyysrbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 1, 'tagname': 'yyysrbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 2, 'tagname': 'jyycbbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 2, 'tagname': 'jyycbbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 3, 'tagname': 'yysjjfjbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 3, 'tagname': 'yysjjfjbyje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 4, 'tagname': 'qzxfsbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 4, 'tagname': 'qzxfsbnljje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 5, 'tagname': 'yysbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 5, 'tagname': 'yysbyje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 6, 'tagname': 'csjswhsbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 6, 'tagname': 'csjswhsbnljje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 7, 'tagname': 'zysbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 7, 'tagname': 'zysbnljje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 8, 'tagname': 'tdzzsbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 8, 'tagname': 'tdzzsbyje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 9, 'tagname': 'cztdsysfcsccsyhsbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 9, 'tagname': 'cztdsysfcsccsyhsbyje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 10, 'tagname': 'jyfjkczypwfbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 10, 'tagname': 'jyfjkczypwfbnljje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 11, 'tagname': 'xsfybyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 11, 'tagname': 'xsfybnljje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 12, 'tagname': 'qzspwxfbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 12, 'tagname': 'qzspwxfbyje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 13, 'tagname': 'ggfhywxcfbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 13, 'tagname': 'ggfhywxcfbyje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 14, 'tagname': 'glfybnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 14, 'tagname': 'glfybyje'})
#
# shenbaosheetcell.create({'sheet_id': 37,'line': 15, 'tagname': 'qzkbfbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 15, 'tagname': 'qzkbfbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 16, 'tagname': 'ywzdfbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 16, 'tagname': 'ywzdfbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 17, 'tagname': 'yjfybnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 17, 'tagname': 'yjfybyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 18, 'tagname': 'cwfybyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 18, 'tagname': 'cwfybnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 19, 'tagname': 'qzlxfysryhtlbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 19, 'tagname': 'qzlxfysryhtlbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 20, 'tagname': 'jtzsybnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 20, 'tagname': 'jtzsybyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 21, 'tagname': 'eyylrbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 21, 'tagname': 'eyylrbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 22, 'tagname': 'jyywsrbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 22, 'tagname': 'jyywsrbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 23, 'tagname': 'qzzfbzbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 23, 'tagname': 'qzzfbzbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 24, 'tagname': 'jyywzcbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 24, 'tagname': 'jyywzcbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 25, 'tagname': 'qzhzssbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 25, 'tagname': 'qzhzssbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 26, 'tagname': 'wfshdzqzqtzssbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 26, 'tagname': 'wfshdzqzqtzssbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 27, 'tagname': 'wfshdzqgqtzssbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 27, 'tagname': 'wfshdzqgqtzssbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 28, 'tagname': 'zrzhdbkklyszcdssbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 28, 'tagname': 'zrzhdbkklyszcdssbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 29, 'tagname': 'ssznjbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 29, 'tagname': 'ssznjbnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 30, 'tagname': 'slrzebyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 30, 'tagname': 'slrzebnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 31, 'tagname': 'jsdsfybnljje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 31, 'tagname': 'jsdsfybyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 32, 'tagname': 'sjlrbyje'})
# shenbaosheetcell.create({'sheet_id': 37,'line': 32, 'tagname': 'sjlrbnljje'})


# shenbaosheetcell.create({'sheet_id': 36, 'tagname': 'sbzlbh'})
# shenbaosheetcell.create({'sheet_id': 36, 'tagname': 'ssqq'})
# shenbaosheetcell.create({'sheet_id': 36, 'tagname': 'ssqz'})
# shenbaosheetcell.create({'sheet_id': 36, 'tagname': 'nsrsbh'})
# shenbaosheetcell.create({'sheet_id': 36, 'tagname': 'area'})
# shenbaosheetcell.create({'sheet_id': 36, 'tagname': 'nsqxdm'})

# 创建期末和年初（已创建）
# shenbaosheetcell.create({'sheet_id': 1,  'line': 1, 'tagname': 'dqjkqmye'})
# shenbaosheetcell.create({'sheet_id': 1,  'line': 1, 'tagname': 'hbzjncye'})
# shenbaosheetcell.create({'sheet_id': 1,  'line': 1, 'tagname': 'hbzjqmye'})
# shenbaosheetcell.create({'sheet_id': 1,  'line': 1, 'tagname': 'dqjkncye'})
#
# shenbaosheetcell.create({'sheet_id': 2,  'line': 2, 'tagname': 'yfpjqmye'})
# shenbaosheetcell.create({'sheet_id': 2,  'line': 2, 'tagname': 'dqtzqmye'})
# shenbaosheetcell.create({'sheet_id': 2,  'line': 2, 'tagname': 'yfpjncye'})
# shenbaosheetcell.create({'sheet_id': 2,  'line': 2, 'tagname': 'dqtzncye'})
#
# shenbaosheetcell.create({'sheet_id': 3,  'line': 3, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 4,  'line': 4, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 5,  'line': 5, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 6,  'line': 6, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 7,  'line': 7, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 8,  'line': 8, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 9,  'line': 9, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 10,  'line': 10, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 11,  'line': 11, 'tagname': 'zzclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 12,  'line': 12, 'tagname': 'kcclncye'})
# shenbaosheetcell.create({'sheet_id': 12,  'line': 12, 'tagname': 'kcclqmye'})
#
# shenbaosheetcell.create({'sheet_id': 13,  'line': 13, 'tagname': 'zzclqmye'})
# shenbaosheetcell.create({'sheet_id': 13,  'line': 13, 'tagname': 'zqjkqmye'})
# shenbaosheetcell.create({'sheet_id': 13,  'line': 13, 'tagname': 'zzclncye'})
# shenbaosheetcell.create({'sheet_id': 13,  'line': 13, 'tagname': 'zqjkncye'})
#
# shenbaosheetcell.create({'sheet_id': 14,  'line': 14, 'tagname': 'zqyfkncye'})
# shenbaosheetcell.create({'sheet_id': 14,  'line': 14, 'tagname': 'qtldzcqmye'})
# shenbaosheetcell.create({'sheet_id': 14,  'line': 14, 'tagname': 'qtldzcncye'})
# shenbaosheetcell.create({'sheet_id': 14,  'line': 14, 'tagname': 'zqyfkqmye'})
#
# shenbaosheetcell.create({'sheet_id': 15,  'line': 15, 'tagname': 'dysyqmye'})
# shenbaosheetcell.create({'sheet_id': 15,  'line': 15, 'tagname': 'ldzchjqmye'})
# shenbaosheetcell.create({'sheet_id': 15,  'line': 15, 'tagname': 'ldzchjncye'})
# shenbaosheetcell.create({'sheet_id': 15,  'line': 15, 'tagname': 'dysyncye'})
#
# shenbaosheetcell.create({'sheet_id': 16,  'line': 16, 'tagname': 'qtfldfzncye'})
# shenbaosheetcell.create({'sheet_id': 16,  'line': 16, 'tagname': 'qtfldfzqmye'})
#
# shenbaosheetcell.create({'sheet_id': 17,  'line': 17, 'tagname': 'fldfzhjncye'})
# shenbaosheetcell.create({'sheet_id': 17,  'line': 17, 'tagname': 'zqzqtzncye'})
# shenbaosheetcell.create({'sheet_id': 17,  'line': 17, 'tagname': 'zqzqtzqmye'})
# shenbaosheetcell.create({'sheet_id': 17,  'line': 17, 'tagname': 'fldfzhjqmye'})
#
# shenbaosheetcell.create({'sheet_id': 18,  'line': 18, 'tagname': 'zqgqtzqmye'})
# shenbaosheetcell.create({'sheet_id': 18,  'line': 18, 'tagname': 'fzhjncye'})
# shenbaosheetcell.create({'sheet_id': 18,  'line': 18, 'tagname': 'fzhjqmye'})
# shenbaosheetcell.create({'sheet_id': 18,  'line': 18, 'tagname': 'zqgqtzncye'})
#
# shenbaosheetcell.create({'sheet_id': 19,  'line': 19, 'tagname': 'gdzcyjncye'})
# shenbaosheetcell.create({'sheet_id': 19,  'line': 19, 'tagname': 'gdzcyjqmye'})
#
# shenbaosheetcell.create({'sheet_id': 20,  'line': 20, 'tagname': 'jljzjncye'})
# shenbaosheetcell.create({'sheet_id': 20,  'line': 20, 'tagname': 'jljzjqmye'})
#
# shenbaosheetcell.create({'sheet_id': 21,  'line': 21, 'tagname': 'gdzczmjzncye'})
# shenbaosheetcell.create({'sheet_id': 21,  'line': 21, 'tagname': 'gdzczmjzqmye'})
#
# shenbaosheetcell.create({'sheet_id': 22,  'line': 22, 'tagname': 'zjgcncye'})
# shenbaosheetcell.create({'sheet_id': 22,  'line': 22, 'tagname': 'zjgcqmye'})
#
# shenbaosheetcell.create({'sheet_id': 23,  'line': 23, 'tagname': 'gcwzncye'})
# shenbaosheetcell.create({'sheet_id': 23,  'line': 23, 'tagname': 'gcwzqmye'})
#
# shenbaosheetcell.create({'sheet_id': 24,  'line': 24, 'tagname': 'gdzcqlqmye'})
# shenbaosheetcell.create({'sheet_id': 24,  'line': 24, 'tagname': 'gdzcqlncye'})
#
# shenbaosheetcell.create({'sheet_id': 25,  'line': 25, 'tagname': 'scxswzcncye'})
# shenbaosheetcell.create({'sheet_id': 25,  'line': 25, 'tagname': 'scxswzcqmye'})
#
# shenbaosheetcell.create({'sheet_id': 26,  'line': 26, 'tagname': 'wxzcqmye'})
# shenbaosheetcell.create({'sheet_id': 26,  'line': 26, 'tagname': 'wxzcncye'})
# shenbaosheetcell.create({'sheet_id': 26,  'line': 26, 'tagname': 'sszbhgbqmye'})
# shenbaosheetcell.create({'sheet_id': 26,  'line': 26, 'tagname': 'sszbhgbncye'})
#
# shenbaosheetcell.create({'sheet_id': 27,  'line': 27, 'tagname': 'zbgjqmye'})
# shenbaosheetcell.create({'sheet_id': 27,  'line': 27, 'tagname': 'zbgjncye'})
# shenbaosheetcell.create({'sheet_id': 27,  'line': 27, 'tagname': 'kfzcncye'})
# shenbaosheetcell.create({'sheet_id': 27,  'line': 27, 'tagname': 'kfzcqmye'})
#
# shenbaosheetcell.create({'sheet_id': 28,  'line': 28, 'tagname': 'zqdtfyqmye'})
# shenbaosheetcell.create({'sheet_id': 28,  'line': 28, 'tagname': 'zqdtfyncye'})
# shenbaosheetcell.create({'sheet_id': 28,  'line': 28, 'tagname': 'yygjqmye'})
# shenbaosheetcell.create({'sheet_id': 28,  'line': 28, 'tagname': 'yygjncye'})
#
# shenbaosheetcell.create({'sheet_id': 29,  'line': 29, 'tagname': 'wfplrncye'})
# shenbaosheetcell.create({'sheet_id': 29,  'line': 29, 'tagname': 'qtfldzcncye'})
# shenbaosheetcell.create({'sheet_id': 29,  'line': 29, 'tagname': 'wfplrqmye'})
# shenbaosheetcell.create({'sheet_id': 29,  'line': 29, 'tagname': 'qtfldzcqmye'})
#
# shenbaosheetcell.create({'sheet_id': 30,  'line': 30, 'tagname': 'syzqyhjncye'})
# shenbaosheetcell.create({'sheet_id': 30,  'line': 30, 'tagname': 'syzqyhjqmye'})
# shenbaosheetcell.create({'sheet_id': 30,  'line': 30, 'tagname': 'fldzchjncye'})
# shenbaosheetcell.create({'sheet_id': 30,  'line': 30, 'tagname': 'fldzchjqmye'})
#
# shenbaosheetcell.create({'sheet_id': 31,  'line': 31, 'tagname': 'zchjncye'})
# shenbaosheetcell.create({'sheet_id': 31,  'line': 31, 'tagname': 'zchjqmye'})
# shenbaosheetcell.create({'sheet_id': 31,  'line': 31, 'tagname': 'fzhsyzqyhjqmye'})
# shenbaosheetcell.create({'sheet_id': 31,  'line': 31, 'tagname': 'fzhsyzqyhjncye'})
