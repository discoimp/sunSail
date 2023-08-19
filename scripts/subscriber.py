#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String

# Define Operation Window for the SunSail in mm
opWindowX = 6000
opWindowY = 6000

# Define the SunSail's measurements in mm
sunSailX = 3400
sunSailY = 4000

# Calculate bounds of the SunSail's operation window
xMin = (opWindowX - sunSailX) / 2

# sketch of simple logic for actuators:
def move_actuators(dx, dy):
    # Assuming the sunSail's width is `w` and height is `h`.
    w_change = dx / 2.0
    h_change = dy / 2.0

    # Calculate wire length changes:
    A_change = (-w_change, -h_change)  # Top-left retracts for rightward and upward movement.
    B_change = (w_change, -h_change)   # Top-right extends for rightward and retracts for upward movement.
    C_change = (w_change, h_change)    # Bottom-right extends for both rightward and upward movement.
    D_change = (-w_change, h_change)   # Bottom-left retracts for rightward and extends for upward movement.

    # Each actuator takes a "delta" value for how much to change its length.
    A_actuator.publish(A_change)
    B_actuator.publish(B_change)
    C_actuator.publish(C_change)
    D_actuator.publish(D_change)


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # use data.data to get the string that was published.
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()

