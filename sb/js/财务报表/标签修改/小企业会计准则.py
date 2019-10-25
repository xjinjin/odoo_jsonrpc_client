# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.230:8069')
c0.login('cic_oa','admin','cic_admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表

# 资产负债表 行次
xqykjzz_zcfzb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_zcfzb')])[0]

# 短期借款31	货币资金1
dqjkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','31'),('line','=',1)])[0]
shenbaosheetcell.browse(dqjkqmye_id).write({'tagname':'dqjkqmye'})
dqjkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','31'),('line','=',1)])[1]
shenbaosheetcell.browse(dqjkncye_id).write({'tagname':'dqjkncye'})
hbzjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','1'),('line','=',1)])[0]
shenbaosheetcell.browse(hbzjncye_id).write({'tagname':'hbzjncye'})
hbzjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','1'),('line','=',1)])[1]
shenbaosheetcell.browse(hbzjqmye_id).write({'tagname':'hbzjqmye'})

# 应付票据32	短期投资2
yfpjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','32'),('line','=',2)])[0]
shenbaosheetcell.browse(yfpjqmye_id).write({'tagname':'yfpjqmye'})
yfpjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','32'),('line','=',2)])[1]
shenbaosheetcell.browse(yfpjncye_id).write({'tagname':'yfpjncye'})
dqtzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','2'),('line','=',2)])[0]
shenbaosheetcell.browse(dqtzqmye_id).write({'tagname':'dqtzqmye'})
dqtzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','2'),('line','=',2)])[1]
shenbaosheetcell.browse(dqtzncye_id).write({'tagname':'dqtzncye'})

# 应收票据3	应付账款33
yspjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','3'),('line','=',3)])[0]
shenbaosheetcell.browse(yspjqmye_id).write({'tagname':'yspjqmye'})
yspjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','3'),('line','=',3)])[1]
shenbaosheetcell.browse(yspjncye_id).write({'tagname':'yspjncye'})
yfzkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','33'),('line','=',3)])[0]
shenbaosheetcell.browse(yfzkncye_id).write({'tagname':'yfzkncye'})
yfzkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','33'),('line','=',3)])[1]
shenbaosheetcell.browse(yfzkqmye_id).write({'tagname':'yfzkqmye'})

# 预收帐款34	应收账款4
ygszkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','4'),('line','=',4)])[0]
shenbaosheetcell.browse(ygszkqmye_id).write({'tagname':'ygszkqmye'})
ygszkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','4'),('line','=',4)])[1]
shenbaosheetcell.browse(ygszkncye_id).write({'tagname':'ygszkncye'})
yszkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','34'),('line','=',4)])[0]
shenbaosheetcell.browse(yszkqmye_id).write({'tagname':'yszkqmye'})
yszkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','34'),('line','=',4)])[1]
shenbaosheetcell.browse(yszkncye_id).write({'tagname':'yszkncye'})

# 预付账款5	应付职工薪酬35
yfzkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','5'),('line','=',5)])[0]
shenbaosheetcell.browse(yfzkqmye_id).write({'tagname':'yfzkqmye'})
yfzkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','5'),('line','=',5)])[1]
shenbaosheetcell.browse(yfzkncye_id).write({'tagname':'yfzkncye'})
yfzgxcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','35'),('line','=',5)])[0]
shenbaosheetcell.browse(yfzgxcncye_id).write({'tagname':'yfzgxcncye'})
yfzgxcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','35'),('line','=',5)])[1]
shenbaosheetcell.browse(yfzgxcqmye_id).write({'tagname':'yfzgxcqmye'})

# 应收股利6	应交税费36
ysglqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','6'),('line','=',6)])[0]
shenbaosheetcell.browse(ysglqmye_id).write({'tagname':'ysglqmye'})
ysglncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','6'),('line','=',6)])[1]
shenbaosheetcell.browse(ysglncye_id).write({'tagname':'ysglncye'})
yjsfncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','36'),('line','=',6)])[0]
shenbaosheetcell.browse(yjsfncye_id).write({'tagname':'yjsfncye'})
yjsfqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','36'),('line','=',6)])[1]
shenbaosheetcell.browse(yjsfqmye_id).write({'tagname':'yjsfqmye'})

# 应付利息7	应收利息37
yflxncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','7'),('line','=',7)])[0]
shenbaosheetcell.browse(yflxncye_id).write({'tagname':'yflxncye'})
yflxqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','7'),('line','=',7)])[1]
shenbaosheetcell.browse(yflxqmye_id).write({'tagname':'yflxqmye'})
yslxqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','37'),('line','=',7)])[0]
shenbaosheetcell.browse(yslxqmye_id).write({'tagname':'yslxqmye'})
yslxncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','37'),('line','=',7)])[1]
shenbaosheetcell.browse(yslxncye_id).write({'tagname':'slxncye'})

# 其他应收款8	应付利润38
qtyskncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','8'),('line','=',8)])[0]
shenbaosheetcell.browse(qtyskncye_id).write({'tagname':'qtyskncye'})
qtyskqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','8'),('line','=',8)])[1]
shenbaosheetcell.browse(qtyskqmye_id).write({'tagname':'qtyskqmye'})
yflrncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','38'),('line','=',8)])[0]
shenbaosheetcell.browse(yflrncye_id).write({'tagname':'yflrncye'})
yflrqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','38'),('line','=',8)])[1]
shenbaosheetcell.browse(yflrqmye_id).write({'tagname':'yflrqmye'})

# 其他应付款39	存货9
chqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','9'),('line','=',9)])[0]
shenbaosheetcell.browse(chqmye_id).write({'tagname':'chqmye'})
chncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','9'),('line','=',9)])[1]
shenbaosheetcell.browse(chncye_id).write({'tagname':'chncye'})
qtyfkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','39'),('line','=',9)])[0]
shenbaosheetcell.browse(qtyfkncye_id).write({'tagname':'qtyfkncye'})
qtyfkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','39'),('line','=',9)])[1]
shenbaosheetcell.browse(qtyfkqmye_id).write({'tagname':'qtyfkqmye'})

# 其中：原材料10	其他流动负债40
qzyclncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','10'),('line','=',10)])[0]
shenbaosheetcell.browse(qzyclncye_id).write({'tagname':'qzyclncye'})
qzyclqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','10'),('line','=',10)])[1]
shenbaosheetcell.browse(qzyclqmye_id).write({'tagname':'qzyclqmye'})
qtldfzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','40'),('line','=',10)])[0]
shenbaosheetcell.browse(qtldfzqmye_id).write({'tagname':'qtldfzqmye'})
qtldfzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','40'),('line','=',10)])[1]
shenbaosheetcell.browse(qtldfzncye_id).write({'tagname':'qtldfzncye'})

# 在产品11	流动负债合计41
zcpncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','11'),('line','=',11)])[0]
shenbaosheetcell.browse(zcpncye_id).write({'tagname':'zcpncye'})
zcpqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','11'),('line','=',11)])[1]
shenbaosheetcell.browse(zcpqmye_id).write({'tagname':'zcpqmye'})
ldfzhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','41'),('line','=',11)])[0]
shenbaosheetcell.browse(ldfzhjqmye_id).write({'tagname':'ldfzhjqmye'})
ldfzhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','41'),('line','=',11)])[1]
shenbaosheetcell.browse(ldfzhjncye_id).write({'tagname':'ldfzhjncye'})

# 库存材料12	非流动负债
kcclncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','12'),('line','=',12)])[0]
shenbaosheetcell.browse(kcclncye_id).write({'tagname':'kcclncye'})
kcclqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','12'),('line','=',12)])[1]
shenbaosheetcell.browse(kcclqmye_id).write({'tagname':'kcclqmye'})

# 周转材料13	长期借款42
zzclqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','13'),('line','=',13)])[0]
shenbaosheetcell.browse(zzclqmye_id).write({'tagname':'zzclqmye'})
zzclncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','13'),('line','=',13)])[1]
shenbaosheetcell.browse(zzclncye_id).write({'tagname':'zzclncye'})
zqjkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','42'),('line','=',13)])[0]
shenbaosheetcell.browse(zqjkqmye_id).write({'tagname':'zqjkqmye'})
zqjkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','42'),('line','=',13)])[1]
shenbaosheetcell.browse(zqjkncye_id).write({'tagname':'zqjkncye'})

# 其他流动资产14	长期应付款43
qtldzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','14'),('line','=',14)])[0]
shenbaosheetcell.browse(qtldzcqmye_id).write({'tagname':'qtldzcqmye'})
qtldzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','14'),('line','=',14)])[1]
shenbaosheetcell.browse(qtldzcncye_id).write({'tagname':'qtldzcncye'})
zqyfkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','43'),('line','=',14)])[0]
shenbaosheetcell.browse(zqyfkncye_id).write({'tagname':'zqyfkncye'})
zqyfkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','43'),('line','=',14)])[1]
shenbaosheetcell.browse(zqyfkqmye_id).write({'tagname':'zqyfkqmye'})

# 流动资产合计15	递延收益44
ldzchjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','15'),('line','=',15)])[0]
shenbaosheetcell.browse(ldzchjqmye_id).write({'tagname':'ldzchjqmye'})
ldzchjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','15'),('line','=',15)])[1]
shenbaosheetcell.browse(ldzchjncye_id).write({'tagname':'ldzchjncye'})
dysyqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','44'),('line','=',15)])[0]
shenbaosheetcell.browse(dysyqmye_id).write({'tagname':'dysyqmye'})
dysyncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','44'),('line','=',15)])[1]
shenbaosheetcell.browse(dysyncye_id).write({'tagname':'dysyncye'})

# 非流动资产	其他非流动负债45
qtfldfzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','45'),('line','=',16)])[0]
shenbaosheetcell.browse(qtfldfzncye_id).write({'tagname':'qtfldfzncye'})
qtfldfzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','45'),('line','=',16)])[1]
shenbaosheetcell.browse(qtfldfzqmye_id).write({'tagname':'qtfldfzqmye'})

# 长期债券投资16	非流动负债合计46
zqzqtzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','16'),('line','=',17)])[0]
shenbaosheetcell.browse(zqzqtzncye_id).write({'tagname':'zqzqtzncye'})
zqzqtzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','16'),('line','=',17)])[1]
shenbaosheetcell.browse(zqzqtzqmye_id).write({'tagname':'zqzqtzqmye'})
fldfzhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','46'),('line','=',17)])[0]
shenbaosheetcell.browse(fldfzhjncye_id).write({'tagname':'fldfzhjncye'})
fldfzhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','46'),('line','=',17)])[1]
shenbaosheetcell.browse(fldfzhjqmye_id).write({'tagname':'fldfzhjqmye'})

# 长期股权投资17	负债合计47
zqgqtzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','17'),('line','=',18)])[0]
shenbaosheetcell.browse(zqgqtzqmye_id).write({'tagname':'zqgqtzqmye'})
zqgqtzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','17'),('line','=',18)])[1]
shenbaosheetcell.browse(zqgqtzncye_id).write({'tagname':'zqgqtzncye'})
fzhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','47'),('line','=',18)])[0]
shenbaosheetcell.browse(fzhjncye_id).write({'tagname':'fzhjncye'})
fzhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','47'),('line','=',18)])[1]
shenbaosheetcell.browse(fzhjqmye_id).write({'tagname':'fzhjqmye'})

# 固定资产原价18
gdzcyjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','18'),('line','=',19)])[0]
shenbaosheetcell.browse(gdzcyjncye_id).write({'tagname':'gdzcyjncye'})
gdzcyjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','18'),('line','=',19)])[1]
shenbaosheetcell.browse(gdzcyjqmye_id).write({'tagname':'gdzcyjqmye'})

# 减：累计折旧19
jljzjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','19'),('line','=',20)])[0]
shenbaosheetcell.browse(jljzjncye_id).write({'tagname':'jljzjncye'})
jljzjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','19'),('line','=',20)])[1]
shenbaosheetcell.browse(jljzjqmye_id).write({'tagname':'jljzjqmye'})

# 固定资产账面价值20
gdzczmjzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','20'),('line','=',21)])[0]
shenbaosheetcell.browse(gdzczmjzncye_id).write({'tagname':'gdzczmjzncye'})
gdzczmjzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','20'),('line','=',21)])[1]
shenbaosheetcell.browse(gdzczmjzqmye_id).write({'tagname':'gdzczmjzqmye'})

# 在建工程21
zjgcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','21'),('line','=',22)])[0]
shenbaosheetcell.browse(zjgcncye_id).write({'tagname':'zjgcncye'})
zjgcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','21'),('line','=',22)])[1]
shenbaosheetcell.browse(zjgcqmye_id).write({'tagname':'zjgcqmye'})

# 工程物资22
gcwzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','22'),('line','=',23)])[0]
shenbaosheetcell.browse(gcwzncye_id).write({'tagname':'gcwzncye'})
gcwzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','22'),('line','=',23)])[1]
shenbaosheetcell.browse(gcwzqmye_id).write({'tagname':'gcwzqmye'})

# 固定资产清理23
gdzcqlqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','23'),('line','=',24)])[0]
shenbaosheetcell.browse(gdzcqlqmye_id).write({'tagname':'gdzcqlqmye'})
gdzcqlncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','23'),('line','=',24)])[1]
shenbaosheetcell.browse(gdzcqlncye_id).write({'tagname':'gdzcqlncye'})

# 生产性生物资产24	所有者权益（或股东权益）
scxswzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','24'),('line','=',25)])[0]
shenbaosheetcell.browse(scxswzcncye_id).write({'tagname':'scxswzcncye'})
scxswzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','24'),('line','=',25)])[1]
shenbaosheetcell.browse(scxswzcqmye_id).write({'tagname':'scxswzcqmye'})

# 无形资产25	实收资本（或股本）48
wxzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','25'),('line','=',26)])[0]
shenbaosheetcell.browse(wxzcqmye_id).write({'tagname':'wxzcqmye'})
wxzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','25'),('line','=',26)])[1]
shenbaosheetcell.browse(wxzcncye_id).write({'tagname':'wxzcncye'})
sszbhgbqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','48'),('line','=',26)])[0]
shenbaosheetcell.browse(sszbhgbqmye_id).write({'tagname':'sszbhgbqmye'})
sszbhgbncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','48'),('line','=',26)])[1]
shenbaosheetcell.browse(sszbhgbncye_id).write({'tagname':'sszbhgbncye'})

# 开发支出26	资本公积49
kfzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','26'),('line','=',27)])[0]
shenbaosheetcell.browse(kfzcncye_id).write({'tagname':'kfzcncye'})
kfzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','26'),('line','=',27)])[1]
shenbaosheetcell.browse(kfzcqmye_id).write({'tagname':'kfzcqmye'})
zbgjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','49'),('line','=',27)])[0]
shenbaosheetcell.browse(zbgjqmye_id).write({'tagname':'zbgjqmye'})
zbgjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','49'),('line','=',27)])[1]
shenbaosheetcell.browse(zbgjncye_id).write({'tagname':'zbgjncye'})

# 长期待摊费用27	盈余公积50
zqdtfyqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','27'),('line','=',28)])[0]
shenbaosheetcell.browse(zqdtfyqmye_id).write({'tagname':'zqdtfyqmye'})
zqdtfyncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','27'),('line','=',28)])[1]
shenbaosheetcell.browse(zqdtfyncye_id).write({'tagname':'zqdtfyncye'})
yygjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','50'),('line','=',28)])[0]
shenbaosheetcell.browse(yygjqmye_id).write({'tagname':'yygjqmye'})
yygjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','50'),('line','=',28)])[1]
shenbaosheetcell.browse(yygjncye_id).write({'tagname':'yygjncye'})

# 其他非流动资产28	未分配利润51
qtfldzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','28'),('line','=',29)])[0]
shenbaosheetcell.browse(qtfldzcncye_id).write({'tagname':'qtfldzcncye'})
qtfldzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','28'),('line','=',29)])[1]
shenbaosheetcell.browse(qtfldzcqmye_id).write({'tagname':'qtfldzcqmye'})
wfplrncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','51'),('line','=',29)])[0]
shenbaosheetcell.browse(wfplrncye_id).write({'tagname':'wfplrncye'})
wfplrqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','51'),('line','=',29)])[1]
shenbaosheetcell.browse(wfplrqmye_id).write({'tagname':'wfplrqmye'})

# 非流动资产合计29	所有者权益（或股东权益）合计52
fldzchjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','29'),('line','=',30)])[0]
shenbaosheetcell.browse(fldzchjncye_id).write({'tagname':'fldzchjncye'})
fldzchjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','29'),('line','=',30)])[1]
shenbaosheetcell.browse(fldzchjqmye_id).write({'tagname':'fldzchjqmye'})
syzqyhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','52'),('line','=',30)])[0]
shenbaosheetcell.browse(syzqyhjncye_id).write({'tagname':'syzqyhjncye'})
syzqyhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','52'),('line','=',30)])[1]
shenbaosheetcell.browse(syzqyhjqmye_id).write({'tagname':'syzqyhjqmye'})

# 资产合计30	负债和所有者权益（或股东权益）总计53
zchjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','30'),('line','=',31)])[0]
shenbaosheetcell.browse(zchjncye_id).write({'tagname':'zchjncye'})
zchjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','30'),('line','=',31)])[1]
shenbaosheetcell.browse(zchjqmye_id).write({'tagname':'zchjqmye'})
fzhsyzqyhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','53'),('line','=',31)])[0]
shenbaosheetcell.browse(fzhsyzqyhjqmye_id).write({'tagname':'fzhsyzqyhjqmye'})
fzhsyzqyhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('line_num','=','53'),('line','=',31)])[1]
shenbaosheetcell.browse(fzhsyzqyhjncye_id).write({'tagname':'fzhsyzqyhjncye'})


# 利润表 行次
xqykjzz_lrb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_lrb')])[0]

yyysrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','1'),('line','=',1)])[0]
shenbaosheetcell.browse(yyysrbnljje_id).write({'tagname':'yyysrbnljje'})
yyysrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','1'),('line','=',1)])[1]
shenbaosheetcell.browse(yyysrbyje_id).write({'tagname':'yyysrbyje'})

jyycbbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','2'),('line','=',2)])[0]
shenbaosheetcell.browse(jyycbbnljje_id).write({'tagname':'jyycbbnljje'})
jyycbbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','2'),('line','=',2)])[1]
shenbaosheetcell.browse(jyycbbyje_id).write({'tagname':'jyycbbyje'})

yysjjfjbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','3'),('line','=',3)])[0]
shenbaosheetcell.browse(yysjjfjbnljje_id).write({'tagname':'yysjjfjbnljje'})
yysjjfjbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','3'),('line','=',3)])[1]
shenbaosheetcell.browse(yysjjfjbyje_id).write({'tagname':'yysjjfjbyje'})

qzxfsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','4'),('line','=',4)])[0]
shenbaosheetcell.browse(qzxfsbyje_id).write({'tagname':'qzxfsbyje'})
qzxfsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','4'),('line','=',4)])[1]
shenbaosheetcell.browse(qzxfsbnljje_id).write({'tagname':'qzxfsbnljje'})

yysbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','5'),('line','=',5)])[0]
shenbaosheetcell.browse(yysbnljje_id).write({'tagname':'yysbnljje'})
yysbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','5'),('line','=',5)])[1]
shenbaosheetcell.browse(yysbyje_id).write({'tagname':'yysbyje'})

csjswhsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','6'),('line','=',6)])[0]
shenbaosheetcell.browse(csjswhsbyje_id).write({'tagname':'csjswhsbyje'})
csjswhsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','6'),('line','=',6)])[1]
shenbaosheetcell.browse(csjswhsbnljje_id).write({'tagname':'csjswhsbnljje'})

zysbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','7'),('line','=',7)])[0]
shenbaosheetcell.browse(zysbyje_id).write({'tagname':'zysbyje'})
zysbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','7'),('line','=',7)])[1]
shenbaosheetcell.browse(zysbnljje_id).write({'tagname':'zysbnljje'})

tdzzsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','8'),('line','=',8)])[0]
shenbaosheetcell.browse(tdzzsbnljje_id).write({'tagname':'tdzzsbnljje'})
tdzzsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','8'),('line','=',8)])[1]
shenbaosheetcell.browse(tdzzsbyje_id).write({'tagname':'tdzzsbyje'})

cztdsysfcsccsyhsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','9'),('line','=',9)])[0]
shenbaosheetcell.browse(cztdsysfcsccsyhsbnljje_id).write({'tagname':'cztdsysfcsccsyhsbnljje'})
cztdsysfcsccsyhsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','9'),('line','=',9)])[1]
shenbaosheetcell.browse(cztdsysfcsccsyhsbyje_id).write({'tagname':'cztdsysfcsccsyhsbyje'})

jyfjkczypwfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','10'),('line','=',10)])[0]
shenbaosheetcell.browse(jyfjkczypwfbyje_id).write({'tagname':'jyfjkczypwfbyje'})
jyfjkczypwfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','10'),('line','=',10)])[1]
shenbaosheetcell.browse(jyfjkczypwfbnljje_id).write({'tagname':'jyfjkczypwfbnljje'})

xsfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','11'),('line','=',11)])[0]
shenbaosheetcell.browse(xsfybyje_id).write({'tagname':'xsfybyje'})
xsfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','11'),('line','=',11)])[1]
shenbaosheetcell.browse(xsfybnljje_id).write({'tagname':'xsfybnljje'})

qzspwxfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','12'),('line','=',12)])[0]
shenbaosheetcell.browse(qzspwxfbnljje_id).write({'tagname':'qzspwxfbnljje'})
qzspwxfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','12'),('line','=',12)])[1]
shenbaosheetcell.browse(qzspwxfbyje_id).write({'tagname':'qzspwxfbyje'})

ggfhywxcfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','13'),('line','=',13)])[0]
shenbaosheetcell.browse(ggfhywxcfbnljje_id).write({'tagname':'ggfhywxcfbnljje'})
ggfhywxcfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','13'),('line','=',13)])[1]
shenbaosheetcell.browse(ggfhywxcfbyje_id).write({'tagname':'ggfhywxcfbyje'})

glfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','14'),('line','=',14)])[0]
shenbaosheetcell.browse(glfybnljje_id).write({'tagname':'glfybnljje'})
glfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','14'),('line','=',14)])[1]
shenbaosheetcell.browse(glfybyje_id).write({'tagname':'glfybyje'})

qzkbfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','15'),('line','=',15)])[0]
shenbaosheetcell.browse(qzkbfbyje_id).write({'tagname':'qzkbfbyje'})
qzkbfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','15'),('line','=',15)])[1]
shenbaosheetcell.browse(qzkbfbnljje_id).write({'tagname':'qzkbfbnljje'})

ywzdfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','16'),('line','=',16)])[0]
shenbaosheetcell.browse(ywzdfbyje_id).write({'tagname':'ywzdfbyje'})
ywzdfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','16'),('line','=',16)])[1]
shenbaosheetcell.browse(ywzdfbnljje_id).write({'tagname':'ywzdfbnljje'})

yjfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','17'),('line','=',17)])[0]
shenbaosheetcell.browse(yjfybnljje_id).write({'tagname':'yjfybnljje'})
yjfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','17'),('line','=',17)])[1]
shenbaosheetcell.browse(yjfybyje_id).write({'tagname':'yjfybyje'})

cwfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','18'),('line','=',18)])[0]
shenbaosheetcell.browse(cwfybyje_id).write({'tagname':'cwfybyje'})
cwfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','18'),('line','=',18)])[1]
shenbaosheetcell.browse(cwfybnljje_id).write({'tagname':'cwfybnljje'})

qzlxfysryhtlbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','19'),('line','=',19)])[0]
shenbaosheetcell.browse(qzlxfysryhtlbyje_id).write({'tagname':'qzlxfysryhtlbyje'})
qzlxfysryhtlbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','19'),('line','=',19)])[1]
shenbaosheetcell.browse(qzlxfysryhtlbnljje_id).write({'tagname':'qzlxfysryhtlbnljje'})

jtzsybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','20'),('line','=',20)])[0]
shenbaosheetcell.browse(jtzsybnljje_id).write({'tagname':'jtzsybnljje'})
jtzsybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','20'),('line','=',20)])[1]
shenbaosheetcell.browse(jtzsybyje_id).write({'tagname':'jtzsybyje'})

eyylrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','21'),('line','=',21)])[0]
shenbaosheetcell.browse(eyylrbnljje_id).write({'tagname':'eyylrbnljje'})
eyylrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','21'),('line','=',21)])[1]
shenbaosheetcell.browse(eyylrbyje_id).write({'tagname':'eyylrbyje'})

jyywsrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','22'),('line','=',22)])[0]
shenbaosheetcell.browse(jyywsrbyje_id).write({'tagname':'jyywsrbyje'})
jyywsrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','22'),('line','=',22)])[1]
shenbaosheetcell.browse(jyywsrbnljje_id).write({'tagname':'jyywsrbnljje'})

qzzfbzbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','23'),('line','=',23)])[0]
shenbaosheetcell.browse(qzzfbzbnljje_id).write({'tagname':'qzzfbzbnljje'})
qzzfbzbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','23'),('line','=',23)])[1]
shenbaosheetcell.browse(qzzfbzbyje_id).write({'tagname':'qzzfbzbyje'})

jyywzcbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','24'),('line','=',24)])[0]
shenbaosheetcell.browse(jyywzcbyje_id).write({'tagname':'jyywzcbyje'})
jyywzcbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','24'),('line','=',24)])[1]
shenbaosheetcell.browse(jyywzcbnljje_id).write({'tagname':'jyywzcbnljje'})

qzhzssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','25'),('line','=',25)])[0]
shenbaosheetcell.browse(qzhzssbnljje_id).write({'tagname':'qzhzssbnljje'})
qzhzssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','25'),('line','=',25)])[1]
shenbaosheetcell.browse(qzhzssbyje_id).write({'tagname':'qzhzssbyje'})

wfshdzqzqtzssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','26'),('line','=',26)])[0]
shenbaosheetcell.browse(wfshdzqzqtzssbnljje_id).write({'tagname':'wfshdzqzqtzssbnljje'})
wfshdzqzqtzssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','26'),('line','=',26)])[1]
shenbaosheetcell.browse(wfshdzqzqtzssbyje_id).write({'tagname':'wfshdzqzqtzssbyje'})

wfshdzqgqtzssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','27'),('line','=',27)])[0]
shenbaosheetcell.browse(wfshdzqgqtzssbyje_id).write({'tagname':'wfshdzqgqtzssbyje'})
wfshdzqgqtzssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','27'),('line','=',27)])[1]
shenbaosheetcell.browse(wfshdzqgqtzssbnljje_id).write({'tagname':'wfshdzqgqtzssbnljje'})

zrzhdbkklyszcdssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','28'),('line','=',28)])[0]
shenbaosheetcell.browse(zrzhdbkklyszcdssbnljje_id).write({'tagname':'zrzhdbkklyszcdssbnljje'})
zrzhdbkklyszcdssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','28'),('line','=',28)])[1]
shenbaosheetcell.browse(zrzhdbkklyszcdssbyje_id).write({'tagname':'zrzhdbkklyszcdssbyje'})

ssznjbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','29'),('line','=',29)])[0]
shenbaosheetcell.browse(ssznjbyje_id).write({'tagname':'ssznjbyje'})
ssznjbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','29'),('line','=',29)])[1]
shenbaosheetcell.browse(ssznjbnljje_id).write({'tagname':'ssznjbnljje'})

slrzebyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','30'),('line','=',30)])[0]
shenbaosheetcell.browse(slrzebyje_id).write({'tagname':'slrzebyje'})
slrzebnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','30'),('line','=',30)])[1]
shenbaosheetcell.browse(slrzebnljje_id).write({'tagname':'slrzebnljje'})

jsdsfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','31'),('line','=',31)])[0]
shenbaosheetcell.browse(jsdsfybnljje_id).write({'tagname':'jsdsfybnljje'})
jsdsfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','31'),('line','=',31)])[1]
shenbaosheetcell.browse(jsdsfybyje_id).write({'tagname':'jsdsfybyje'})

sjlrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','32'),('line','=',32)])[0]
shenbaosheetcell.browse(sjlrbyje_id).write({'tagname':'sjlrbyje'})
sjlrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('line_num','=','32'),('line','=',32)])[1]
shenbaosheetcell.browse(sjlrbnljje_id).write({'tagname':'sjlrbnljje'})

