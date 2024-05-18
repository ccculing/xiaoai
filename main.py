import json
from DrissionPage import WebPage, ChromiumOptions
from flask import Flask, jsonify, request
from flask_cors import CORS
from os import system
import pabili
from DrissionPage.common import Actions
from pypinyin import lazy_pinyin

# 初始化Flask应用，并启用跨域资源共享CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

# 定义保存搜索结果的json对象
json_results = {"current_index": 0}

# 定义动画名称与URL映射字典
animation_mapping = {
    '阿奇': '5ad30182889af6f62c08b46d7b5a78d3',
    '依娜和恰恰': 'b16f84875d332437a6af1273f8577783',
    '拉布拉多': '584cf6f1705246bdcd209ab2af5fd68d',
    '宝宝巴士': '0d7e410ec9d2c890b975a1310d34eff1',
    '佩奇': 'f48e0db58cd86791adf93793b8b32d84',
    '布鲁伊': 'a4b857c56110e34967f8055f5d8414f5',
    '海绵宝宝': 'cdec2cca5b2bcb0e5702c26bbfaa2644',
    '朵拉': 'ef588852f2ac1de9e3aaedfcdae630c8',
    '爱探险的朵拉': 'ef588852f2ac1de9e3aaedfcdae630c8',
    '班班和莉莉': '84f29f1a21ce3ead29b1fd5cb4738c0e',
    '瑞奇宝宝': 'be6c2fa10a0dc480a05f005bb5ec3bba',
    '米奇妙妙屋': '5da89fc8f1ee0da5a4d97214b4fae6a8',
    '红小豆': 'a34fe2c3a0325b6013972299d5b55c15',
    '宝贝赳赳': '1a9f81fa573cd1693df544c665487bb7',
    '宝贝JOJO': '1a9f81fa573cd1693df544c665487bb7',
    '汪汪队': 'c35e6967513714db10d5dfa9d488759d',
    '天线宝宝': '62cdce820ced050b162dd3fffe7f8ae9',
    '猫猫做饭':'145eb2fcba2da6c79c9a847e02b74d0f',
    '料理猫王':'145eb2fcba2da6c79c9a847e02b74d0f',
    '小马宝莉':'2e31123bc1e5da5d627d45703c9894e4',
    '托马斯':'528371a35ccef3325ee714cac4029bea',
    '小火车':'528371a35ccef3325ee714cac4029bea',
    '海底小纵队':'8776e841122f2aed008532a45554ad4c',
    '熊出没':'5b7c153988439d424c9b065b9fd395ef',
    '光头强':'5b7c153988439d424c9b065b9fd395ef',
    '超级飞侠':'c3fee2bb08275cc1cf79b88f3ca80862'
}

def save_json(data, filename='results.json'):
    """
    将数据保存为json文件。
    
    :param data: 要保存的数据。
    :param filename: 保存的文件名，默认为'results.json'。
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(filename='results.json'):
    """
    加载json文件的数据。
    
    :param filename: 要加载的文件名，默认为'results.json'。
    :return: 加载的数据。
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_webpage():
    """
    获取一个WebPage对象，用于浏览器操作。
    
    :return: 初始化好的WebPage对象。
    """
    page = WebPage()
    page.set.window.full()
    return page

def is_pinyin_match(target, keyword):
    """
    检查目标字符串是否是关键词的拼音匹配。
    
    :param target: 目标字符串。
    :param keyword: 关键词。
    :return: 如果目标字符串是关键词的拼音前缀，返回True，否则返回False。
    """
    target_pinyin = lazy_pinyin(target)
    keyword_pinyin = lazy_pinyin(keyword)
    for i in range(len(keyword_pinyin) - len(target_pinyin) + 1):
        if target_pinyin == keyword_pinyin[i:i+len(target_pinyin)]:
            return True
    return False

def play_animation(animation_name):
    """
    播放指定的动画。
    
    :param animation_name: 动画名称。
    """
    print(f'播放动画：{animation_name}')
    animation_id = animation_mapping.get(animation_name) 
    if animation_id:
        url = f'http://192.168.2.168:8096/web/index.html#!/details?id={animation_id}&context=tvshows&serverId=49f9428a7b8e400cbd00fdc7703341dc'
        page = get_webpage()
        page.new_tab(url)
        page.get_tab(2).close()
        page.get_tab().actions.click(on_ele='tag:button@@class=button-flat btnShuffle detailButton emby-button')

@app.route('/nodered', methods=['GET', 'POST'])
def nodered():
    """
    处理与Node-RED的交互请求。
    
    :return: 返回处理结果的JSON。
    """
    action = request.args.get('action')

    if action == 'current':
        # 处理当前搜索请求
        keyword = request.args.get('keyword')[len("搜索"):]
        results = pabili.get_search(keyword, 1)
        json_results["links"] = results
        save_json(json_results)
        data = load_json()
        page = get_webpage()
        page.get(url := data["links"][data['current_index']])
        
    elif action in ['next', 'previous']:
        # 处理下一个或上一个搜索结果请求
        data = load_json()
        page = get_webpage()
        if action == 'next':
            data['current_index'] += 1
        else:
            data['current_index'] -= 1
        save_json(data)
        page.get(url := data["links"][data['current_index']])
        
    elif action == 'close':
        # 关闭当前标签页并返回到动画列表
        page = get_webpage()
        page.new_tab('http://192.168.2.168:8096/web/index.html#!/tv.html?topParentId=54e2f5a65fcc052ea18327d63079be5a')
        page.get_tab(2).close()

    elif action == 'cartoon':
        # 根据拼音搜索并播放动画
        keyword = request.args.get('keyword')
        for animation_name in animation_mapping:
            if is_pinyin_match(animation_name, keyword):
                play_animation(animation_name)
                break

    return jsonify({"msg": True})

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=5001)