"""清理傻逼"""

def pycache_clear():
    import os
    os.system("echo off")
    os.system("""for /d /r %i in (__pycache__) do rd /s /q "%i""")
    os.system("del /q build")
    os.system("del /f /q MainPage.spec")
    os.system("cls")
    os.system("echo on")
pycache_clear()