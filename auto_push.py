import os
import time

# 定义提交和推送的时间间隔（秒）
interval = 60

def has_changes():
    """检查是否有文件更改"""
    result = os.popen('git status --porcelain').read()
    return bool(result.strip())

while True:
    try:
        if has_changes():
            # 添加所有更改
            os.system("git add .")
            # 提交更改
            os.system('git commit -m "Auto commit on change"')
            # 推送更改
            os.system("git push")
            print("Changes committed and pushed.")
        else:
            print("No changes detected.")
    except Exception as e:
        print(f"Error: {e}")
    # 等待指定的时间间隔
    time.sleep(interval)
    