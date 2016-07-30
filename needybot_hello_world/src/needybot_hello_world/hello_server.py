#!/usr/bin/env python

import rospy

from std_msgs.msg import Empty

from needybot.control.task_server.task_server import TaskServer
from needybot.lib import channels as nb_channels 
from needybot.lib.logger import *

if __name__ == '__main__':
    rospy.init_node('hello_server')
    server = TaskServer(idle_task='say_hello')

    rospy.wait_for_message('/needybot/speech/cache/warmed', Empty, timeout=10)

    loginfo("PLEASE CONNECT IPAD", "*")
    rospy.wait_for_message(nb_channels.Messages.ui_connected.value, Empty, timeout=10)
    loginfo("IPAD CONNECTED", "*")

    server.boot()
    rospy.spin()
