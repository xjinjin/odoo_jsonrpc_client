# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.230:8069')
c0.login('cic_oa','admin','cic_admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell']    # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']             # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']   # 创建表

#from odooClient import  ODOO;c0 = ODOO('http://192.168.1.230:8069');c0.login('cic_oa','admin','cic_admin');shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'];shenbaosheet = c0.env['cic_taxsb.shenbaosheet'];shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']

# cic_ocr_report_taxnum.search_read([],fields = ['decType'])
# cic_tools = c0.env['cic_tools.cic_finance']
# res = cic_tools.get_declaration_data('91320214MA1NYKMBXK','2019-07-01','2019-09-30')
# res = self.env['cic_tools.cic_finance'].get_declaration_data('91320214MA1NYKMBXK', '2019-07-01','2019-09-30')
# shenbaosheetwizard.browse(5).create_shenbao_sheet()
# shenbaosheetwizard.create({'dqbm': '32', 'sheet_id': 39,'account_id': 100, 'startdate': '2019-09-01', 'enddate': '2019-09-30'})

# 资产负债表
get_value_func_zcfzb = '''
zcfzb_dict = res.get('资产负债表')
if cell.tagname[-4:] == 'ncye':
    BeginOREnd = 'CurrentBegin'
if cell.tagname[-4:] == 'qmye':
    BeginOREnd = 'CurrentEnd'
cell_key = 'line' + cell.line_num + BeginOREnd
cell_value = zcfzb_dict.get(cell_key)
cell.write({'key':cell_key,'value':str(cell_value),'temp_dict':str(zcfzb_dict)})
'''
# 表     单元格
zcfzb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_zcfzb')])[0]
for cell in shenbaosheet.browse(zcfzb_id).cells:
    cell.write({'get_value_func':get_value_func_zcfzb})

# 利润表
get_value_func_lrb = '''
lrb_dict = res.get('利润表')
if cell.tagname[-4:] == 'byje':
    PriorORCurren = 'CurrentPrior'
if cell.tagname[-6:] == 'bnljje':
    PriorORCurren = 'CurrentCurrent'
cell_key = 'line' + cell.line_num + PriorORCurren
cell_value = lrb_dict.get(cell_key)
cell.write({'key':cell_key,'value':str(cell_value),'temp_dict':str(lrb_dict)})
'''
# 表     单元格
lrb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_lrb')])[0]
for cell in shenbaosheet.browse(lrb_id).cells:
    cell.write({'get_value_func':get_value_func_lrb})

# 申报信息
get_value_func_sbzlbh = '''
# 申报种类编号是定死的，比如小企业会计准则就是29806，企业会计准则2017就是B9805
# cell.write({'value':'29806'})
cell.write({'value':'record.sbzlbh'})
'''
get_value_func_ssqq = '''
# 等于向导对象的开始日期
cell.write({'value':record.startdate})
'''
get_value_func_ssqz = '''
# 等于向导对象的结束日期
cell.write({'value':record.enddate})
'''
get_value_func_nsrsbh = '''
# 从总账系统获取：record.account_id.levyNum
cell.write({'value':record.account_id.levyNum})
'''
get_value_func_area = '''
# 等于向导对象的dqbm属性
cell.write({'value':record.dqbm})
'''
get_value_func_nsqxdm = '''
# 从总账系统获取：申报类型
decType_dict = {'月度申报':'1','季度申报':'2','半年度申报':'3','年度申报':'4','次度申报':'5'}
# cell.write({'value':decType_dict.get(record.account_id.company_account.decType)})
cell.write({'value':record.nsqxdm})
'''
# 小企业会计准则   申报信息    单元格     取值函数录入
xml_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzzxxVO')])[0]  # 39
sbbinfo_id = shenbaosheet.search([('tagname','=','sbbinfo'),('parent_id','=',xml_id)])[0]  # 45
for cell in shenbaosheet.browse(sbbinfo_id).cells:
    if cell.tagname == 'sbzlbh':
        cell.write({'get_value_func':get_value_func_sbzlbh})
    if cell.tagname == 'ssqq':
        cell.write({'get_value_func':get_value_func_ssqq})
    if cell.tagname == 'ssqz':
        cell.write({'get_value_func':get_value_func_ssqz})
    if cell.tagname == 'nsrsbh':
        cell.write({'get_value_func':get_value_func_nsrsbh})
    if cell.tagname == 'area':
        cell.write({'get_value_func':get_value_func_area})
    if cell.tagname == 'nsqxdm':
        cell.write({'get_value_func':get_value_func_nsqxdm})