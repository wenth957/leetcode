# -*- Coding: UTF-8 -*-
# tv.py
# @作者 ML_get
# @创建日期 2021-04-27T22:15:56.609Z+08:00
# @最后修改日期 2021-04-27T22:15:56.609Z+08:00
#
import requests
import json


class DoubanSpider:
    def __init__(self):
        self.url_temp = 'https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?start={}&count=18'
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46'
        }
        pass

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        # 提取数据
        dict_ret = json.loads(json_str)
        content_list = dict_ret['subject_collection_items']
        total = dict_ret['total']
        return content_list, total

    def save_content_list(self, content_list):
        with open('douban.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write('\n')
                # 写入换行符进行换行

    def run(self):
        # 实现主要逻辑
        num = 0
        total = 100  # 假设某个值有第一页
        while num < total + 18:
            # 不能写= 不然会再跑一遍
            # 1 start_url
            start_url = self.url_temp.format(num)
            # 2 请求获取响应
            json_str = self.parse_url(start_url)
            # 3 提取数据
            content_list, total = self.get_content_list(json_str)
            # 4 保存
            self.save_content(content_list)
            # 5 构造下一页url,循环
            # if len(content_list) < 18:
            #    break
            num += 18


if __name__ == '__main__':
    doubantv = DoubanSpider()
    doubantv.run()
