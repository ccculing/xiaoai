# ��ȡ��ǰ PowerShell �ű����ڵ�Ŀ¼
$scriptDirectory = $PSScriptRoot

# ���� Python �ű�������·��
$pythonScriptPath = Join-Path -Path $scriptDirectory -ChildPath "main.py"

# ʹ�� Python ִ�иýű�
& python $pythonScriptPath

# ���� PowerShell ���ڴ򿪣��Ա�鿴����������Ҫ��
Read-Host -Prompt "Press Enter to exit"