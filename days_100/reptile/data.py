# -*- Coding: UTF-8 -*-
# data.py
# @作者 ML_get
# @创建日期 2021-04-26T16:00:54.397Z+08:00
# @最后修改日期 2021-04-26T22:12:42.172Z+08:00
# 软科排名
import requests
from bs4 import BeautifulSoup
import json
import csv


class FindRank:
    def __init__(self, num):
        self.num = num
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/90.0.4430.85'
        }
        pass

    def parse(self, url):
        # 传入url返回一个字典
        try:
            response = requests.get(url, headers=self.headers, timeout=20)
            response.raise_for_status()
            dict_text = json.loads(response.content.decode())
            return dict_text
        except:
            return ''

    def get_data(self, ulist):
        # 提取排名信息
        # 打印表头
        print("{:^10}\t{:^20}\t{:^10}".format('排名', '学校名称', '得分'))
        for i in range(self.num):
            u = ulist[i]
            print("{:^10}\t{:^20}\t{:^10}\
            ".format(u['rankOverall'], u['univNameCn'], u['score']))

    def store_data(self, ulist):
        with open('rank.csv', 'w', newline='') as f:
            w = csv.DictWriter(f, ulist[0].keys())
            w.writeheader()
            w.writerows(ulist)
        print('写入成功')

    def run(self):
        # 实现主要逻辑
        # 1、获取网页信息
        url = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2021'
        dict1 = self.parse(url)
        # 2、提取网页信息存储到数据结构中并展示
        ulist = dict1['data']['rankings']
        self.get_data(ulist)
        # 3.或者存入本地
        self.store_data(ulist)


if __name__ == '__main__':
    rank = FindRank(300)
    rank.run()
