#!/usr/bin/env python

import actionlib
import rospy

from std_msgs.msg import Empty

from needybot.control.task_server.base import Task, TaskStep

from needybot.lib.logger import *
from needybot_msgs.msg import SpeechAction, \
     SpeechFeedback, SpeechResult, SpeechGoal 

class SayHello(Task):

    def __init__(self):
        super(SayHello, self).__init__('say_hello')
        self.add_steps([
            TaskStep(
                'load',
                entered_handler=self.load_entered,
                instructions={
                    'view': 'eye',
                    'type': 'happy'
                }
            ),
            TaskStep(
                'ask',
                entered_handler=self.ask_entered,
                failure_step='sad',
                success_step='happy',
                instructions={
                    'view': 'ui',
                    'type': 'confirm',
                    'data': {
                        'title': 'Do you like robots?',
                        'subtitle': '(please say yes)'
                    }
                }
            ),
            TaskStep(
                'excited',
                entered_handler=self.excited_entered,
                instructions={
                    'view': 'eye',
                    'type': 'happy'
                }
            ),
            TaskStep(
                'sad',
                entered_handler=self.sad_entered,
                instructions={
                    'view': 'eye',
                    'type': 'sad'
                }
            )
        ])

        self.client = actionlib.SimpleActionClient('needybot_speech', SpeechAction)
        self.client.wait_for_server()

    def load_entered(self, step):
        super(SayHello, self).load_entered(step)

        goal = SpeechGoal(key="hello")
        self.client.send_goal(goal)
        self.client.wait_for_result()

        rospy.sleep(1.0)
        self.serve_step('ask')

    def ask_entered(self, step):
        goal = SpeechGoal(key="ask_like_robots")
        self.client.send_goal(goal)
        self.client.wait_for_result()
        self.instruct()

    def excited_entered(self, step):
        self.instruct()
        goal = SpeechGoal(key="excited_01")
        self.client.send_goal(goal)
        self.client.wait_for_result()

    def sad_entered(self, step):
        self.instruct()
        goal = SpeechGoal(key="sad_01")
        self.client.send_goal(goal)
        self.client.wait_for_result()

if __name__ == '__main__':
    rospy.init_node('say_hello')
    task = SayHello()
    rospy.spin()
