#!/usr/bin/env python

import rospy
from ros_stepup_kadai.msg import Okuha_kataranai
import time

class Oreda():
    def __init__(self):
        rospy.init_node("kitaini_kotaetemiyo")
        self.yare = rospy.get_param("kitaini_kotaetemiyo/yare")
        self.pub = rospy.Publisher("/oreno/shijini/shitagae", Okuha_kataranai, queue_size = 1)
        time.sleep(0.3)
        self.main()
        
    def main(self):
        message = Okuha_kataranai()
        if self.yare == 1: 
            message.movement = [1, 3, 4, 2]
            message.time = [3, 2, 2, 3]
        elif self.yare == 2:
            message.movement = [3, 4, 1, 2]
            message.time = [2, 2, 3, 3]
        self.pub.publish(message)

if __name__=='__main__':
    oreda = Oreda()