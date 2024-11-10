"""配置程序准备阶段"""

def logging(msg):
    import datetime
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    with open("Logs/Log.log", "a", encoding="utf-8") as f:
        f.write("[" + time + " - INFO]" + " [Loader] " + msg+ "\n")

def load():
    
    import Modules.Check_Process
    import os
    
    os.system("cls")
    Modules.Check_Process.check_process()
    os.system("cls")