#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int16

LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.5

class Mob_A():
    def __init__(self):
        rospy.init_node("shouchi")
        self.pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size = 1)
        self.sub = rospy.Subscriber("/oreno/shijini/shitagae", Int16, self.main)
    
    def main(self, message):
        t = Twist()
        linear = 0
        angular = 0
        if message.data == 0:    #stop
            pass
        elif message.data == 1:  #forword
            linear = 1
        elif message.data == 2:  #backword
            linear = -1
        elif message.data == 3:  #left
            angular = 1
        elif message.data == 4:  #right
            angular = -1
        elif message.data == 5:  #finish
            print("finish")
            exit()

        t.linear.x = linear * LINEAR_SPEED
        t.angular.z = angular * ANGULAR_SPEED
        self.pub.publish(t)


if __name__=='__main__':
    try: 
        mob_A = Mob_A()
        rospy.spin()
    
    except KeyboardInterrupt:
        pass