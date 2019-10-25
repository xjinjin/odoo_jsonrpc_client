
# -*- coding: utf-8 -*-

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

xml = '''<?xml version="1.0" encoding="UTF-8"?>
<jsds_yhsxxVO>
	<sbbinfo>
		<sbzlbh>10111</sbzlbh> <!-- 申报种类编号 -->
		<ssqq>2019-02-01</ssqq> <!-- 所属期起 -->
		<ssqz>2019-02-28</ssqz> <!-- 所属期止 -->
		<nsrsbh>91110108MA01ATW72J</nsrsbh> <!-- 申报的纳税人识别号 -->
		<area>32</area> <!-- 区域 -->
		<nsqxdm>1</nsqxdm> <!--纳税期限代码 1:月 2:季 3:半年 4:年 5:次-->
	</sbbinfo>
	<!--印花税纳税申报表(新)-->
	<jsds_yhs_sbb>
		<!--本期是否适用增值税小规模纳税人减征政策(减免性质代码：09049901)-->
		<sbbGridlbVO>
			<ewbhxh>1</ewbhxh>
			<!--本期是否适用增值税小规模纳税人减征政策(减免性质代码：09049901)##-->
			<bqsfsyzzsxgmnsrjzzcjmxzdm/>
		</sbbGridlbVO>
		<!--0100 购销合同-->
		<sbbGridlbVO>
			<ewbhxh>2</ewbhxh>
			<!--0100 购销合同##核定征收##核定比例-->
			<gxhthdzshdbl/>
			<!--0100 购销合同##本期已缴税额##核定比例-->
			<gxhtbqyjsehdbl/>
			<!--0100 购销合同##适用税率##核定比例-->
			<gxhtsyslhdbl/>
			<!--0100 购销合同##本期增值税小规模纳税人减征额##核定比例-->
			<gxhtbqzzsxgmnsrjzehdbl/>
			<!--0100 购销合同##核定征收##核定依据金额-->
			<gxhthdzshdyjje/>
			<!--0100 购销合同##减免税额##核定比例-->
			<gxhtjmsehdbl/>
			<!--0100 购销合同##应税凭证-->
			<gxhtyspz/>
			<!--0100 购销合同##本期应补(退)税额##核定比例-->
			<gxhtbqybtsehdbl/>
			<!--0100 购销合同##本期应纳税额##核定比例-->
			<gxhtbqynsehdbl/>
			<!--0100 购销合同##按实征收##计税金额或件数-->
			<gxhtaszsjsjehjs/>
		</sbbGridlbVO>
		<!--0200 加工承揽合同-->
		<sbbGridlbVO>
			<ewbhxh>3</ewbhxh>
			<!--0200 加工承揽合同##本期已缴税额##核定比例-->
			<jgclhtbqyjsehdbl/>
			<!--0200 加工承揽合同##核定征收##核定依据金额-->
			<jgclhthdzshdyjje/>
			<!--0200 加工承揽合同##本期应补(退)税额##核定比例-->
			<jgclhtbqybtsehdbl/>
			<!--0200 加工承揽合同##按实征收##计税金额或件数-->
			<jgclhtaszsjsjehjs/>
			<!--0200 加工承揽合同##适用税率##核定比例-->
			<jgclhtsyslhdbl/>
			<!--0200 加工承揽合同##核定征收##核定比例-->
			<jgclhthdzshdbl/>
			<!--0200 加工承揽合同##减免税额##核定比例-->
			<jgclhtjmsehdbl/>
			<!--0200 加工承揽合同##本期增值税小规模纳税人减征额##核定比例-->
			<jgclhtbqzzsxgmnsrjzehdbl/>
			<!--0200 加工承揽合同##应税凭证-->
			<jgclhtyspz/>
			<!--0200 加工承揽合同##本期应纳税额##核定比例-->
			<jgclhtbqynsehdbl/>
		</sbbGridlbVO>
		<!--0300 建设工程勘察设计合同-->
		<sbbGridlbVO>
			<ewbhxh>4</ewbhxh>
			<!--0300 建设工程勘察设计合同##应税凭证-->
			<jsgckcsjhtyspz/>
			<!--0300 建设工程勘察设计合同##按实征收##计税金额或件数-->
			<jsgckcsjhtaszsjsjehjs/>
			<!--0300 建设工程勘察设计合同##核定征收##核定依据金额-->
			<jsgckcsjhthdzshdyjje/>
			<!--0300 建设工程勘察设计合同##本期增值税小规模纳税人减征额##核定比例-->
			<jsgckcsjhtbqzzsxgmnsrjzehdbl/>
			<!--0300 建设工程勘察设计合同##本期应补(退)税额##核定比例-->
			<jsgckcsjhtbqybtsehdbl/>
			<!--0300 建设工程勘察设计合同##本期应纳税额##核定比例-->
			<jsgckcsjhtbqynsehdbl/>
			<!--0300 建设工程勘察设计合同##本期已缴税额##核定比例-->
			<jsgckcsjhtbqyjsehdbl/>
			<!--0300 建设工程勘察设计合同##核定征收##核定比例-->
			<jsgckcsjhthdzshdbl/>
			<!--0300 建设工程勘察设计合同##适用税率##核定比例-->
			<jsgckcsjhtsyslhdbl/>
			<!--0300 建设工程勘察设计合同##减免税额##核定比例-->
			<jsgckcsjhtjmsehdbl/>
		</sbbGridlbVO>
		<!--0400 建筑安装工程承包合同-->
		<sbbGridlbVO>
			<ewbhxh>5</ewbhxh>
			<!--0400 建筑安装工程承包合同##应税凭证-->
			<jzazgccbhtyspz/>
			<!--0400 建筑安装工程承包合同##本期增值税小规模纳税人减征额##核定比例-->
			<jzazgccbhtbqzzsxgmnsrjzehdbl/>
			<!--0400 建筑安装工程承包合同##本期已缴税额##核定比例-->
			<jzazgccbhtbqyjsehdbl/>
			<!--0400 建筑安装工程承包合同##按实征收##计税金额或件数-->
			<jzazgccbhtaszsjsjehjs/>
			<!--0400 建筑安装工程承包合同##本期应纳税额##核定比例-->
			<jzazgccbhtbqynsehdbl/>
			<!--0400 建筑安装工程承包合同##核定征收##核定依据金额-->
			<jzazgccbhthdzshdyjje/>
			<!--0400 建筑安装工程承包合同##减免税额##核定比例-->
			<jzazgccbhtjmsehdbl/>
			<!--0400 建筑安装工程承包合同##本期应补(退)税额##核定比例-->
			<jzazgccbhtbqybtsehdbl/>
			<!--0400 建筑安装工程承包合同##核定征收##核定比例-->
			<jzazgccbhthdzshdbl/>
			<!--0400 建筑安装工程承包合同##适用税率##核定比例-->
			<jzazgccbhtsyslhdbl/>
		</sbbGridlbVO>
		<!--0500 财产租赁合同-->
		<sbbGridlbVO>
			<ewbhxh>6</ewbhxh>
			<!--0500 财产租赁合同##减免税额##核定比例-->
			<cczlhtjmsehdbl/>
			<!--0500 财产租赁合同##本期应补(退)税额##核定比例-->
			<cczlhtbqybtsehdbl/>
			<!--0500 财产租赁合同##应税凭证-->
			<cczlhtyspz/>
			<!--0500 财产租赁合同##核定征收##核定比例-->
			<cczlhthdzshdbl/>
			<!--0500 财产租赁合同##按实征收##计税金额或件数-->
			<cczlhtaszsjsjehjs/>
			<!--0500 财产租赁合同##本期应纳税额##核定比例-->
			<cczlhtbqynsehdbl/>
			<!--0500 财产租赁合同##本期增值税小规模纳税人减征额##核定比例-->
			<cczlhtbqzzsxgmnsrjzehdbl/>
			<!--0500 财产租赁合同##适用税率##核定比例-->
			<cczlhtsyslhdbl/>
			<!--0500 财产租赁合同##核定征收##核定依据金额-->
			<cczlhthdzshdyjje/>
			<!--0500 财产租赁合同##本期已缴税额##核定比例-->
			<cczlhtbqyjsehdbl/>
		</sbbGridlbVO>
		<!--0600 货物运输合同-->
		<sbbGridlbVO>
			<ewbhxh>7</ewbhxh>
			<!--0600 货物运输合同##本期应补(退)税额##核定比例-->
			<hwyshtbqybtsehdbl/>
			<!--0600 货物运输合同##核定征收##核定比例-->
			<hwyshthdzshdbl/>
			<!--0600 货物运输合同##适用税率##核定比例-->
			<hwyshtsyslhdbl/>
			<!--0600 货物运输合同##本期应纳税额##核定比例-->
			<hwyshtbqynsehdbl/>
			<!--0600 货物运输合同##本期增值税小规模纳税人减征额##核定比例-->
			<hwyshtbqzzsxgmnsrjzehdbl/>
			<!--0600 货物运输合同##核定征收##核定依据金额-->
			<hwyshthdzshdyjje/>
			<!--0600 货物运输合同##减免税额##核定比例-->
			<hwyshtjmsehdbl/>
			<!--0600 货物运输合同##本期已缴税额##核定比例-->
			<hwyshtbqyjsehdbl/>
			<!--0600 货物运输合同##按实征收##计税金额或件数-->
			<hwyshtaszsjsjehjs/>
			<!--0600 货物运输合同##应税凭证-->
			<hwyshtyspz/>
		</sbbGridlbVO>
		<!--0700 仓储保管合同-->
		<sbbGridlbVO>
			<ewbhxh>8</ewbhxh>
			<!--0700 仓储保管合同##本期应补(退)税额##核定比例-->
			<ccbghtbqybtsehdbl/>
			<!--0700 仓储保管合同##应税凭证-->
			<ccbghtyspz/>
			<!--0700 仓储保管合同##按实征收##计税金额或件数-->
			<ccbghtaszsjsjehjs/>
			<!--0700 仓储保管合同##本期增值税小规模纳税人减征额##核定比例-->
			<ccbghtbqzzsxgmnsrjzehdbl/>
			<!--0700 仓储保管合同##减免税额##核定比例-->
			<ccbghtjmsehdbl/>
			<!--0700 仓储保管合同##本期应纳税额##核定比例-->
			<ccbghtbqynsehdbl/>
			<!--0700 仓储保管合同##核定征收##核定比例-->
			<ccbghthdzshdbl/>
			<!--0700 仓储保管合同##核定征收##核定依据金额-->
			<ccbghthdzshdyjje/>
			<!--0700 仓储保管合同##适用税率##核定比例-->
			<ccbghtsyslhdbl/>
			<!--0700 仓储保管合同##本期已缴税额##核定比例-->
			<ccbghtbqyjsehdbl/>
		</sbbGridlbVO>
		<!--0900 财产保险合同-->
		<sbbGridlbVO>
			<ewbhxh>9</ewbhxh>
			<!--0900 财产保险合同##适用税率##核定比例-->
			<ccbxhtsyslhdbl/>
			<!--0900 财产保险合同##核定征收##核定比例-->
			<ccbxhthdzshdbl/>
			<!--0900 财产保险合同##本期增值税小规模纳税人减征额##核定比例-->
			<ccbxhtbqzzsxgmnsrjzehdbl/>
			<!--0900 财产保险合同##应税凭证-->
			<ccbxhtyspz/>
			<!--0900 财产保险合同##核定征收##核定依据金额-->
			<ccbxhthdzshdyjje/>
			<!--0900 财产保险合同##本期已缴税额##核定比例-->
			<ccbxhtbqyjsehdbl/>
			<!--0900 财产保险合同##本期应纳税额##核定比例-->
			<ccbxhtbqynsehdbl/>
			<!--0900 财产保险合同##减免税额##核定比例-->
			<ccbxhtjmsehdbl/>
			<!--0900 财产保险合同##本期应补(退)税额##核定比例-->
			<ccbxhtbqybtsehdbl/>
			<!--0900 财产保险合同##按实征收##计税金额或件数-->
			<ccbxhtaszsjsjehjs/>
		</sbbGridlbVO>
		<!--1000 技术合同-->
		<sbbGridlbVO>
			<ewbhxh>10</ewbhxh>
			<!--1000 技术合同##适用税率##核定比例-->
			<jshtsyslhdbl/>
			<!--1000 技术合同##核定征收##核定比例-->
			<jshthdzshdbl/>
			<!--1000 技术合同##核定征收##核定依据金额-->
			<jshthdzshdyjje/>
			<!--1000 技术合同##按实征收##计税金额或件数-->
			<jshtaszsjsjehjs/>
			<!--1000 技术合同##本期应纳税额##核定比例-->
			<jshtbqynsehdbl/>
			<!--1000 技术合同##本期已缴税额##核定比例-->
			<jshtbqyjsehdbl/>
			<!--1000 技术合同##本期增值税小规模纳税人减征额##核定比例-->
			<jshtbqzzsxgmnsrjzehdbl/>
			<!--1000 技术合同##减免税额##核定比例-->
			<jshtjmsehdbl/>
			<!--1000 技术合同##本期应补(退)税额##核定比例-->
			<jshtbqybtsehdbl/>
			<!--1000 技术合同##应税凭证-->
			<jshtyspz/>
		</sbbGridlbVO>
		<!--1190 产权转移书据-->
		<sbbGridlbVO>
			<ewbhxh>11</ewbhxh>
			<!--1190 产权转移书据##本期应补(退)税额##核定比例-->
			<cqzysjbqybtsehdbl/>
			<!--1190 产权转移书据##本期应纳税额##核定比例-->
			<cqzysjbqynsehdbl/>
			<!--1190 产权转移书据##核定征收##核定比例-->
			<cqzysjhdzshdbl/>
			<!--1190 产权转移书据##本期增值税小规模纳税人减征额##核定比例-->
			<cqzysjbqzzsxgmnsrjzehdbl/>
			<!--1190 产权转移书据##应税凭证-->
			<cqzysjyspz/>
			<!--1190 产权转移书据##按实征收##计税金额或件数-->
			<cqzysjaszsjsjehjs/>
			<!--1190 产权转移书据##核定征收##核定依据金额-->
			<cqzysjhdzshdyjje/>
			<!--1190 产权转移书据##适用税率##核定比例-->
			<cqzysjsyslhdbl/>
			<!--1190 产权转移书据##减免税额##核定比例-->
			<cqzysjjmsehdbl/>
			<!--1190 产权转移书据##本期已缴税额##核定比例-->
			<cqzysjbqyjsehdbl/>
		</sbbGridlbVO>
		<!--1201 营业帐簿-->
		<sbbGridlbVO>
			<ewbhxh>12</ewbhxh>
			<!--1201 营业帐簿##本期已缴税额##核定比例-->
			<yyzbbqyjsehdbl/>
			<!--1201 营业帐簿##核定征收##核定比例-->
			<yyzbhdzshdbl/>
			<!--1201 营业帐簿##本期应纳税额##核定比例-->
			<yyzbbqynsehdbl/>
			<!--1201 营业帐簿##适用税率##核定比例-->
			<yyzbsyslhdbl/>
			<!--1201 营业帐簿##应税凭证-->
			<yyzbyspz/>
			<!--1201 营业帐簿##本期应补(退)税额##核定比例-->
			<yyzbbqybtsehdbl/>
			<!--1201 营业帐簿##按实征收##计税金额或件数-->
			<yyzbaszsjsjehjs/>
			<!--1201 营业帐簿##减免税额##核定比例-->
			<yyzbjmsehdbl/>
			<!--1201 营业帐簿##本期增值税小规模纳税人减征额##核定比例-->
			<yyzbbqzzsxgmnsrjzehdbl/>
			<!--1201 营业帐簿##核定征收##核定依据金额-->
			<yyzbhdzshdyjje/>
			<!--1201 营业帐簿##减免性质代码##核定比例-->
			<yyzbjmxzdmhdbl/>
		</sbbGridlbVO>
		<!--1202 资本增值额(实收资本、资本公积等)-->
		<sbbGridlbVO>
			<ewbhxh>13</ewbhxh>
			<!--1202 资本增值额(实收资本、资本公积等)##按实征收##计税金额或件数-->
			<zbzzesszbzbgjdaszsjsjehjs/>
			<!--1202 资本增值额(实收资本、资本公积等)##减免税额##核定比例-->
			<zbzzesszbzbgjdjmsehdbl/>
			<!--1202 资本增值额(实收资本、资本公积等)##本期已缴税额##核定比例-->
			<zbzzesszbzbgjdbqyjsehdbl/>
			<!--1202 资本增值额(实收资本、资本公积等)##本期应补(退)税额##核定比例-->
			<zbzzesszbzbgjdbqybtsehdbl/>
			<!--1202 资本增值额(实收资本、资本公积等)##核定征收##核定比例-->
			<zbzzesszbzbgjdhdzshdbl/>
			<!--1202 资本增值额(实收资本、资本公积等)##应税凭证-->
			<zbzzesszbzbgjdyspz/>
			<!--1202 资本增值额(实收资本、资本公积等)##核定征收##核定依据金额-->
			<zbzzesszbzbgjdhdzshdyjje/>
			<!--1202 资本增值额(实收资本、资本公积等)##适用税率##核定比例-->
			<zbzzesszbzbgjdsyslhdbl/>
			<!--1202 资本增值额(实收资本、资本公积等)##本期应纳税额##核定比例-->
			<zbzzesszbzbgjdbqynsehdbl/>
			<!--1202 资本增值额(实收资本、资本公积等)##本期增值税小规模纳税人减征额##核定比例-->
			<zbzzesszbzbgjdbqzzsxgmnsrjzehdbl/>
		</sbbGridlbVO>
		<!--1300 权利、许可证照-->
		<sbbGridlbVO>
			<ewbhxh>14</ewbhxh>
			<!--1300 权利、许可证照##按实征收##计税金额或件数-->
			<qlxkzzaszsjsjehjs/>
			<!--1300 权利、许可证照##减免税额##核定比例-->
			<qlxkzzjmsehdbl/>
			<!--1300 权利、许可证照##本期增值税小规模纳税人减征额##核定比例-->
			<qlxkzzbqzzsxgmnsrjzehdbl/>
			<!--1300 权利、许可证照##适用税率##核定比例-->
			<qlxkzzsyslhdbl/>
			<!--1300 权利、许可证照##核定征收##核定比例-->
			<qlxkzzhdzshdbl/>
			<!--1300 权利、许可证照##本期应补(退)税额##核定比例-->
			<qlxkzzbqybtsehdbl/>
			<!--1300 权利、许可证照##本期应纳税额##核定比例-->
			<qlxkzzbqynsehdbl/>
			<!--1300 权利、许可证照##本期已缴税额##核定比例-->
			<qlxkzzbqyjsehdbl/>
			<!--1300 权利、许可证照##应税凭证-->
			<qlxkzzyspz/>
			<!--1300 权利、许可证照##核定征收##核定依据金额-->
			<qlxkzzhdzshdyjje/>
		</sbbGridlbVO>
		<!---->
		<sbbGridlbVO>
			<ewbhxh>15</ewbhxh>
			<!--##减免税额##核定比例-->
			<jmsehdbl/>
			<!--##本期已缴税额##核定比例-->
			<bqyjsehdbl/>
			<!--##本期应补(退)税额##核定比例-->
			<bqybtsehdbl/>
			<!--##本期应纳税额##核定比例-->
			<bqynsehdbl/>
		</sbbGridlbVO>
		<!--代理人(公章)-->
		<sbbGridlbVO>
			<ewbhxh>16</ewbhxh>
			<!--代理人 经办人 姓名 -->
			<dlrgzsyslhdbl/>
		</sbbGridlbVO>
		<!--经办人身份证号码:-->
		<sbbGridlbVO>
			<ewbhxh>17</ewbhxh>
			<!--经办人身份证号码-->
			<jbrsfzhmsyslhdbl/>
		</sbbGridlbVO>
	</jsds_yhs_sbb>
</jsds_yhsxxVO>
'''
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