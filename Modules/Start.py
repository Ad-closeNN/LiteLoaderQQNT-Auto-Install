"""打开 QQ.exe"""

from Modules.Logger import logger as logging
import subprocess
def start():
    import Modules.Check_QQNT
    try:
        subprocess.Popen(r'"' + Modules.Check_QQNT.qqnt_location + '\\QQ.exe"')
        logging("[System] QQ启动成功")
    except Exception as e:
        import Modules.Logger
        Modules.Logger.err_logger("[System] QQ启动失败，错误信息：" + str(e))