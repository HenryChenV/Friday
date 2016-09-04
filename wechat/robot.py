#-*- coding=utf-8 -*-

import sys
import werobot
from chatter import deepThought

from settings import WECHAT


robot = werobot.WeRoBot(token=WECHAT["token"])


@robot.text
def echo(message):
    default_resp = "哎呦，出错了..."
    resp = None
    try:
        resp = deepThought.get_response(message.content) or default_resp
    except Exception:
        import traceback
        traceback.print_exc()

    return resp


def debug():
    command = {
        "exit": lambda x: sys.exit(),
    }

    while 1:
        message = input(">>>> ")
        if message in command:
            command["message"](message)
        print(deepThought.get_response(message))


wechat_server = robot.run
debug_shell = debug
