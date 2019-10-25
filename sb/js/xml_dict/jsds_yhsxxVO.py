
# -*- coding: utf-8 -*-

# client：根据xml报文，创建所需对象。server：调用服务端功能生成xml框架

from sb.js.xml_dict.dict_xml import xml_to_dict
# import json

from odooClient import ODOO
c0 = ODOO('http://192.168.1.230:8069')
c0.login('cic_oa', 'admin', 'cic_admin')
# c0 = ODOO('http://192.168.1.240:8069')
# c0.login('test', 'admin', 'admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell']  # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']  # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']  # 创建表

xml = '''xml文件内容copy到此处'''
# print(json.dumps(xml_to_dict(xml),indent=4))
xml_dict = xml_to_dict(xml)
# {'jsxgs_zzs_ybnsrxxVO':{'sbbinfo':{'sbzlbh':'10101',...},'jsxgs_zzs_ybnsr_sbb':{'sbbGridlbVO':[{'ewbhxh':'1',...},...]},'jsxgs_zzs_ybnsr_scqy15':None,...}}
# print(list(xml_dict.keys())[0]) #   xml_dict.keys():dict_keys(['jsxgs_zzs_ybnsrxxVO'])
xml_name = list(xml_dict.keys())[0]  # jsxgs_zzs_ybnsrxxVO
forms_name = list(list(xml_dict.values())[0].keys()) # ['sbbinfo', 'jsxgs_zzs_ybnsr_sbb',...]
# xml 创建xml
xml_id = shenbaosheet.create({'name': '印花税纳税申报表-月报-江苏',  'description': '印花税纳税申报表-月报-江苏', 'dqbm': '32', 'tagname': xml_name})
# forms
for form_name in forms_name: # ['sbbinfo', 'jsxgs_zzs_ybnsr_sbb',...]
    # 创建表
    form_id = shenbaosheet.create({'parent_id': xml_id, 'name': form_name, 'description': form_name, 'dqbm': '32', 'tagname': form_name})
    # 非空表 有两种情况    1.字典的value是列表     2.字典
    if xml_dict[xml_name][form_name]:
        # xml--form--line--cell   1.字典的value是列表  {'sbbGridlbVO':[{'ewbhxh':'1',...},...]}
        if isinstance(list(xml_dict[xml_name][form_name].values())[0],list):
            # 创建行
            line_name = list(xml_dict[xml_name][form_name].keys())[0]
            line_id = shenbaosheet.create({'parent_id': form_id, 'name': line_name, 'description': line_name, 'dqbm': '32',
                                 'tagname': line_name})
            # 创建单元格 [{'ewbhxh':'1',...},...]
            for cell_dict in xml_dict[xml_name][form_name][line_name]:
                cell_line_num = int(cell_dict['ewbhxh'])
                cell_name_list = list(cell_dict.keys())
                # ['ewbhxh', 'yybjsffjsqbz', 'yybjs']
                for cell_name in cell_name_list:
                    if cell_name != 'ewbhxh':
                        shenbaosheetcell.create({'sheet_id': form_id, 'line': cell_line_num, 'tagname': cell_name})
        # xml--form--cell   2.字典 ps:直接else就可以，只是让逻辑更清晰   {'sbzlbh':'10101',...}
        if isinstance(xml_dict[xml_name][form_name],dict):
            # 创建单元格
            cell_name_list = list(xml_dict[xml_name][form_name].keys())
            for cell_name in cell_name_list:
                shenbaosheetcell.create({'sheet_id': form_id, 'tagname': cell_name})
    # # 空表 只需要创建表对象即可
    # else:
    #     pass