#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from random import uniform

rospy.init_node('omnibot_random_move')

cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

while not rospy.is_shutdown():
    twist_msg = Twist()
    twist_msg.linear.x = uniform(-1.0, 1.0)
    twist_msg.angular.z = uniform(-1.0, 1.0)
    cmd_vel_pub.publish(twist_msg)
    rospy.sleep(1.0)

