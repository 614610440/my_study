#!/usr/bin/env python

from dynamixel_monitor_module.msg import *
import rospy

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %d', data.present_torque)

if __name__ == '__main__':
    rospy.init_node('dynamixel_state_plot', anonymous=True)
    rospy.Subscriber('/monitor_module/dynamixel_state', DyState, callback)

    while True:
        rospy.spin()
