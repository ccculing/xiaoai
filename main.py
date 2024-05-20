import json
from DrissionPage import WebPage
from flask import Flask, jsonify, request
from flask_cors import CORS
import pabili
from DrissionPage.common import Keys

# 初始化Flask应用，并启用跨域资源共享CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

# 定义保存搜索结果的json对象
json_results = {"current_index": 0}

def save_json(data, filename='results.json'):
    """将数据保存为json文件。"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_json(filename='results.json'):
    """加载json文件的数据。"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_webpage():
    """获取一个WebPage对象，用于浏览器操作。"""
    page = WebPage()
    page.set.window.full()
    return page
def play_animation(url):
    """播放指定的动画。"""
    full_url = f'http://192.168.2.168:8096/web/index.html#!/details?id={url}&context=tvshows&serverId=49f9428a7b8e400cbd00fdc7703341dc'
    page = get_webpage()
    page.new_tab(full_url)
    page.get_tab(2).close()
    page.get_tab().actions.click(on_ele='tag:button@@class=button-flat btnShuffle detailButton emby-button')

@app.route('/nodered', methods=['GET', 'POST'])
def nodered():
    """处理与Node-RED的交互请求。"""
    action = request.args.get('action')
    keyword = request.args.get('keyword')
    url = request.args.get('url')

    if action == 'current':
        # 处理当前搜索请求
        keyword = keyword[len("搜索"):]
        results = pabili.get_search(keyword, 1)
        json_results["links"] = results
        save_json(json_results)
        data = load_json()
        page = get_webpage()
        page.get(data["links"][data['current_index']])

    elif action in ['next', 'previous']:
        # 处理下一个或上一个搜索结果请求
        data = load_json()
        if action == 'next':
            data['current_index'] += 1
        else:
            data['current_index'] -= 1
        save_json(data)
        page = get_webpage()
        page.get(data["links"][data['current_index']])

    elif action == 'close':
        # 关闭当前标签页并返回到动画列表
        page = get_webpage()
        page.new_tab('http://192.168.2.168:8096/web/index.html#!/tv.html?topParentId=54e2f5a65fcc052ea18327d63079be5a')
        page.get_tab(2).close()

    elif action == 'pause':
        # 暂停播放
        page = get_webpage()
        page.actions.type(Keys.SPACE)

    elif action == 'cartoon' and url:
        play_animation(url)

    return jsonify({"msg": True})

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=5001)
