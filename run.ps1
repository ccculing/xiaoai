# 设置执行策略以允许脚本运行（仅对当前会话有效）
Set-ExecutionPolicy Bypass -Scope Process -Force

# 调用Python执行指定的脚本
& python "D:\xiaoai\main.py"