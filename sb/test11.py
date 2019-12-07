

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
#自定义请求头信息
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }

#指定url
url = 'http://yct.sh.gov.cn/portal_yct/'

#proxy
# proxy =  {"http": "192.168.1.230:8888"}
# proxy =  {"http": "127.0.0.1:8888"}

#发起请求
# responseget = requests.get(url=url, headers=headers, proxies=proxy, timeout=40)
responsepost = requests.post(url=url,data='')

