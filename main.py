from DrissionPage import ChromiumPage

page = ChromiumPage()
page.get('http://DrissionPage.cn')




# import json
# from DrissionPage import WebPage
# from flask import Flask, jsonify, redirect, request
# from flask_cors import CORS
# from os import system
# import pabili
# from DrissionPage.common import Actions
# import keyboard
# from pypinyin import lazy_pinyin
# from DrissionPage import ChromiumOptions

# # 创建Flask应用实例
# app = Flask(__name__)
# CORS(app, supports_credentials=True)


# #创建保存搜索结果的json
# json_results = {"current_index":0}

# # 定义路由'/nodered'，接受GET和POST请求
# @app.route('/nodered', methods=['GET', 'POST'])



# def nodered():
#     # 从请求参数中获取关键词
#     action = request.args.get('action')

#     #默认播放第一个
#     if action == 'current':
#         all_keyword = request.args.get('keyword')
#         keyword=all_keyword[len("搜索"):]
#         print(keyword)
#         #搜索结果
#         results = pabili.get_search(keyword, 1)

#         #将搜索结果写入json
#         json_results["links"]=results
#         #写入json
#         with open('results.json', 'w', encoding='utf-8') as f:
#             json.dump(json_results, f, ensure_ascii=False, indent=4)

#         #读取json
#         with open('results.json', 'r', encoding='utf-8') as file:
#             data = json.load(file)

#         #默认播放第一个链接
#         page=WebPage()
#         index=data['current_index']
#         page.get(url:=data["links"][index])
#         ac=Actions(page)

#         #全屏
#         page.set.window.full()

#         # TODO 检查是否有其他标签页，如果有，则关闭
        


#     #播放下一个    
#     elif action == 'next':
#         #读取json
#         with open('results.json', 'r', encoding='utf-8') as file:
#             data = json.load(file)

#         page=WebPage()

#         #修改序列号
#         index=data['current_index']
#         new_index=index+1

#         #更新json
#         data['current_index']=new_index
        
#         #写入json
#         with open('results.json', 'w', encoding='utf-8') as file:
#             json.dump(data, file, ensure_ascii=False, indent=4)

#         #播放
#         page.get(url:=data["links"][new_index])
#         # #全屏
#         page.set.window.full()
        
#         # TODO 检查是否有其他标签页，如果有，则关闭
        

#     #播放上一个
#     elif action == 'previous':
#         #读取json
#         with open('results.json', 'r', encoding='utf-8') as file:
#             data = json.load(file)

#         page=WebPage()

#         #修改序列号
#         index=data['current_index']
#         new_index=index-1

#         #更新json
#         data['current_index']=new_index
        
#         #写入json
#         with open('results.json', 'w', encoding='utf-8') as file:
#             json.dump(data, file, ensure_ascii=False, indent=4)
            
#         #播放
#         page.get(url:=data["links"][new_index])
#         #全屏
#         page.set.window.full()

#         # TODO 检查是否有其他标签页，如果有，则关闭
    

#     #返回主页面
#     elif action == 'close':
#         page=WebPage()
#         page.set.window.full()
#         page.new_tab('http://192.168.2.168:8096/web/index.html#!/tv.html?topParentId=54e2f5a65fcc052ea18327d63079be5a')
#         page.get_tab(2).close()
#         #全屏
        
#         # TODO 检查是否有其他标签页，如果有，则关闭


#     #播放动画
#     elif action == 'cartoon' :

#         # 动画名称与URL的映射关系
#         animation_mapping = {
#             '阿奇': '5ad30182889af6f62c08b46d7b5a78d3',
#             '依娜和恰恰': 'b16f84875d332437a6af1273f8577783',
#             '拉布拉多': '584cf6f1705246bdcd209ab2af5fd68d',
#             '宝宝巴士':'0d7e410ec9d2c890b975a1310d34eff1',
#             '佩奇': 'f48e0db58cd86791adf93793b8b32d84',
#             '布鲁伊': 'a4b857c56110e34967f8055f5d8414f5',
#             '海绵宝宝': 'cdec2cca5b2bcb0e5702c26bbfaa2644',
#             '朵拉': 'ef588852f2ac1de9e3aaedfcdae630c8',
#             '班班和莉莉':'84f29f1a21ce3ead29b1fd5cb4738c0e',
#             '瑞奇宝宝':'be6c2fa10a0dc480a05f005bb5ec3bba',
#             '米奇妙妙屋':'5da89fc8f1ee0da5a4d97214b4fae6a8',
#             '红小豆':'a34fe2c3a0325b6013972299d5b55c15',
#             '宝贝赳赳':'1a9f81fa573cd1693df544c665487bb7',
#             '汪汪队':'c35e6967513714db10d5dfa9d488759d',
#             '天线宝宝':'62cdce820ced050b162dd3fffe7f8ae9',
#         }
#         def is_pinyin_match(target, keyword):
#             """检查target的拼音是否为keyword拼音的子序列"""
#             target_pinyin = lazy_pinyin(target)
#             keyword_pinyin = lazy_pinyin(keyword)
#             # 滑动窗口法检查匹配
#             for i in range(len(keyword_pinyin) - len(target_pinyin) + 1):
#                 if target_pinyin == keyword_pinyin[i:i+len(target_pinyin)]:
#                     return True
#             return False
#         # 根据关键词播放动画
#         def play_animation(animation_name, keyword):
#             animation_id = animation_mapping.get(animation_name)
#             if animation_id:
#                 url = f'http://192.168.2.168:8096/web/index.html#!/details?id={animation_id}&context=tvshows&serverId=49f9428a7b8e400cbd00fdc7703341dc'
#                 page = WebPage()
#                 page.set.window.full()
#                 page.new_tab(url)
#                 page.get_tab(2).close()
#                 page.get_tab().actions.click(on_ele='tag:button@@class=button-flat btnShuffle detailButton emby-button')
#                 #全屏
                
#                 # TODO 检查是否有其他标签页，如果有，则关闭

#         # 播放动画主逻辑
#         keyword = request.args.get('keyword')
#         print(keyword)
#         for animation_name in animation_mapping:
#             print(animation_name)
#             if is_pinyin_match(animation_name, keyword):
#                 play_animation(animation_name, keyword)
#                 break  # 找到第一个匹配项即停止查找


        
#     # 创建响应结果
#     result = {
#         "msg": True,
#     }
#     # 返回JSON格式的响应
#     return jsonify(result)

# # 当脚本直接运行时，启动Flask应用
# if __name__ == "__main__":
#     # 在所有网络接口上运行应用程序，开启调试模式，指定端口为250
#     app.run('0.0.0.0', debug=True, port=5001)



