import requests
from retrying import retry

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46'
}


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data):
    print('*' * 20)
    if method == 'POST':
        r = requests.post(url, data=data, headers=headers)
    else:
        r = requests.get(url, headers=headers, timeout=3)
        assert r.status_code == 200
    return r.content.decode()


def parse_url(url, method='GET', data=None):
    # 异常捕获
    try:
        html_str = _parse_url(url, method, data)
    except:
        html_str = None

    return html_str


#if __name__ == '__main__':
#    url = 'https://www.shanghairanking.cn/api/pub/v1/bcur?bcur_type=11&year=2021'
#    print(parse_url(url))
