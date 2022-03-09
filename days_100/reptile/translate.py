import requests
import json
import sys


class BaiduFanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_detect_url = 'https://fanyi.baidu.com/langdetect'
        self.trans_url = 'https://fanyi.baidu.com/basetrans'
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/90.0.4430.85'
        }
        pass

    def parse_url(self, url, data):
        r = requests.post(url, data=data, headers=self.headers)
        return json.loads(r.content.decode())

    def get_ret(self, dict_response):
        ret = dict_response['trans'][0]['dst']
        print('result is', ret)

    def run(self):
        # 主要实现逻辑
        # 1 获取语言类型
        # 1.1 准备post_url,post_data 1.2 发送post请求1.3 提取语言类型
        lang_detect_data = {'query': self.trans_str}
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)['lan']
        # 2 准备post数据
        trans_data = {
            'query': self.trans_str, 'from': 'zh',
            'to': 'en'} if lang == 'zh' else \
            {'query': self.trans_str, 'from': 'en', 'to': 'zh'}
        # 3 发送请求，获得响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        self.get_ret(dict_response)
        # 4 提取数据


if __name__ == '__main__':
    trans_str = sys.argv[1]
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()
