#-*- coding=utf-8 -*-

import werobot

robot = werobot.WeRobot(token="chatterbotfriday")


def echo(message):
    return "Hello World."


robot.run()
