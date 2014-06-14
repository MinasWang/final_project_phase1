#!/usr/bin/env python
# license removed for bervity

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter',String)
    rospy.init_node('talker',anonymous=True) 
    r = rospy.Rate(0.5) #10hz
    count = 0
    while not rospy.is_shutdown():
	str = "0,0,0,%d"%count        
	#str = "hello world %s"%rospy.get_time() + " count = %d"%count
	if count == 10:
            str = "1,2,0"
	if count == 20:
	    str = "1,1.2,1.8"
	if count == 30:
	    str = "1,0.3,1.4"
	if count == 40:
	    str = "1,0.1,03"
	if count == 50:
	    str = "1,2,2.3"
	if count == 60:
	   str = "1,-1,2"
	if count == 70:
	    str = "1,1,-1"
	    count = 0
	count = count + 1
	rospy.loginfo(str)
	pub.publish(str)
	r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
