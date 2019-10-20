# -*- coding: utf-8 -*-
from odooClient import ODOO
# from datetime import datetime,timedelta

odoo230 =ODOO('http://192.168.1.230:8069',timeout=600)
odoo230.login('cic_oa','admin','cic_admin')
cic_tools = odoo230.env['cic_tools.cic_finance']

res = cic_tools.get_declaration_data('91320214MA1NYKMBXK','2019-07-01','2019-09-30')

