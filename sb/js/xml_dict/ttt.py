
# -*- coding: utf-8 -*-

import json
import os
from sb.js.xml_dict.dict_xml import dict_to_xml
from odooClient import ODOO
c0 = ODOO('http://192.168.1.230:8069')
c0.login('cic_oa', 'admin', 'cic_admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell']  # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']  # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']  # 创建表

# for root, dirs, files in os.walk('D:\git_jst\project\odoo_jsonrpc_client\sb\js\申报提交XML报文'):
#         for file_name in files:
#             file_name_no_extend, extension_name = os.path.splitext(file_name)
#             xml_id = shenbaosheet.search([('name', '=', file_name_no_extend)])
#             shenbaosheetwizard.browse(7).write({'sheet_id': xml_id[0]})
#             shenbaosheetwizard.browse(7).create_shenbao_sheet()
#             print()
#             print(shenbaosheetwizard.browse(7).xml,xml_id)

# 统一报文：json转dict转xml
temp_dict = {
	"doc":{
		"taxParam":{
			"nsrsbh":"",
			"nsrmc":"",
			"sbrq":"2019-10-01",
			"skssqq":"2019-09-01",
			"skssqz":"2018-09-30",
			"sz":"fjs"
		},
		"fjsslxxForm":{
			"dlr": "",
			"dlrsfzh": "",

			"smrxm":"",
			"dzdw":"",
			"jsyjxgyy":""
		},
		"fjsnsrxxForm": {
			"lxfs": ""
		},
		"fjsData":{
			"fjssbb":{
				"sbxxGrid":{
					"sbxxJbxxGridlbVO":{
						"bqsfsyzzsxgmnsrjzzc": "N",
						"jzblcswhjss": "0",
						"jzbljyffj": "0",
						"jzbldfjyfj": "0",
						"bqsfsycjrhxqyjzzc": "N",
						"dqxztze": "0",
						"sqldkdmje": "0",
						"jzxqkdmje": "0"
					},
					"sbxxhjGridlbVO":{
						"zhj": "0",
						"bqynsfehj": "0",
						"jmehj": "0",
						"bqcjrhxqydmjehj": "0",
						"phjmsehj": "0",
						"bqyjsehj": "0",
						"bqybtsehj": "0"
					},
					"sbxxGridlbVO":[
						{
							"ewbhxh":"1",
							"zsxmMc":"城市维护建设税",
							"zspmMc":"市区（增值税附征）",
							"ybzzs": "0",
							"zzsmdse": "0",
							"xfs": "0",
							"yys": "0",
							"hj": "0",
							"sl1": "0",
							"bqynsfe": "0",
							"jmxzDm":"",
							"jmxzdmMc":"",
							"jme": "0",
							"bqyjse": "0",
							"bqybtse": "0",


							"zsxmDm":"10109",
							"zspmDm":"101090101",
							"phjmxzMc":"",
							"phjzbl":"0",
							"cjrhjmxzMc":"0",
							"bqcjrhxqydmje":"0"
						},
						{
							"ewbhxh":"2",
							"zsxmMc":"教育费附加",
							"zspmMc":"增值税教育费附加",
							"ybzzs": "0",
							"zzsmdse": "0",
							"xfs": "0",
							"yys": "0",
							"hj": "0",
							"sl1": "0",
							"bqynsfe": "0",
							"jmxzDm":"",
							"jmxzdmMc":"",
							"jme": "0",
							"bqyjse": "0",
							"bqybtse": "0",

							"zsxmDm":"10109",
							"zspmDm":"101090101",
							"phjmxzMc":"",
							"phjzbl":"0",
							"cjrhjmxzMc":"0",
							"bqcjrhxqydmje":"0"
						},
						{
							"ewbhxh":"3",
							"zsxmMc":"地方教育附加",
							"zspmMc":"增值税地方教育附加",
							"ybzzs": "0",
							"zzsmdse": "0",
							"xfs": "0",
							"yys": "0",
							"hj": "0",
							"sl1": "0",
							"bqynsfe": "0",
							"jmxzDm":"",
							"jmxzdmMc":"",
							"jme": "0",
							"bqyjse": "0",
							"bqybtse": "0",

							"zsxmDm":"10109",
							"zspmDm":"101090101",
							"phjmxzMc":"",
							"phjzbl":"0",
							"cjrhjmxzMc":"0",
							"bqcjrhxqydmje":"0"
						}
					]
				}
			}
		}
	}
}
# print(dict_to_xml(temp_dict))

import json
import re
# Regular expression for comments
comment_re = re.compile(
    '(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
    re.DOTALL | re.MULTILINE
)
def parse_json():
    """ Parse a JSON file
        First remove comments and then use the json module package
        Comments look like :
            // ...
        or
            /*
            ...
            */
    """
    for root, dirs, files in os.walk('D:\git_jst\project\odoo_jsonrpc_client\sb\js\申报提交XML报文'):
        for file_name in files:
            with open(file_name,'r',encoding='utf-8') as f:
                content = ''.join(f.readlines())
                ## Looking for comments
                match = comment_re.search(content)
                while match:
                    # single line comment
                    content = content[:match.start()] + content[match.end():]
                    match = comment_re.search(content)

                print(content)
                # Return json file
                return json.loads(content)

