# -*- coding: utf-8 -*-

from sb.js.xml_dict.dict_xml import xml_to_dict
import os
from odooClient import ODOO

def create_xml_obj(full_filename):
    # 客户端输入文件名自动创建xml结构的对象，xml--forms--lines--cells。之后在服务端调用创建表向导即可。

    c0 = ODOO('http://192.168.1.230:8069')
    c0.login('cic_oa', 'admin', 'cic_admin')
    shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell']  # 单元格
    shenbaosheet = c0.env['cic_taxsb.shenbaosheet']  # 表

    xml_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'申报提交XML报文')
    file_name = full_filename
    file_name_no_extend, extension_name = os.path.splitext(file_name)
    xml_abspath = os.path.join(xml_dir,file_name)
    with open(xml_abspath,'r',encoding='utf-8') as f:
        xml = f.read()

    xml_dict = xml_to_dict(xml)
    # {'jsxgs_zzs_ybnsrxxVO':{'sbbinfo':{'sbzlbh':'10101',...},'jsxgs_zzs_ybnsr_sbb':{'sbbGridlbVO':[{'ewbhxh':'1',...},...]},'jsxgs_zzs_ybnsr_scqy15':None,...}}
    # print(list(xml_dict.keys())[0]) #   xml_dict.keys():dict_keys(['jsxgs_zzs_ybnsrxxVO'])
    xml_name = list(xml_dict.keys())[0]  # jsxgs_zzs_ybnsrxxVO
    forms_name = list(list(xml_dict.values())[0].keys()) # ['sbbinfo', 'jsxgs_zzs_ybnsr_sbb',...]
    # xml 创建xml
    xml_id = shenbaosheet.create({'name': file_name_no_extend,  'description': file_name_no_extend, 'dqbm': '32', 'tagname': xml_name})
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

if __name__ == '__main__':
    # create_xml_obj('增值税一般纳税人申报表接口(月报).xml')
    # create_xml_obj('印花税纳税申报（报告）表接口(月季报).xml')
    # create_xml_obj('印花税纳税申报表(选报)接口(次报).xml')
    # create_xml_obj('城建税、教育费附加、地方教育附加税(费)申报表(月)接口.xml')
    # 1.上传xml   2.把此功能做在服务端
    pass