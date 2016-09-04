#-*- coding=utf-8 -*-


from settings import SERVER, DEBUG
from wechat.robot import wechat_server, debug_shell


if __name__ == "__main__":
    if DEBUG:
        debug_shell()
    else:
        wechat_server(server=SERVER["mode"], port=SERVER["port"])
