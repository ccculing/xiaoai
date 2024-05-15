# 获取当前 PowerShell 脚本所在的目录
$scriptDirectory = $PSScriptRoot

# 构建 Python 脚本的完整路径
$pythonScriptPath = Join-Path -Path $scriptDirectory -ChildPath "main.py"

# 使用 Python 执行该脚本
& python $pythonScriptPath

# 保持 PowerShell 窗口打开，以便查看输出（如果需要）
Read-Host -Prompt "Press Enter to exit"