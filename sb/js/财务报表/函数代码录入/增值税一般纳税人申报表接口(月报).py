# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.230:8069')
c0.login('cic_oa','admin','cic_admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell']    # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']             # 表

# jsds_fjsxxVO

# jsds_fjs_sbb

# sbbinfo
get_value_func_sbzlbh = '''
# 申报种类编号
cell.write({'value':record.sbzlbh})
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
# 申报的纳税人识别号
cell.write({'value':record.nsrsbh})
'''
get_value_func_area = '''
# 地区编码
cell.write({'value':record.dqbm})
'''
get_value_func_nsqxdm = '''
# 纳税期限代码
cell.write({'value':record.nsqxdm})
'''

xml_id = shenbaosheet.search([('name','=','增值税一般纳税人申报表接口(月报)')])[0]  # 174
sbbinfo_id = shenbaosheet.search([('tagname','=','sbbinfo'),('parent_id','=',xml_id)])[0]  # 179
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


# 初始值设置
