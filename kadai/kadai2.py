#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
import time

class Oreda():
    def __init__(self):
        rospy.init_node("kitaini_kotaetemiyo")
        self.pub = rospy.Publisher("/oreno/shijini/shitagae", Int16, queue_size = 1)
        self.main()
        
    def main(self):
        message = Int16()
        rate = rospy.Rate(50)
        start_time = time.time()
        while not rospy.is_shutdown():
            now_time = time.time()
            if now_time - start_time < 3:
                message.data = 1  #forword
            elif now_time - start_time < 5:
                message.data = 3  #left
            elif now_time - start_time < 7:
                message.data = 4  #right
            elif now_time - start_time < 10:
                message.data = 2  #backword
            else:
                message.data = 0  #stop
                break
            self.pub.publish(message)
            
            rate.sleep()
        
        message.data = 5  #finish
        self.pub.publish(message)


if __name__=='__main__':
    try: 
        oreda = Oreda()
    
    except KeyboardInterrupt:
        pass