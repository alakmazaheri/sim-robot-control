#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64, Float64MultiArray

drive_pub = rospy.Publisher('r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=1)
head_pub = rospy.Publisher('r2d2_head_controller/command', Float64, queue_size=1)
gripper_pub = rospy.Publisher('r2d2_gripper_controller/command', Float64MultiArray, queue_size=1)

rospy.init_node('drive_gripper')

# define driving motions
stop_twist = Twist() 
forward_twist = Twist()
forward_twist.linear.x = 10
right_twist = Twist() 
right_twist.angular.z = -5

# define arm motions
retracted_pose = Float64MultiArray()
retracted_pose.data = [-0.5, 0, 0]
extended_pose = Float64MultiArray()
extended_pose.data = [0, 0.5, 0.5]

driving_forward = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  if driving_forward:
    gripper_pub.publish(retracted_pose)
    drive_pub.publish(forward_twist)
  else:
    gripper_pub.publish(extended_pose)
    drive_pub.publish(right_twist)

  if rospy.Time.now() > light_change_time:
    driving_forward = not driving_forward
    light_change_time = rospy.Time.now() + rospy.Duration(3)

rate.sleep()
