# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.230:8069')
c0.login('cic_oa','admin','cic_admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell']    # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']             # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']   # 创建表

# 申报信息
get_value_func_sbzlbh = '''
# 申报种类编号是定死的，比如小企业会计准则就是29806，企业会计准则2017就是B9805
# cell.write({'value':'29806'})
cell.write({'value':record.sbzlbh})
'''

get_value_func_nsqxdm = '''
# 从总账系统获取：申报类型
# decType_dict = {'月度申报':'1','季度申报':'2','半年度申报':'3','年度申报':'4','次度申报':'5'}
# cell.write({'value':decType_dict.get(record.account_id.company_account.decType)})
cell.write({'value':record.nsqxdm})
'''
# 小企业会计准则   申报信息    单元格     取值函数录入
xml_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzzxxVO')])[0]  # 39
sbbinfo_id = shenbaosheet.search([('tagname','=','sbbinfo'),('parent_id','=',xml_id)])[0]  # 45
for cell in shenbaosheet.browse(sbbinfo_id).cells:
    if cell.tagname == 'sbzlbh':
        cell.write({'get_value_func':get_value_func_sbzlbh})
    if cell.tagname == 'nsqxdm':
        cell.write({'get_value_func':get_value_func_nsqxdm})