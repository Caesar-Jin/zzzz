#!/usr/bin/env python
# -*- coding: utf-8 -*-
#提交出错le吗
import requests
url="http://www.bluecore.com.cn"
r=requests.get(url)
print(r.text)

