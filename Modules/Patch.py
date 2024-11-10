"""去除 Windows 端下QQNT文件校验"""

from Modules.Logger import logger as logging
import os
import sys
import requests
def patch():
    """下载补丁"""

    while True:
        maxbit = sys.maxsize
        if maxbit > 2**32:
            logging("[System] 最大计算值：" + str(maxbit) + "，为 64 位操作系统")
            bit = "64" # 系统位数：64 位
        else:
            logging("[System] 最大计算值：" + str(maxbit) + "，为 32 位操作系统")
            bit = "86" # 系统位数： 32 位
        
        # 调用 GitHub API 获取最新版本信息
        url = "https://api.github.com/repos/LiteLoaderQQNT/QQNTFileVerifyPatch/releases/latest"
        response = requests.get(url)
        data = response.json()

        # 提取包含 "dbghelp_x{bit}.dll" 的下载链接
        download_url = ""
        for asset in data["assets"]:
            if f"dbghelp_x{bit}.dll" in asset["browser_download_url"]:
                download_url = asset["browser_download_url"]
                break
        
        # 提取包含 "dbghelp_x{bit}.dll" 的 dbghelp.dll 文件大小
        github_file_size = ""
        for asset in data["assets"]:
            if f"dbghelp_x{bit}.dll" in asset["browser_download_url"]:
                github_file_size = asset["size"]
                break
        logging("[Download] dbghelp_x" + bit + ".dll 文件大小获取成功：" + str(github_file_size) + " 字节")


        import Modules.Check_QQNT
        logging("[Download] 即将下载 dbghelp_x" + bit +".dll 至 " + Modules.Check_QQNT.qqnt_location + "\\dbghelp.dll")
        with open(Modules.Check_QQNT.qqnt_location+"\\dbghelp.dll", "wb") as download:
            print("\n开始下载补丁......")
            logging("[Download] 开始下载 dbghelp_x" + bit +".dll ，链接：" + download_url)
            download.write(requests.get(download_url, stream=True).content)
            logging("[Download] 下载完毕")
            print("下载完毕")
        
        # 文件校验
        local_file_size = str(os.path.getsize(Modules.Check_QQNT.qqnt_location+"\\dbghelp.dll"))
        if local_file_size == str(github_file_size):
            logging("[Download] 文件校验成功，大小：" + local_file_size + " 字节")
            print("文件校验成功，大小：" + local_file_size + " 字节")
            break
        else:
            import Modules.Logger
            Modules.Logger.err_logger("[Download] 文件校验失败，大小：" + local_file_size + " 字节，远程服务器文件大小：" + str(github_file_size) + " 字节")
            print("文件校验失败，正在重新下载")
    
    """去 QQNT 文件校验"""
    
    if os.path.exists(Modules.Check_QQNT.qqnt_location + "\\versions"):
        logging("[System] versions 目录存在，为新版 QQ")
        version_name = os.listdir(os.path.join(Modules.Check_QQNT.qqnt_location, "versions"))[0] # “版本号” 文件夹名
        logging("[System] versions/版本号 文件夹名称获取成功：" + version_name)
        execute_dir = Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app"
        logging("[Patch] QQNT 补丁执行目录：" + execute_dir)
    
    if not os.path.exists(Modules.Check_QQNT.qqnt_location + "\\versions"):
        logging("[System] QQNT 文件夹下没有 versions 目录，为旧版 QQ")
        print("你的 QQ 可能为旧版 QQ")
        execute_dir = Modules.Check_QQNT.qqnt_location + "\\resources\\app"
        logging("[Patch] QQNT 补丁执行目录：" + execute_dir)
        
    with open(execute_dir + "\\app_launcher\\LiteLoaderQQNT.js", "w", encoding="utf-8") as js:
        import Modules.Download
        if Modules.Download.auto_or_not_auto == "y": # 自己已有的 LiteLoaderQQNT 文件夹
            js.write(f"require(String.raw`{Modules.Download.unzip_folder}`)")
            logging(f"[Patch] 已写入 require(String.raw`{Modules.Download.unzip_folder}`) 到 " + execute_dir + "\\app_launcher\\LiteLoaderQQNT.js")       
        elif Modules.Download.auto_or_not_auto == "n": # 程序自动下载并保存的 LiteLoaderQQNT 文件夹
            js.write(f"require(String.raw`{Modules.Download.unzip_folder}\\LiteLoaderQQNT`)")
            logging(f"[Patch] 已写入 require(String.raw`{Modules.Download.unzip_folder}\\LiteLoaderQQNT`) 到 " + execute_dir + "\\app_launcher\\LiteLoaderQQNT.js")
    
    with open(execute_dir + "\\package.json", "r", encoding="utf-8") as package:
        import json
        package_json = json.load(package)
        package_json["main"] = "./app_launcher/LiteLoaderQQNT.js"
    
    with open(execute_dir + "\\package.json", "w", encoding="utf-8") as new_package:
        json.dump(package_json, new_package, indent=2)
    
    print("补丁成功")
    
    