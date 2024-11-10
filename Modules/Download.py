"""下载模块"""

from Modules.Logger import logger as logging
def need_download():
        global unzip_folder
        import requests
        # 调用 GitHub API 获取最新版本信息
        url = "https://api.github.com/repos/LiteLoaderQQNT/LiteLoaderQQNT/releases/latest"
        response = requests.get(url)
        data = response.json()

        # 提取包含 "LiteLoaderQQNT.zip" 的下载链接
        download_url = ""
        for asset in data["assets"]:
            if "LiteLoaderQQNT.zip" in asset["browser_download_url"]:
                download_url = asset["browser_download_url"]
                break

        # 下载
        if download_url:
            import tempfile
            temp_folder = tempfile.gettempdir()
            logging("[System] 系统临时文件夹路径：" + temp_folder)
            with open(temp_folder+"\\LiteLoaderQQNT.zip", "wb") as download:
                print("\n开始下载 LiteLoaderQQNT 压缩包......")
                logging("[Download] 开始下载 LiteLoaderQQNT 压缩包，链接：" + download_url)
                download.write(requests.get(download_url, stream=True).content)
                logging("[Download] 下载完毕")
                print("下载完毕")
        # 解压
        unzip_folder = input("\n请输入存放 LiteLoaderQQNT 的完整路径（包括盘符。文件夹会自动创建。比如输入 C:\\ 后 LiteLoaderQQNT 的路径将为 C:\\LiteLoaderQQNT）\n> ")
        logging("[System] LiteLoaderQQNT 存放路径：" + unzip_folder)
        import zipfile
        try:
            with zipfile.ZipFile(temp_folder+"\\LiteLoaderQQNT.zip", 'r') as zip_ref:
                zip_ref.extractall(unzip_folder+"\\LiteLoaderQQNT")
                logging("[Download] 解压文件 LiteLoaderQQNT.zip 完毕")
                print("解压完毕，路径为",unzip_folder+"\\LiteLoaderQQNT")
        except Exception as e:
            import Modules.Logger
            Modules.Logger.err_logger("[Download] 解压文件 LiteLoaderQQNT.zip 失败，错误信息：" + str(e))
            print("解压失败，错误信息：", str(e))

def download():
    global unzip_folder
    global auto_or_not_auto    
    """检测/询问用户是否使用当前 LiteLoaderQQNT 目录"""

    while True:
        auto_or_not_auto = input("\n是否使用已有的 LiteLoaderQQNT 目录？(y/n)\n> ").lower()
        if auto_or_not_auto == "y" or auto_or_not_auto == "yes":
            unzip_folder = input("\n请输入已有的 LiteLoaderQQNT 的完整路径（比如输入 C:\\LiteLoaderQQNT 后路径将为 C:\\LiteLoaderQQNT）\n> ")
            logging("[System] 已选择使用已有的 LiteLoaderQQNT 目录：" + unzip_folder)
            break
        elif auto_or_not_auto == "n" or auto_or_not_auto == "no":
            logging("[System] 已选择不使用已有的 LiteLoaderQQNT 目录，已跳过检测")
            need_download()
            break
        else:
            continue