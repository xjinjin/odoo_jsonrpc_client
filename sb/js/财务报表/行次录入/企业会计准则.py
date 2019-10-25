
# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.240:8069')
c0.login('test','admin','admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表

# 资产负债表
zcfzb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_kjzd_zcfzb')])[0] # [40]

hbzjncs_id = shenbaosheetcell.search([('sheet_id','=',zcfzb_id),('line','=',1),('tagname','=','hbzjncs')])[0]
shenbaosheetcell.browse(hbzjncs_id).write({'line_num':'1'})

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

