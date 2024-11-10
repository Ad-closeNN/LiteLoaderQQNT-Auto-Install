"""获取 ../QQNT/ 文件夹路径"""

def check_qqnt():
    global qqnt_location # qqnt_location是..\QQNT\文件夹，root是..\QQNT\文件夹，用 qqnt_location 更好
    import os
    target = "QQ.exe" # 遍历搜索目标
    try:
        drives = ["D:\\Program Files"]
        for drive in drives:
            for root, dirs, files in os.walk(drive):
                if target in files:
                    qqnt_location = root
    except:
        try:
            drives = ["C:\\Program Files"]
            for drive in drives:
                for root, dirs, files in os.walk(drive):
                    if target in files:
                        print("已找到 QQNT 的位置:", os.path.join(root, target))
                        qqnt_location = root
        except:
            try:
                drives = ["D:\\Program Files (x86)"]
                for drive in drives:
                    for root, dirs, files in os.walk(drive):
                        if target in files:
                            print("已找到 QQNT 的位置:", os.path.join(root, target))
                            qqnt_location = root
            except:
                try:
                    drives = ["C:\\Program Files (x86)"]
                    for drive in drives:
                        for root, dirs, files in os.walk(drive):
                            if target in files:
                                print("已找到 QQNT 的位置:", os.path.join(root, target))
                                qqnt_location = root
                                
                except:
                    while True:
                        qqnt_location = input("未找到 QQNT 文件夹的位置，请手动输入\n(如: D:\\Program Files\\Tencent\\QQNT):\n> ")
                        if os.path.exists(qqnt_location):
                            print("已手动设置 QQ.exe 的位置为:", qqnt_location)
                            break
                        else:
                            pass