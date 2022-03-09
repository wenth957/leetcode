# -*- Coding: UTF-8 -*-
# kr36.py
# @作者 ML_get
# @创建日期 2021-04-27T21:27:22.073Z+08:00
# @最后修改日期 2021-04-27T21:27:22.073Z+08:00
#

import re
import requests
from parse import parse_url
import json

url = 'https://www.36kr.com'
html_str = parse_url(url)
ret = re.findall(r"<script>window.initialState=(.*?)</script>", html_str)
print(ret)
