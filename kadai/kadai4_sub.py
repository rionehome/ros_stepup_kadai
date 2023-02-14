#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from ros_stepup_kadai.msg import Okuha_kataranai
import time

N = 4  #element count
LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.5

class Mob_A():
    def __init__(self):
        rospy.init_node("shouchi")
        self.pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 1)
        self.sub = rospy.Subscriber("/oreno/shijini/shitagae", Okuha_kataranai, self.main)
    
    def main(self, message):
        for i in range(0, N):
            t = Twist()
            linear = 0
            angular = 0
            mov = message.movement[i]
            tim = message.time[i]

            if mov == 0:    #stop
                pass
            elif mov == 1:  #forword
                linear = 1
            elif mov == 2:  #backword
                linear = -1
            elif mov == 3:  #left
                angular = 1
            elif mov == 4:  #right
                angular = -1
            t.linear.x = linear * LINEAR_SPEED
            t.angular.z = angular * ANGULAR_SPEED

            start_time = time.time()
            end_time = time.time()
            while end_time - start_time < tim:
                self.pub.publish(t)
                end_time = time.time()


if __name__=='__main__':
    try: 
        mob_A = Mob_A()
        rospy.spin()
    
    except KeyboardInterrupt:
        pass