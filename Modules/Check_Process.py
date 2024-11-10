"""检查 QQNT 的进程"""

from Modules.Logger import logger as logging

import subprocess
def check_process():
    process_list = subprocess.check_output("tasklist", text=True)
    if "QQ.exe" in process_list:
        if "QQ.exe" in process_list:
            logging("[Loader] QQNT（QQ.exe） 正在运行")

        import os
        while True:
            if_kill = input("QQ 正在运行，是否使用本程序将其强制关闭？如果想手动关闭QQ，请在此时手动退出QQ并输入n\n(y/n)\n> ").lower()
            if if_kill == "y" or if_kill == "yes":
                os.system("taskkill /f /im QQ.exe")
                logging("[Loader] 已杀死 QQ.exe")
                break
            if if_kill == "n" or if_kill == "no":
                logging("[Loader] 正在检测手动关闭 QQ 后的 taklist")
                process_list = subprocess.check_output("tasklist", text=True)
                if "QQ.exe" in process_list:
                    logging("[Loader] QQNT 仍然未关闭，要求重新关闭")
                    continue
    elif "QQ.exe" not in process_list:
        logging("[Loader] QQNT 未运行，已跳过进程检测")    