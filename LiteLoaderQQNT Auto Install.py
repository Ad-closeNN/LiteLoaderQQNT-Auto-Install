"""主要"""

"""配置日志"""
import os
import sys
if not os.path.exists("Logs"):
    os.makedirs("Logs")
with open("Logs/Log.log", "w", encoding="utf-8") as rewrite:
    rewrite.write("")
from Modules.Logger import logger as logging

import Modules.Load
Modules.Load.load()
logging("[Loader] 加载完毕")

print("欢迎使用 LiteLoaderQQNT 安装器\n")
print("------------")
print("正在检查 QQNT 的位置，请稍后...")
import Modules.Check_QQNT
Modules.Check_QQNT.check_qqnt()
logging("QQNT 文件夹位置获取成功：" + Modules.Check_QQNT.qqnt_location)
os.system("cls")
print("欢迎使用 LiteLoaderQQNT 安装器\n")

while True:
    logging("[Page] 切换至主界面")
    Menu = input("\n请选择执行的操作：\n1. 安装 LiteLoaderQQNT\n2. 卸载 LiteLoaderQQNT\n3. 退出本程序\n> ")
    if Menu == "1":
        logging("[Control] 执行操作：1")
        import Controls.Install
        Controls.Install.IInstall()
        
        logging("[Control] 安装模块执行完毕")
        print("安装完毕") 
    if Menu == "2":
        logging("[Control] 执行操作：2")
        import Controls.Remove
        Controls.Remove.RRemove()
        
        logging("[Control] 卸载模块执行完毕")
        print("卸载完毕")
    if Menu == "3":
        logging("[Control] 收到关闭指令，进程退出")
        sys.exit()
    if Menu == "4":
        print("没有 4！")
    else:
        continue

