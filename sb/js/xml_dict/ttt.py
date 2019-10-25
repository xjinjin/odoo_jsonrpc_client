
import os
# file_name = '印花税纳税申报（报告）表接口(月季报).xml'
file_name = '印花税纳税申报（报告）表接口(月季报)'
file_name_no_extend, extension_name = os.path.splitext(file_name)
print(file_name_no_extend)
print(extension_name)