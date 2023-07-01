#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import signal

from wcferry import Wcf

from configuration import Config
from robot import Robot

def main():
    config = Config()
    wcf = Wcf(debug=True)

    def handler(sig, frame):
        wcf.cleanup()  # 退出前清理环境
        exit(0)

    signal.signal(signal.SIGINT, handler)

    robot = Robot(config, wcf)
    robot.LOG.info("正在启动机器人···")

    # 机器人启动发送测试消息
    robot.sendTextMsg("机器人启动成功！", "filehelper")

    # 接收消息
    robot.enableRecvMsg()

    # 让机器人一直跑
    robot.keepRunningAndBlockProcess()


if __name__ == "__main__":
    main()
