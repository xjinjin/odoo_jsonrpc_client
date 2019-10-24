import base64

s = '代码'
es = base64.b64encode(s.encode('utf-8')).decode("utf-8")
print(es)  # 5Luj56CB

ds = base64.b64decode(es.encode('utf-8')).decode("utf-8")
print(ds)  # 代码