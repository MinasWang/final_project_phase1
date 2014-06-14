#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def clamcallback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard a message %s", data.data)
    
    # here is your code for the movement of clamArm.

def listen():
    rospy.init_node('clamArm_listener', anonymous=True)
	
    rospy.Subscriber("anotherchatter",String,clamcallback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listen()
    except rospy.ROSInterruptException: pass
