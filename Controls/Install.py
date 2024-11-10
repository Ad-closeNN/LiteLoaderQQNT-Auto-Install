"""安装 LiteLoaderQQNT"""

def IInstall():
    import Modules.Download
    import Modules.Patch
    import Modules.Start

    Modules.Download.download() # 下载 LiteLoaderQQNT 压缩包
    Modules.Patch.patch() # 修补 LiteLoaderQQNT
    Modules.Start.start() # 启动 QQNT
    
    