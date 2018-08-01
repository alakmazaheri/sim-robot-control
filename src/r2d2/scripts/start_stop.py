#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('start_stop')
drive_pub = rospy.Publisher('r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=1)

red_light_twist = Twist() 
green_light_twist = Twist()
green_light_twist.linear.x = 300 #<3>

driving_forward = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  if driving_forward:
    drive_pub.publish(green_light_twist) #<4>
  else:
    drive_pub.publish(red_light_twist)

  if rospy.Time.now() > light_change_time:
    drive_forward = not driving_forward
    light_change_time = rospy.Time.now() + rospy.Duration(3)

rate.sleep()



