
# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.240:8069')
c0.login('test','admin','admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表


#############财务报表-企业会计制度-江苏
# xml
xml_id = shenbaosheet.create({'name': '财务报表-企业会计准则2017-江苏',  'description': '财务报表-企业会计准则2017-江苏', 'dqbm': '32', 'tagname': 'jsxgs_year_cwbb_ybqy_2017xxVO'})

# forms
sbbinfo_id = shenbaosheet.create({'parent_id': xml_id,'name': '申报信息表',  'description': '申报信息表', 'dqbm': '32', 'tagname': 'sbbinfo'})
zcfzb_id = shenbaosheet.create({'parent_id': xml_id,'name': '资产负债表',  'description': '资产负债表', 'dqbm': '32', 'tagname': 'jsxgs_year_cwbb_ybqy_2017_zcfzb'})
lrb_id = shenbaosheet.create({'parent_id': xml_id,'name': '利润表',  'description': '利润表', 'dqbm': '32', 'tagname': 'jsxgs_year_cwbb_ybqy_2017_lrb'})
xjllb_id = shenbaosheet.create({'parent_id': xml_id,'name': '现金流量表',  'description': '现金流量表', 'dqbm': '32', 'tagname': 'jsxgs_year_cwbb_ybqy_2017_xjllb'})

# lines
zcfzb_line_id = shenbaosheet.create({'parent_id': zcfzb_id,'name': '资产负债表的行',  'description': '资产负债表的行', 'dqbm': '32', 'tagname': 'zcfzbGridlbVO'})
lrb_line_id = shenbaosheet.create({'parent_id': lrb_id,'name': '利润表的行',  'description': '利润表的行', 'dqbm': '32', 'tagname': 'lrbGridlbVO'})
xjllb_line_id = shenbaosheet.create({'parent_id': xjllb_id,'name': '现金流量表的行',  'description': '现金流量表的行', 'dqbm': '32', 'tagname': 'xjllbGridlbVO'})

## cells
# 申报信息表     单元格录入
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'sbzlbh'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'ssqq'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'ssqz'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'nsrsbh'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'area'})
shenbaosheetcell.create({'sheet_id': sbbinfo_id, 'tagname': 'nsqxdm'})
# 资产负债表     单元格录入
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'dqjkqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'hbzjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'hbzjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 1, 'tagname': 'dqjkncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'ygyjzjlqqbdjrdqsydjrfzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'ygyjzjlqqbdjrdqsydjrzcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'ygyjzjlqqbdjrdqsydjrzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 2, 'tagname': 'ygyjzjlqqbdjrdqsydjrfzqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'ysjrzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'ysjrfzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'ysjrfzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 3, 'tagname': 'ysjrzcqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'yspjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'yfpjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'yfpjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 4, 'tagname': 'yspjncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yszkqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yszkncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yfzkncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 5, 'tagname': 'yfzkqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yfkxncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yfkxqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yskxncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 6, 'tagname': 'yskxqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'yslxqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'yfzgxcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'yslxncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 7, 'tagname': 'yfzgxcqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'ysglqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'yjsfqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'yjsfncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 8, 'tagname': 'ysglncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'yflxncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'qtyskncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'qtyskqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 9, 'tagname': 'yflxqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'yfglqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'chqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'chncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 10, 'tagname': 'yfglncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'cydszcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'cydszcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'cydsfzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 11, 'tagname': 'cydsfzncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'ynndqdfldzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'ynndqdfldzcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'qtyfkncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 12, 'tagname': 'qtyfkqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'ynndqdfldfzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'qtldzcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'ynndqdfldfzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 13, 'tagname': 'qtldzcncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'qtldfzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'ldzchjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'ldzchjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 14, 'tagname': 'qtldfzncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 15, 'tagname': 'ldfzhjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 15, 'tagname': 'ldfzhjncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 16, 'tagname': 'kgcsjrzcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 16, 'tagname': 'kgcsjrzcncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'cyzdqtzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'cyzdqtzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'zqjkqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 17, 'tagname': 'zqjkncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 18, 'tagname': 'zqyskqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 18, 'tagname': 'zqyskncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 18, 'tagname': 'yfzqncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 18, 'tagname': 'yfzqqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'zqgqtzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'qzyxgncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'qzyxgqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 19, 'tagname': 'zqgqtzncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'tzxfdcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'yxzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'yxzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 20, 'tagname': 'tzxfdcqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'zqyfkncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'gdzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'zqyfkqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 21, 'tagname': 'gdzcqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'zjgcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'zxyfkqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'zxyfkncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 22, 'tagname': 'zjgcqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 23, 'tagname': 'yjfzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 23, 'tagname': 'gcwzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 23, 'tagname': 'gcwzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 23, 'tagname': 'yjfzncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'gdzcqlqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'dysyqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'gdzcqlncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 24, 'tagname': 'dysyncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'dysdsfzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'dysdsfzqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'scxswzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 25, 'tagname': 'scxswzcqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 26, 'tagname': 'yqzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 26, 'tagname': 'qtfldfzncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 26, 'tagname': 'yqzcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 26, 'tagname': 'qtfldfzqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 27, 'tagname': 'fldfzhjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 27, 'tagname': 'wxzcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 27, 'tagname': 'wxzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 27, 'tagname': 'fldfzhjqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 28, 'tagname': 'kfzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 28, 'tagname': 'fzhjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 28, 'tagname': 'kfzcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 28, 'tagname': 'fzhjqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 29, 'tagname': 'syncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 29, 'tagname': 'syqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'zqdtfyqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'sszbhgbncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'zqdtfyncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 30, 'tagname': 'sszbhgbqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'dysdszcqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'qtqygjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'dysdszcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 31, 'tagname': 'qtqygjncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'qtfldzcncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'qzyxg1qmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'qzyxg1ncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 32, 'tagname': 'qtfldzcqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 33, 'tagname': 'yxz1qmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 33, 'tagname': 'yxz1ncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 33, 'tagname': 'fldzchjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 33, 'tagname': 'fldzchjqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 34, 'tagname': 'zbgjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 34, 'tagname': 'zbgjncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 35, 'tagname': 'jkcgncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 35, 'tagname': 'jkcgqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 36, 'tagname': 'qtzhsyncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 36, 'tagname': 'qtzhsyqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 37, 'tagname': 'yygjqmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 37, 'tagname': 'yygjncye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 38, 'tagname': 'wfplrncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 38, 'tagname': 'wfplrqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 39, 'tagname': 'syzqyhgdqyhjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 39, 'tagname': 'syzqyhgdqyhjqmye'})

shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 40, 'tagname': 'ncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 40, 'tagname': 'fzhsyzqyhgdqyhjncye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 40, 'tagname': 'qmye'})
shenbaosheetcell.create({'sheet_id': zcfzb_id,'line': 40, 'tagname': 'fzhsyzqyhgdqyhjqmye'})

# 利润表         单元格录入
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 1, 'tagname': 'yyysrsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 1, 'tagname': 'yyysrbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 2, 'tagname': 'jyycbbqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 2, 'tagname': 'jyycbsqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 3, 'tagname': 'yysjjfjsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 3, 'tagname': 'yysjjfjbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 4, 'tagname': 'xsfybqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 4, 'tagname': 'xsfysqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 5, 'tagname': 'glfybqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 5, 'tagname': 'glfysqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 6, 'tagname': 'cwfysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 6, 'tagname': 'cwfybqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 7, 'tagname': 'zcjzsssqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 7, 'tagname': 'zcjzssbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 8, 'tagname': 'jgyjzbdsyssyhtlbqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 8, 'tagname': 'jgyjzbdsyssyhtlsqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 9, 'tagname': 'tzsyssyhtlsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 9, 'tagname': 'tzsyssyhtlbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 10, 'tagname': 'qzdlyqyhhyqydtzsysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 10, 'tagname': 'qzdlyqyhhyqydtzsybqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 11, 'tagname': 'zcczsyssy-htlsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 11, 'tagname': 'zcczsyssy-htlbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 12, 'tagname': 'qtsysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 12, 'tagname': 'qtsybqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 13, 'tagname': 'eyylrksyhtlbqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 13, 'tagname': 'eyylrksyhtlsqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 14, 'tagname': 'jyywsrsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 14, 'tagname': 'jyywsrbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 15, 'tagname': 'qzfldzcczldbqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 15, 'tagname': 'qzfldzcczldsqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 16, 'tagname': 'jyywzcsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 16, 'tagname': 'jyywzcbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 17, 'tagname': 'qzfldzcczsssqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 17, 'tagname': 'qzfldzcczssbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 18, 'tagname': 'slrzekszeyhtlbqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 18, 'tagname': 'slrzekszeyhtlsqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 19, 'tagname': 'jsdsfybqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 19, 'tagname': 'jsdsfysqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 20, 'tagname': 'sjlrjksyhtlbqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 20, 'tagname': 'sjlrjksyhtlsqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 21, 'tagname': 'ycxjyjlrjksy-htlsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 21, 'tagname': 'ycxjyjlrjksy-htlbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 22, 'tagname': 'yzzjyjlrjksy-htlbqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 22, 'tagname': 'yzzjyjlrjksy-htlsqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 23, 'tagname': 'wqtzhsydshjebqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 23, 'tagname': 'wqtzhsydshjesqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 24, 'tagname': 'yyhbnzfljsydqtzhsysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 24, 'tagname': 'yyhbnzfljsydqtzhsybqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 25, 'tagname': 'zxjlsdsyjhjfzhjzcdbdsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 25, 'tagname': 'zxjlsdsyjhjfzhjzcdbdbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 26, 'tagname': 'qyfxzbtzdwbnzfljsydqtzhsyzxydfesqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 26, 'tagname': 'qyfxzbtzdwbnzfljsydqtzhsyzxydfebqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 27, 'tagname': 'eyhjzfljsydqtzhsysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 27, 'tagname': 'eyhjzfljsydqtzhsybqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 28, 'tagname': 'qyfxzbtzdwyhjzfljsydqtzhsyzxydfesqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 28, 'tagname': 'qyfxzbtzdwyhjzfljsydqtzhsyzxydfebqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 29, 'tagname': 'kgcsjrzcgyjzbdsybqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 29, 'tagname': 'kgcsjrzcgyjzbdsysqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 30, 'tagname': 'jyzdqtzzflkgcsjrzcsysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 30, 'tagname': 'jyzdqtzzflkgcsjrzcsybqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 31, 'tagname': 'xjljtqsydyxbfsqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 31, 'tagname': 'xjljtqsydyxbfbqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 32, 'tagname': 'wbcwbbzscebqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 32, 'tagname': 'wbcwbbzscesqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 33, 'tagname': 'lzhsyzesqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 33, 'tagname': 'lzhsyzebqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 34, 'tagname': 'yjbmgsysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 34, 'tagname': 'yjbmgsybqje'})

shenbaosheetcell.create({'sheet_id': lrb_id,'line': 35, 'tagname': 'exsmgsysqje'})
shenbaosheetcell.create({'sheet_id': lrb_id,'line': 35, 'tagname': 'exsmgsybqje'})

# 现金流量表         单元格录入
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 1, 'tagname': 'xsccpsptglwsddxjsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 1, 'tagname': 'xsccpsptglwsddxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 2, 'tagname': 'sddsffhsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 2, 'tagname': 'sddsffhbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 3, 'tagname': 'sddqtyjyhdygdxjsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 3, 'tagname': 'sddqtyjyhdygdxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 4, 'tagname': 'jyhdxjlrxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 4, 'tagname': 'jyhdxjlrxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 5, 'tagname': 'gmspjslwzfdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 5, 'tagname': 'gmspjslwzfdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 6, 'tagname': 'zfjzgyjwzgzfdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 6, 'tagname': 'zfjzgyjwzgzfdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 7, 'tagname': 'zfdgxsfsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 7, 'tagname': 'zfdgxsfbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 8, 'tagname': 'zfdqtyjyhdygdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 8, 'tagname': 'zfdqtyjyhdygdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 9, 'tagname': 'jyhdxjlcxjsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 9, 'tagname': 'jyhdxjlcxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 10, 'tagname': 'jyhdcsdxjlljesqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 10, 'tagname': 'jyhdcsdxjlljebqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 11, 'tagname': 'shtzsddxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 11, 'tagname': 'shtzsddxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 12, 'tagname': 'qdtzsysddxjsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 12, 'tagname': 'qdtzsysddxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 13, 'tagname': 'czgdzcwxzchqtzqzcshdxjjebqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 13, 'tagname': 'czgdzcwxzchqtzqzcshdxjjesqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 14, 'tagname': 'czzgsjqtyydwsddxjjesqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 14, 'tagname': 'czzgsjqtyydwsddxjjebqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 15, 'tagname': 'sdqtytzhdygdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 15, 'tagname': 'sdqtytzhdygdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 16, 'tagname': 'tzhdxjlrxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 16, 'tagname': 'tzhdxjlrxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 17, 'tagname': 'gjgdzcwxzchqtzqzcszfdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 17, 'tagname': 'gjgdzcwxzchqtzqzcszfdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 18, 'tagname': 'tzzfdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 18, 'tagname': 'tzzfdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 19, 'tagname': 'qdzgsjqtyydwzfdxjjebqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 19, 'tagname': 'qdzgsjqtyydwzfdxjjesqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 20, 'tagname': 'zfqtytzhdygdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 20, 'tagname': 'zfqtytzhdygdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 21, 'tagname': 'tzhdxjlcxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 21, 'tagname': 'tzhdxjlcxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 22, 'tagname': 'tzhdcsdxjlljebqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 22, 'tagname': 'tzhdcsdxjlljesqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 23, 'tagname': 'xstzsddxjsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 23, 'tagname': 'xstzsddxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 24, 'tagname': 'qdjksddxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 24, 'tagname': 'qdjksddxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 25, 'tagname': 'sdqtyczhdygdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 25, 'tagname': 'sdqtyczhdygdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 26, 'tagname': 'czhdxjlrxjsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 26, 'tagname': 'czhdxjlrxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 27, 'tagname': 'chzwzfdxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 27, 'tagname': 'chzwzfdxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 28, 'tagname': 'sqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 28, 'tagname': 'bqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 29, 'tagname': 'zfqtyczhdygdxjsqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 29, 'tagname': 'zfqtyczhdygdxjbqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 30, 'tagname': 'czhdxjlcxjbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 30, 'tagname': 'czhdxjlcxjsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 31, 'tagname': 'czhdcsdxjlljebqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 31, 'tagname': 'czhdcsdxjlljesqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 32, 'tagname': 'shlbddxjjxjdjwdyxbqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 32, 'tagname': 'shlbddxjjxjdjwdyxsqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 33, 'tagname': 'wxjjxjdjwjzjebqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 33, 'tagname': 'wxjjxjdjwjzjesqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 34, 'tagname': 'jqcxjjxjdjwyesqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 34, 'tagname': 'jqcxjjxjdjwyebqje'})

shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 35, 'tagname': 'lqmxjjxjdjwyesqje'})
shenbaosheetcell.create({'sheet_id': xjllb_id,'line': 35, 'tagname': 'lqmxjjxjdjwyebqje'})