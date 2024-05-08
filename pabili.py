import requests  # 发送请求

# 请求头和请求参数定义为常量以及单独的函数，以提高代码的可维护性
HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # 将cookie处理逻辑移至函数内部，避免硬编码
    'cookie': '',
    'origin': 'https://search.bilibili.com',
    'referer': 'https://search.bilibili.com/all?keyword={}&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=24',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

def build_params(page, keyword):
    """
    构建请求参数字典。

    :param page: 请求的页码
    :param keyword: 搜索关键词
    :return: 请求参数字典
    """
    return {
        "category_id": "",
        "search_type": "video",
        "ad_resource": "5654",
        "__refresh__": 'true',
        "_extra": "",
        "context": "",
        "page": page,
        "page_size": 30,
        "from_source": "",
        "from_spmid": "333.337",
        "platform": "pc",
        "highlight": 1,
        "single_column": 0,
        "keyword": keyword,
        "qv_id": "TNww4PCwCehEud96L4zhhVdObPolUUdL",
        "source_tag": 3,
        "gaia_vtoken": "",
        "dynamic_offset": 72,
        "web_location": 1430654,
        "w_rid": "85c6fa25e89d395d7beda67ccaafbd32",
        "wts": 1714677986
    }

def get_cookie():
    """
    获取cookie的逻辑实现，应返回cookie字符串。

    :return: cookie字符串
    """
    return "_uuid=108C45154-5B3C-DAC8-CF10C-3CA667343EFB32523infoc; buvid3=38CEFC71-60DC-E967-BD58-01582F5ABEED35062infoc; b_nut=1713377035; buvid4=2B1CE582-8FB4-D561-5EA4-F227986DCED735062-024041718-iDPXKBSsl3aBRE6S9A5v5iCjMNhw0%2Bzon1%2BUOJevaMJSuDZRPXOEH9hKSups5aAG; rpdid=0zbfvSf8WZ|mBrns9FH|35M|3w1RX9DH; SESSDATA=da6e122d%2C1728929105%2C6ee15%2A41CjAWL92LHU5ojaJaNRlz6DGRn0TRLF2TO7Zy7j1XfIYwO6TOgIIy86bvZNTwUWyYPhISVm1VU3NlYjRkMHllbW16QXF1T0R5X0JjNTRoSWNOUmFVeU45cWxOZlBCMU5QMUszWlpUalIxdlUtOERKMXl3VUEwWmY4a3Y1aTBCQ0RjWXlBdmoxOFpnIIEC; bili_jct=9f8a374ce3b3a6de5eb5231ec6422b89; DedeUserID=483321254; DedeUserID__ckMd5=7965ec0572c356aa; enable_web_push=DISABLE; FEED_LIVE_VERSION=V_HEADER_LIVE_NO_POP; header_theme_version=CLOSE; buvid_fp_plain=undefined; fingerprint=11ee264b042f6a071807aaba66c702f2; buvid_fp=11ee264b042f6a071807aaba66c702f2; bp_video_offset_483321254=925045761297612872; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; PVID=1; CURRENT_QUALITY=80; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQ4OTA5NDIsImlhdCI6MTcxNDYzMTY4MiwicGx0IjotMX0.m5TM6f7u_zoA6zh413wbcGpey5ZSFYzWQEecNt0GESg; bili_ticket_expires=1714890882; sid=620upubf; home_feed_column=5; browser_resolution=1836-958; bp_t_offset_483321254=926994392206540808; b_lsid=693EB497_18F3AB0B029"

def get_search(keyword, max_page):
    """
    爬取B站搜索结果页面的视频地址。

    :param keyword: 搜索关键词
    :param max_page: 最大爬取页数
    """
    headers = HEADERS.copy()
    headers['cookie'] = get_cookie()
    # video_urls = []  # 用于存储所有视频地址
    for page in range(1, max_page + 1):
        print(f'开始爬取第{page}页')
        url = 'https://api.bilibili.com/x/web-interface/search/type'
        params = build_params(page, keyword)
        
        try:
            r = requests.get(url, headers=headers, params=params)
            r.raise_for_status()  # 检查HTTP响应状态
            j_data = r.json()
            data_list = j_data['data']['result']
            print(f'数据长度：{len(data_list)}')
            arcurl_list = [data['arcurl'] for data in data_list if 'arcurl' in data]
            # video_urls.extend(arcurl_list)
            # # 打印视频地址
            # for arcurl in arcurl_list:
            #     print(f'视频地址: {arcurl} ')
        except requests.RequestException as e:
            print(f'请求错误: {e}')
        except KeyError:
            print(f'数据解析错误: 缺失关键字段')
    return arcurl_list 

#使用示例
# if __name__ == '__main__':
#     search_keyword = '三只老虎'
#     max_page = 1
#     get_search(search_keyword, max_page)