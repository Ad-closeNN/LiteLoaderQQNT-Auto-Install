"""日志记录器"""

import logging
def logger(info):
    logging.basicConfig(
        filename='Logs/Log.log',  # 指定日志文件名
        filemode='a',        # 追加模式
        format='[%(asctime)s - %(levelname)s] %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO,  # 设置最低记录级别
        encoding="utf-8"
    )
    logging.info(info)

def err_logger(info):
    logging.basicConfig(
        filename='Logs/Log.log',  # 指定日志文件名
        filemode='a',        # 追加模式
        format='[%(asctime)s - %(levelname)s] %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO,  # 设置最低记录级别
        encoding="utf-8"
    )
    logging.error(info)