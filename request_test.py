#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 0027 16:48
# @Author  : Zhang YP
# @Email   : 1579922399@qq.com
# @github  :  Aaron Ramsey
# @File    : request_test.py

import json, requests

from datetime import datetime

"""
    一次只能查询一个字段:station,sku,erpsku,asin
    一个属性查询多个用逗号(英文)连接。其中查询站点字段个数不得超过4个,查询erpsku,sku,asin不得超过1000
"""

startTime = datetime.now()
url = "http://172.16.128.240:8000/query_kws"
token = "468a998a670b1ed7695cd0f5ac3850db"
# 查询单个示例
# params = {'token':token,'station': 'kimiss_uk'}
params = {'token':token,'erpsku':'JM02869-07'}
# 查询多个示例
# params = {'token':token,'asin': 'B07Y27RCZS,B07Y3ZM2PT,B07P6NXF5H'}
# params = {'token':token,'sku': 'GS15336-FZH-DGACsw-XIJ,201822620-01/120932hhh'}
# 本地上传的文件路径
request = requests.get(url=url, params=params,timeout=(3,7))
response = request.content
responseInfo = json.loads(response)
if 'data' not in responseInfo:
    print(responseInfo)
responseData = json.loads(response)['data']
print(responseData)
print(f'上传上传文件花费:{(datetime.now()-startTime).total_seconds()}秒.')
