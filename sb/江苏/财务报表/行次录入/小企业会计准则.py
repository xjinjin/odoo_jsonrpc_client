# -*- coding: utf-8 -*-

from odooClient import  ODOO
c0 = ODOO('http://192.168.1.240:8069')
c0.login('test','admin','admin')

shenbaosheetcell = c0.env['cic_taxsb.shenbaosheet.cell'] # 单元格
shenbaosheet = c0.env['cic_taxsb.shenbaosheet']          # 表
shenbaosheetwizard = c0.env['create.shenbaosheet.wizard']# 创建表

# 资产负债表 行次
xqykjzz_zcfzb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_zcfzb')])[0]

# 短期借款31	货币资金1
dqjkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','dqjkqmye'),('line','=',1)])[0]
shenbaosheetcell.browse(dqjkqmye_id).write({'line_num':'31'})
dqjkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','dqjkncye'),('line','=',1)])[0]
shenbaosheetcell.browse(dqjkncye_id).write({'line_num':'31'})
hbzjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','hbzjncye'),('line','=',1)])[0]
shenbaosheetcell.browse(hbzjncye_id).write({'line_num':'1'})
hbzjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','hbzjqmye'),('line','=',1)])[0]
shenbaosheetcell.browse(hbzjqmye_id).write({'line_num':'1'})

# 应付票据32	短期投资2
yfpjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfpjqmye'),('line','=',2)])[0]
shenbaosheetcell.browse(yfpjqmye_id).write({'line_num':'32'})
yfpjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfpjncye'),('line','=',2)])[0]
shenbaosheetcell.browse(yfpjncye_id).write({'line_num':'32'})
dqtzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','dqtzqmye'),('line','=',2)])[0]
shenbaosheetcell.browse(dqtzqmye_id).write({'line_num':'2'})
dqtzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','dqtzncye'),('line','=',2)])[0]
shenbaosheetcell.browse(dqtzncye_id).write({'line_num':'2'})

# 应收票据3	应付账款33
yspjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yspjqmye'),('line','=',3)])[0]
shenbaosheetcell.browse(yspjqmye_id).write({'line_num':'3'})
yspjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yspjncye'),('line','=',3)])[0]
shenbaosheetcell.browse(yspjncye_id).write({'line_num':'3'})
yfzkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfzkncye'),('line','=',3)])[0]
shenbaosheetcell.browse(yfzkncye_id).write({'line_num':'33'})
yfzkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfzkqmye'),('line','=',3)])[0]
shenbaosheetcell.browse(yfzkqmye_id).write({'line_num':'33'})

# 预收帐款34	应收账款4
ygszkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ygszkqmye'),('line','=',4)])[0]
shenbaosheetcell.browse(ygszkqmye_id).write({'line_num':'4'})
ygszkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ygszkncye'),('line','=',4)])[0]
shenbaosheetcell.browse(ygszkncye_id).write({'line_num':'4'})
yszkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yszkqmye'),('line','=',4)])[0]
shenbaosheetcell.browse(yszkqmye_id).write({'line_num':'34'})
yszkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yszkncye'),('line','=',4)])[0]
shenbaosheetcell.browse(yszkncye_id).write({'line_num':'34'})

# 预付账款5	应付职工薪酬35
yfzkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfzkqmye'),('line','=',5)])[0]
shenbaosheetcell.browse(yfzkqmye_id).write({'line_num':'5'})
yfzkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfzkncye'),('line','=',5)])[0]
shenbaosheetcell.browse(yfzkncye_id).write({'line_num':'5'})
yfzgxcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfzgxcncye'),('line','=',5)])[0]
shenbaosheetcell.browse(yfzgxcncye_id).write({'line_num':'35'})
yfzgxcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yfzgxcqmye'),('line','=',5)])[0]
shenbaosheetcell.browse(yfzgxcqmye_id).write({'line_num':'35'})

# 应收股利6	应交税费36
ysglqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ysglqmye'),('line','=',6)])[0]
shenbaosheetcell.browse(ysglqmye_id).write({'line_num':'6'})
ysglncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ysglncye'),('line','=',6)])[0]
shenbaosheetcell.browse(ysglncye_id).write({'line_num':'6'})
yjsfncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yjsfncye'),('line','=',6)])[0]
shenbaosheetcell.browse(yjsfncye_id).write({'line_num':'36'})
yjsfqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yjsfqmye'),('line','=',6)])[0]
shenbaosheetcell.browse(yjsfqmye_id).write({'line_num':'36'})

# 应付利息7	应收利息37
yflxncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yflxncye'),('line','=',7)])[0]
shenbaosheetcell.browse(yflxncye_id).write({'line_num':'7'})
yflxqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yflxqmye'),('line','=',7)])[0]
shenbaosheetcell.browse(yflxqmye_id).write({'line_num':'7'})
yslxqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yslxqmye'),('line','=',7)])[0]
shenbaosheetcell.browse(yslxqmye_id).write({'line_num':'37'})
yslxncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yslxncye'),('line','=',7)])[0]
shenbaosheetcell.browse(yslxncye_id).write({'line_num':'37'})

# 其他应收款8	应付利润38
qtyskncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtyskncye'),('line','=',8)])[0]
shenbaosheetcell.browse(qtyskncye_id).write({'line_num':'8'})
qtyskqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtyskqmye'),('line','=',8)])[0]
shenbaosheetcell.browse(qtyskqmye_id).write({'line_num':'8'})
yflrncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yflrncye'),('line','=',8)])[0]
shenbaosheetcell.browse(yflrncye_id).write({'line_num':'38'})
yflrqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yflrqmye'),('line','=',8)])[0]
shenbaosheetcell.browse(yflrqmye_id).write({'line_num':'38'})

# 其他应付款39	存货9
chqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','chqmye'),('line','=',9)])[0]
shenbaosheetcell.browse(chqmye_id).write({'line_num':'9'})
chncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','chncye'),('line','=',9)])[0]
shenbaosheetcell.browse(chncye_id).write({'line_num':'9'})
qtyfkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtyfkncye'),('line','=',9)])[0]
shenbaosheetcell.browse(qtyfkncye_id).write({'line_num':'39'})
qtyfkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtyfkqmye'),('line','=',9)])[0]
shenbaosheetcell.browse(qtyfkqmye_id).write({'line_num':'39'})

# 其中：原材料10	其他流动负债40
qzyclncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qzyclncye'),('line','=',10)])[0]
shenbaosheetcell.browse(qzyclncye_id).write({'line_num':'10'})
qzyclqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qzyclqmye'),('line','=',10)])[0]
shenbaosheetcell.browse(qzyclqmye_id).write({'line_num':'10'})
qtldfzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtldfzqmye'),('line','=',10)])[0]
shenbaosheetcell.browse(qtldfzqmye_id).write({'line_num':'40'})
qtldfzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtldfzncye'),('line','=',10)])[0]
shenbaosheetcell.browse(qtldfzncye_id).write({'line_num':'40'})

# 在产品11	流动负债合计41
zcpncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zcpncye'),('line','=',11)])[0]
shenbaosheetcell.browse(zcpncye_id).write({'line_num':'11'})
zcpqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zcpqmye'),('line','=',11)])[0]
shenbaosheetcell.browse(zcpqmye_id).write({'line_num':'11'})
ldfzhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ldfzhjqmye'),('line','=',11)])[0]
shenbaosheetcell.browse(ldfzhjqmye_id).write({'line_num':'41'})
ldfzhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ldfzhjncye'),('line','=',11)])[0]
shenbaosheetcell.browse(ldfzhjncye_id).write({'line_num':'41'})

# 库存材料12	非流动负债
kcclncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','kcclncye'),('line','=',12)])[0]
shenbaosheetcell.browse(kcclncye_id).write({'line_num':'12'})
kcclqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','kcclqmye'),('line','=',12)])[0]
shenbaosheetcell.browse(kcclqmye_id).write({'line_num':'12'})

# 周转材料13	长期借款42
zzclqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zzclqmye'),('line','=',13)])[0]
shenbaosheetcell.browse(zzclqmye_id).write({'line_num':'13'})
zzclncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zzclncye'),('line','=',13)])[0]
shenbaosheetcell.browse(zzclncye_id).write({'line_num':'13'})
zqjkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqjkqmye'),('line','=',13)])[0]
shenbaosheetcell.browse(zqjkqmye_id).write({'line_num':'42'})
zqjkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqjkncye'),('line','=',13)])[0]
shenbaosheetcell.browse(zqjkncye_id).write({'line_num':'42'})

# 其他流动资产14	长期应付款43
qtldzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtldzcqmye'),('line','=',14)])[0]
shenbaosheetcell.browse(qtldzcqmye_id).write({'line_num':'14'})
qtldzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtldzcncye'),('line','=',14)])[0]
shenbaosheetcell.browse(qtldzcncye_id).write({'line_num':'14'})
zqyfkncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqyfkncye'),('line','=',14)])[0]
shenbaosheetcell.browse(zqyfkncye_id).write({'line_num':'43'})
zqyfkqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqyfkqmye'),('line','=',14)])[0]
shenbaosheetcell.browse(zqyfkqmye_id).write({'line_num':'43'})

# 流动资产合计15	递延收益44
ldzchjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ldzchjqmye'),('line','=',15)])[0]
shenbaosheetcell.browse(ldzchjqmye_id).write({'line_num':'15'})
ldzchjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','ldzchjncye'),('line','=',15)])[0]
shenbaosheetcell.browse(ldzchjncye_id).write({'line_num':'15'})
dysyqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','dysyqmye'),('line','=',15)])[0]
shenbaosheetcell.browse(dysyqmye_id).write({'line_num':'44'})
dysyncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','dysyncye'),('line','=',15)])[0]
shenbaosheetcell.browse(dysyncye_id).write({'line_num':'44'})

# 非流动资产	其他非流动负债45
qtfldfzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtfldfzncye'),('line','=',16)])[0]
shenbaosheetcell.browse(qtfldfzncye_id).write({'line_num':'45'})
qtfldfzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtfldfzqmye'),('line','=',16)])[0]
shenbaosheetcell.browse(qtfldfzqmye_id).write({'line_num':'45'})

# 长期债券投资16	非流动负债合计46
zqzqtzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqzqtzncye'),('line','=',17)])[0]
shenbaosheetcell.browse(zqzqtzncye_id).write({'line_num':'16'})
zqzqtzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqzqtzqmye'),('line','=',17)])[0]
shenbaosheetcell.browse(zqzqtzqmye_id).write({'line_num':'16'})
fldfzhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fldfzhjncye'),('line','=',17)])[0]
shenbaosheetcell.browse(fldfzhjncye_id).write({'line_num':'46'})
fldfzhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fldfzhjqmye'),('line','=',17)])[0]
shenbaosheetcell.browse(fldfzhjqmye_id).write({'line_num':'46'})

# 长期股权投资17	负债合计47
zqgqtzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqgqtzqmye'),('line','=',18)])[0]
shenbaosheetcell.browse(zqgqtzqmye_id).write({'line_num':'17'})
zqgqtzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqgqtzncye'),('line','=',18)])[0]
shenbaosheetcell.browse(zqgqtzncye_id).write({'line_num':'17'})
fzhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fzhjncye'),('line','=',18)])[0]
shenbaosheetcell.browse(fzhjncye_id).write({'line_num':'47'})
fzhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fzhjqmye'),('line','=',18)])[0]
shenbaosheetcell.browse(fzhjqmye_id).write({'line_num':'47'})

# 固定资产原价18
gdzcyjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gdzcyjncye'),('line','=',19)])[0]
shenbaosheetcell.browse(gdzcyjncye_id).write({'line_num':'18'})
gdzcyjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gdzcyjqmye'),('line','=',19)])[0]
shenbaosheetcell.browse(gdzcyjqmye_id).write({'line_num':'18'})

# 减：累计折旧19
jljzjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','jljzjncye'),('line','=',20)])[0]
shenbaosheetcell.browse(jljzjncye_id).write({'line_num':'19'})
jljzjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','jljzjqmye'),('line','=',20)])[0]
shenbaosheetcell.browse(jljzjqmye_id).write({'line_num':'19'})

# 固定资产账面价值20
gdzczmjzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gdzczmjzncye'),('line','=',21)])[0]
shenbaosheetcell.browse(gdzczmjzncye_id).write({'line_num':'20'})
gdzczmjzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gdzczmjzqmye'),('line','=',21)])[0]
shenbaosheetcell.browse(gdzczmjzqmye_id).write({'line_num':'20'})

# 在建工程21
zjgcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zjgcncye'),('line','=',22)])[0]
shenbaosheetcell.browse(zjgcncye_id).write({'line_num':'21'})
zjgcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zjgcqmye'),('line','=',22)])[0]
shenbaosheetcell.browse(zjgcqmye_id).write({'line_num':'21'})

# 工程物资22
gcwzncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gcwzncye'),('line','=',23)])[0]
shenbaosheetcell.browse(gcwzncye_id).write({'line_num':'22'})
gcwzqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gcwzqmye'),('line','=',23)])[0]
shenbaosheetcell.browse(gcwzqmye_id).write({'line_num':'22'})

# 固定资产清理23
gdzcqlqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gdzcqlqmye'),('line','=',24)])[0]
shenbaosheetcell.browse(gdzcqlqmye_id).write({'line_num':'23'})
gdzcqlncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','gdzcqlncye'),('line','=',24)])[0]
shenbaosheetcell.browse(gdzcqlncye_id).write({'line_num':'23'})

# 生产性生物资产24	所有者权益（或股东权益）
scxswzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','scxswzcncye'),('line','=',25)])[0]
shenbaosheetcell.browse(scxswzcncye_id).write({'line_num':'24'})
scxswzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','scxswzcqmye'),('line','=',25)])[0]
shenbaosheetcell.browse(scxswzcqmye_id).write({'line_num':'24'})

# 无形资产25	实收资本（或股本）48
wxzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','wxzcqmye'),('line','=',26)])[0]
shenbaosheetcell.browse(wxzcqmye_id).write({'line_num':'25'})
wxzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','wxzcncye'),('line','=',26)])[0]
shenbaosheetcell.browse(wxzcncye_id).write({'line_num':'25'})
sszbhgbqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','sszbhgbqmye'),('line','=',26)])[0]
shenbaosheetcell.browse(sszbhgbqmye_id).write({'line_num':'48'})
sszbhgbncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','sszbhgbncye'),('line','=',26)])[0]
shenbaosheetcell.browse(sszbhgbncye_id).write({'line_num':'48'})

# 开发支出26	资本公积49
kfzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','kfzcncye'),('line','=',27)])[0]
shenbaosheetcell.browse(kfzcncye_id).write({'line_num':'26'})
kfzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','kfzcqmye'),('line','=',27)])[0]
shenbaosheetcell.browse(kfzcqmye_id).write({'line_num':'26'})
zbgjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zbgjqmye'),('line','=',27)])[0]
shenbaosheetcell.browse(zbgjqmye_id).write({'line_num':'49'})
zbgjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zbgjncye'),('line','=',27)])[0]
shenbaosheetcell.browse(zbgjncye_id).write({'line_num':'49'})

# 长期待摊费用27	盈余公积50
zqdtfyqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqdtfyqmye'),('line','=',28)])[0]
shenbaosheetcell.browse(zqdtfyqmye_id).write({'line_num':'27'})
zqdtfyncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zqdtfyncye'),('line','=',28)])[0]
shenbaosheetcell.browse(zqdtfyncye_id).write({'line_num':'27'})
yygjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yygjqmye'),('line','=',28)])[0]
shenbaosheetcell.browse(yygjqmye_id).write({'line_num':'50'})
yygjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','yygjncye'),('line','=',28)])[0]
shenbaosheetcell.browse(yygjncye_id).write({'line_num':'50'})

# 其他非流动资产28	未分配利润51
qtfldzcncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtfldzcncye'),('line','=',29)])[0]
shenbaosheetcell.browse(qtfldzcncye_id).write({'line_num':'28'})
qtfldzcqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','qtfldzcqmye'),('line','=',29)])[0]
shenbaosheetcell.browse(qtfldzcqmye_id).write({'line_num':'28'})
wfplrncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','wfplrncye'),('line','=',29)])[0]
shenbaosheetcell.browse(wfplrncye_id).write({'line_num':'51'})
wfplrqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','wfplrqmye'),('line','=',29)])[0]
shenbaosheetcell.browse(wfplrqmye_id).write({'line_num':'51'})

# 非流动资产合计29	所有者权益（或股东权益）合计52
fldzchjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fldzchjncye'),('line','=',30)])[0]
shenbaosheetcell.browse(fldzchjncye_id).write({'line_num':'29'})
fldzchjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fldzchjqmye'),('line','=',30)])[0]
shenbaosheetcell.browse(fldzchjqmye_id).write({'line_num':'29'})
syzqyhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','syzqyhjncye'),('line','=',30)])[0]
shenbaosheetcell.browse(syzqyhjncye_id).write({'line_num':'52'})
syzqyhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','syzqyhjqmye'),('line','=',30)])[0]
shenbaosheetcell.browse(syzqyhjqmye_id).write({'line_num':'52'})

# 资产合计30	负债和所有者权益（或股东权益）总计53
zchjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zchjncye'),('line','=',31)])[0]
shenbaosheetcell.browse(zchjncye_id).write({'line_num':'30'})
zchjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','zchjqmye'),('line','=',31)])[0]
shenbaosheetcell.browse(zchjqmye_id).write({'line_num':'30'})
fzhsyzqyhjqmye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fzhsyzqyhjqmye'),('line','=',31)])[0]
shenbaosheetcell.browse(fzhsyzqyhjqmye_id).write({'line_num':'53'})
fzhsyzqyhjncye_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_zcfzb_id),('tagname','=','fzhsyzqyhjncye'),('line','=',31)])[0]
shenbaosheetcell.browse(fzhsyzqyhjncye_id).write({'line_num':'53'})


# 利润表 行次
xqykjzz_lrb_id = shenbaosheet.search([('tagname','=','jsxgs_cwbb_xqykjzz_lrb')])[0]

yyysrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yyysrbnljje'),('line','=',1)])[0]
shenbaosheetcell.browse(yyysrbnljje_id).write({'line_num':'1'})
yyysrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yyysrbyje'),('line','=',1)])[0]
shenbaosheetcell.browse(yyysrbyje_id).write({'line_num':'1'})

jyycbbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyycbbnljje'),('line','=',2)])[0]
shenbaosheetcell.browse(jyycbbnljje_id).write({'line_num':'2'})
jyycbbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyycbbyje'),('line','=',2)])[0]
shenbaosheetcell.browse(jyycbbyje_id).write({'line_num':'2'})

yysjjfjbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yysjjfjbnljje'),('line','=',3)])[0]
shenbaosheetcell.browse(yysjjfjbnljje_id).write({'line_num':'3'})
yysjjfjbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yysjjfjbyje'),('line','=',3)])[0]
shenbaosheetcell.browse(yysjjfjbyje_id).write({'line_num':'3'})

qzxfsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzxfsbyje'),('line','=',4)])[0]
shenbaosheetcell.browse(qzxfsbyje_id).write({'line_num':'4'})
qzxfsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzxfsbnljje'),('line','=',4)])[0]
shenbaosheetcell.browse(qzxfsbnljje_id).write({'line_num':'4'})

yysbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yysbnljje'),('line','=',5)])[0]
shenbaosheetcell.browse(yysbnljje_id).write({'line_num':'5'})
yysbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yysbyje'),('line','=',5)])[0]
shenbaosheetcell.browse(yysbyje_id).write({'line_num':'5'})

csjswhsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','csjswhsbyje'),('line','=',6)])[0]
shenbaosheetcell.browse(csjswhsbyje_id).write({'line_num':'6'})
csjswhsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','csjswhsbnljje'),('line','=',6)])[0]
shenbaosheetcell.browse(csjswhsbnljje_id).write({'line_num':'6'})

zysbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','zysbyje'),('line','=',7)])[0]
shenbaosheetcell.browse(zysbyje_id).write({'line_num':'7'})
zysbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','zysbnljje'),('line','=',7)])[0]
shenbaosheetcell.browse(zysbnljje_id).write({'line_num':'7'})

tdzzsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','tdzzsbnljje'),('line','=',8)])[0]
shenbaosheetcell.browse(tdzzsbnljje_id).write({'line_num':'8'})
tdzzsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','tdzzsbyje'),('line','=',8)])[0]
shenbaosheetcell.browse(tdzzsbyje_id).write({'line_num':'8'})

cztdsysfcsccsyhsbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','cztdsysfcsccsyhsbnljje'),('line','=',9)])[0]
shenbaosheetcell.browse(cztdsysfcsccsyhsbnljje_id).write({'line_num':'9'})
cztdsysfcsccsyhsbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','cztdsysfcsccsyhsbyje'),('line','=',9)])[0]
shenbaosheetcell.browse(cztdsysfcsccsyhsbyje_id).write({'line_num':'9'})

jyfjkczypwfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyfjkczypwfbyje'),('line','=',10)])[0]
shenbaosheetcell.browse(jyfjkczypwfbyje_id).write({'line_num':'10'})
jyfjkczypwfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyfjkczypwfbnljje'),('line','=',10)])[0]
shenbaosheetcell.browse(jyfjkczypwfbnljje_id).write({'line_num':'10'})

xsfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','xsfybyje'),('line','=',11)])[0]
shenbaosheetcell.browse(xsfybyje_id).write({'line_num':'11'})
xsfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','xsfybnljje'),('line','=',11)])[0]
shenbaosheetcell.browse(xsfybnljje_id).write({'line_num':'11'})

qzspwxfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzspwxfbnljje'),('line','=',12)])[0]
shenbaosheetcell.browse(qzspwxfbnljje_id).write({'line_num':'12'})
qzspwxfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzspwxfbyje'),('line','=',12)])[0]
shenbaosheetcell.browse(qzspwxfbyje_id).write({'line_num':'12'})

ggfhywxcfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','ggfhywxcfbnljje'),('line','=',13)])[0]
shenbaosheetcell.browse(ggfhywxcfbnljje_id).write({'line_num':'13'})
ggfhywxcfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','ggfhywxcfbyje'),('line','=',13)])[0]
shenbaosheetcell.browse(ggfhywxcfbyje_id).write({'line_num':'13'})

glfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','glfybnljje'),('line','=',14)])[0]
shenbaosheetcell.browse(glfybnljje_id).write({'line_num':'14'})
glfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','glfybyje'),('line','=',14)])[0]
shenbaosheetcell.browse(glfybyje_id).write({'line_num':'14'})

qzkbfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzkbfbyje'),('line','=',15)])[0]
shenbaosheetcell.browse(qzkbfbyje_id).write({'line_num':'15'})
qzkbfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzkbfbnljje'),('line','=',15)])[0]
shenbaosheetcell.browse(qzkbfbnljje_id).write({'line_num':'15'})

ywzdfbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','ywzdfbyje'),('line','=',16)])[0]
shenbaosheetcell.browse(ywzdfbyje_id).write({'line_num':'16'})
ywzdfbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','ywzdfbnljje'),('line','=',16)])[0]
shenbaosheetcell.browse(ywzdfbnljje_id).write({'line_num':'16'})

yjfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yjfybnljje'),('line','=',17)])[0]
shenbaosheetcell.browse(yjfybnljje_id).write({'line_num':'17'})
yjfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','yjfybyje'),('line','=',17)])[0]
shenbaosheetcell.browse(yjfybyje_id).write({'line_num':'17'})

cwfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','cwfybyje'),('line','=',18)])[0]
shenbaosheetcell.browse(cwfybyje_id).write({'line_num':'18'})
cwfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','cwfybnljje'),('line','=',18)])[0]
shenbaosheetcell.browse(cwfybnljje_id).write({'line_num':'18'})

qzlxfysryhtlbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzlxfysryhtlbyje'),('line','=',19)])[0]
shenbaosheetcell.browse(qzlxfysryhtlbyje_id).write({'line_num':'19'})
qzlxfysryhtlbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzlxfysryhtlbnljje'),('line','=',19)])[0]
shenbaosheetcell.browse(qzlxfysryhtlbnljje_id).write({'line_num':'19'})

jtzsybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jtzsybnljje'),('line','=',20)])[0]
shenbaosheetcell.browse(jtzsybnljje_id).write({'line_num':'20'})
jtzsybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jtzsybyje'),('line','=',20)])[0]
shenbaosheetcell.browse(jtzsybyje_id).write({'line_num':'20'})

eyylrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','eyylrbnljje'),('line','=',21)])[0]
shenbaosheetcell.browse(eyylrbnljje_id).write({'line_num':'21'})
eyylrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','eyylrbyje'),('line','=',21)])[0]
shenbaosheetcell.browse(eyylrbyje_id).write({'line_num':'21'})

jyywsrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyywsrbyje'),('line','=',22)])[0]
shenbaosheetcell.browse(jyywsrbyje_id).write({'line_num':'22'})
jyywsrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyywsrbnljje'),('line','=',22)])[0]
shenbaosheetcell.browse(jyywsrbnljje_id).write({'line_num':'22'})

qzzfbzbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzzfbzbnljje'),('line','=',23)])[0]
shenbaosheetcell.browse(qzzfbzbnljje_id).write({'line_num':'23'})
qzzfbzbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzzfbzbyje'),('line','=',23)])[0]
shenbaosheetcell.browse(qzzfbzbyje_id).write({'line_num':'23'})

jyywzcbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyywzcbyje'),('line','=',24)])[0]
shenbaosheetcell.browse(jyywzcbyje_id).write({'line_num':'24'})
jyywzcbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jyywzcbnljje'),('line','=',24)])[0]
shenbaosheetcell.browse(jyywzcbnljje_id).write({'line_num':'24'})

qzhzssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzhzssbnljje'),('line','=',25)])[0]
shenbaosheetcell.browse(qzhzssbnljje_id).write({'line_num':'25'})
qzhzssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','qzhzssbyje'),('line','=',25)])[0]
shenbaosheetcell.browse(qzhzssbyje_id).write({'line_num':'25'})

wfshdzqzqtzssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','wfshdzqzqtzssbnljje'),('line','=',26)])[0]
shenbaosheetcell.browse(wfshdzqzqtzssbnljje_id).write({'line_num':'26'})
wfshdzqzqtzssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','wfshdzqzqtzssbyje'),('line','=',26)])[0]
shenbaosheetcell.browse(wfshdzqzqtzssbyje_id).write({'line_num':'26'})

wfshdzqgqtzssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','wfshdzqgqtzssbyje'),('line','=',27)])[0]
shenbaosheetcell.browse(wfshdzqgqtzssbyje_id).write({'line_num':'27'})
wfshdzqgqtzssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','wfshdzqgqtzssbnljje'),('line','=',27)])[0]
shenbaosheetcell.browse(wfshdzqgqtzssbnljje_id).write({'line_num':'27'})

zrzhdbkklyszcdssbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','zrzhdbkklyszcdssbnljje'),('line','=',28)])[0]
shenbaosheetcell.browse(zrzhdbkklyszcdssbnljje_id).write({'line_num':'28'})
zrzhdbkklyszcdssbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','zrzhdbkklyszcdssbyje'),('line','=',28)])[0]
shenbaosheetcell.browse(zrzhdbkklyszcdssbyje_id).write({'line_num':'28'})

ssznjbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','ssznjbyje'),('line','=',29)])[0]
shenbaosheetcell.browse(ssznjbyje_id).write({'line_num':'29'})
ssznjbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','ssznjbnljje'),('line','=',29)])[0]
shenbaosheetcell.browse(ssznjbnljje_id).write({'line_num':'29'})

slrzebyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','slrzebyje'),('line','=',30)])[0]
shenbaosheetcell.browse(slrzebyje_id).write({'line_num':'30'})
slrzebnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','slrzebnljje'),('line','=',30)])[0]
shenbaosheetcell.browse(slrzebnljje_id).write({'line_num':'30'})

jsdsfybnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jsdsfybnljje'),('line','=',31)])[0]
shenbaosheetcell.browse(jsdsfybnljje_id).write({'line_num':'31'})
jsdsfybyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','jsdsfybyje'),('line','=',31)])[0]
shenbaosheetcell.browse(jsdsfybyje_id).write({'line_num':'31'})

sjlrbyje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','sjlrbyje'),('line','=',32)])[0]
shenbaosheetcell.browse(sjlrbyje_id).write({'line_num':'32'})
sjlrbnljje_id = shenbaosheetcell.search([('sheet_id','=',xqykjzz_lrb_id),('tagname','=','sjlrbnljje'),('line','=',32)])[0]
shenbaosheetcell.browse(sjlrbnljje_id).write({'line_num':'32'})

