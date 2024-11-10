"""卸载 LiteLoaderQQNT 本身及组件"""

def RRemove():
    from Modules.Logger import logger as logging
    import Modules.Check_QQNT
    import os
    
    """检查 LiteLoaderQQNT 需要的文件"""
    if os.path.exists(Modules.Check_QQNT.qqnt_location + "\\versions"):
        logging("[System] versions 目录存在，为新版 QQ")
        version_name = os.listdir(os.path.join(Modules.Check_QQNT.qqnt_location, "versions"))[0] # “版本号” 文件夹名
        logging("[System] versions/版本号 文件夹名称获取成功：" + version_name)
    
    if os.path.exists(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\app_launcher\\LiteLoaderQQNT.js"):
        while True:
            del_LiteLoaderQQNT_js = input("\n是否删除 \\versions\\" + version_name + "\\resources\\app\\app_launcher\\LiteLoaderQQNT.js ？\n[本文件用于引导 LiteLoaderQQNT]\n(y/n)\n> ").lower()
            if del_LiteLoaderQQNT_js == "y" or del_LiteLoaderQQNT_js == "yes":
                try:
                    os.remove(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\app_launcher\\LiteLoaderQQNT.js")
                    logging("[Remove] LiteLoaderQQNT.js 删除成功")
                    print("已删除 LiteLoaderQQNT.js")
                    break
                except Exception as e:
                    import Modules.Logger
                    Modules.Logger.err_logger("[Remove] LiteLoaderQQNT.js 删除失败，错误信息：" + str(e))
                    print("LiteLoaderQQNT.js 删除失败，错误信息：" + str(e))
            elif del_LiteLoaderQQNT_js == "n" or del_LiteLoaderQQNT_js == "no":
                logging("[Remove] LiteLoaderQQNT.js 删除跳过")
                print("已跳过 LiteLoaderQQNT.js 删除")
                break
            else:
                continue
    
    elif not os.path.exists(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\app_launcher\\LiteLoaderQQNT.js"):
        # 没有找到 程序生成的 LiteLoaderQQNT.js
        logging("[Remove] LiteLoaderQQNT.js 不存在")
        del_LiteLoaderQQNT_js = input("\nLiteLoaderQQNT.js 不存在，请手动输入完整的文件地址，不输入即为跳过\n[本文件位于\\app\\app_launcher\\*.js，用于引导 LiteLoaderQQNT]\n> ")
        logging("[Remove] 手动输入的 LiteLoaderQQNT.js 文件地址：" + del_LiteLoaderQQNT_js)
        if del_LiteLoaderQQNT_js != "":
            try:
                os.remove(del_LiteLoaderQQNT_js)
                logging("[Remove] LiteLoaderQQNT.js 删除成功")
                print("已删除 LiteLoaderQQNT.js")
            except Exception as e:
                import Modules.Logger
                Modules.Logger.err_logger("[Remove] LiteLoaderQQNT.js 删除失败，错误信息：" + str(e))
                print("LiteLoaderQQNT.js 删除失败，错误信息：" + str(e))
        elif del_LiteLoaderQQNT_js == "":
            logging("[Remove] LiteLoaderQQNT.js 删除跳过")
            print("已跳过 LiteLoaderQQNT.js 删除")
    
    if os.path.exists(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\package.json"):
        while True:    
            del_package_json = input("\n是否修改 \\versions\\" + version_name + "\\resources\\app\\package.json 至默认内容？\n[本文件用于引导 LiteLoaderQQNT]\n(y/n)\n> ").lower()
            if del_package_json == "y" or del_package_json == "yes":
                import json
                try:
                    with open(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\package.json", "r", encoding="utf-8") as package:
                        package_json = json.load(package)
                        package_json["main"] = "./application.asar/app_launcher/index.js"
                    with open(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\package.json", "w", encoding="utf-8") as new_package:
                        json.dump(package_json, new_package, indent=2)
                    with open(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\package.json", "r", encoding="utf-8") as package:
                        package_json = json.load(package)
                    logging("[Remove] package.json 重置成功，当前的 package.json 内容为：\n" + str(json.dumps(package_json, indent=2)))
                    print("已重置 package.json")
                    break
                except Exception as e:
                    import Modules.Logger
                    Modules.Logger.err_logger("[Remove] package.json 重置失败，错误信息：" + str(e))
            if del_package_json == "n" or del_package_json == "no":
                logging("[Remove] package.json 重置跳过")
                print("已跳过 package.json 重置")
                break
            else:
                continue
    elif not os.path.exists(Modules.Check_QQNT.qqnt_location + "\\versions\\" + version_name + "\\resources\\app\\package.json"):
        import Modules.Logger
        Modules.Logger.err_logger("[Remove] package.json 不存在，跳过重置")
        print("由于找不到 package.json，已跳过 package.json 重置")
    
    """删除 dbghelp.dll"""
    
    if os.path.exists(Modules.Check_QQNT.qqnt_location + "\\dbghelp.dll"):
        while True:
            del_dbghelp = input("\n是否删除 dbghelp.dll？\n[本文件用于绕过 QQNT 的文件完整性校验]\n(y/n)\n> ").lower()
            if del_dbghelp == "y" or del_dbghelp == "yes":
                try:
                    os.remove(Modules.Check_QQNT.qqnt_location + "\\dbghelp.dll")
                    logging("[Remove] dbghelp.dll 删除成功")
                    print("已删除 dbghelp.dll")
                    break
                except Exception as e:
                    import Modules.Logger
                    Modules.Logger.err_logger("[Remove] dbghelp.dll 删除失败，错误信息：" + str(e))
                    print("dbghelp.dll 删除失败，错误信息：" + str(e))
            if del_dbghelp == "n" or del_dbghelp == "no":
                logging("[Remove] dbghelp.dll 删除跳过")
                print("已跳过 dbghelp.dll 删除")
                break
            else:
                continue
    elif not os.path.exists(Modules.Check_QQNT.qqnt_location + "\\dbghelp.dll"):
        import Modules.Logger
        Modules.Logger.err_logger("[Remove] dbghelp.dll 不存在，跳过删除")
        print("由于找不到 dbghelp.dll，已跳过 dbghelp.dll 删除")