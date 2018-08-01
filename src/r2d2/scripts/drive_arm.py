#!/usr/bin/env python
import rospy, time
from rospy.rostime import Duration

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64, Float64MultiArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

drive_pub = rospy.Publisher('r2d2_diff_drive_controller/cmd_vel', Twist, queue_size=1)
head_pub = rospy.Publisher('r2d2_head_controller/command', Float64, queue_size=1)
gripper_pub = rospy.Publisher('r2d2_gripper_controller/command', Float64MultiArray, queue_size=1)
arm_pub = rospy.Publisher('r2d2_left_arm_controller/command', JointTrajectory, queue_size=10)

rospy.init_node('drive_traj')

# define driving motions
stop_twist = Twist() 
forward_twist = Twist()
forward_twist.linear.x = -10
right_twist = Twist() 
right_twist.angular.z = -5

# define gripper motions
retracted_pose = Float64MultiArray()
retracted_pose.data = [-0.5, 0, 0]
extended_pose = Float64MultiArray()
extended_pose.data = [0, 0.5, 0.5]

#define arm motions
waypoint1 = JointTrajectoryPoint()
waypoint1.positions = [0.25, -1.5, 0.0]
waypoint1.time_from_start = Duration(0.0)

waypoint2 = JointTrajectoryPoint()
waypoint2.positions = [0.75, -2.0, 0.75]
waypoint2.time_from_start = Duration(1.0)

waypoint3 = JointTrajectoryPoint()
waypoint3.positions = [-0.15, -3.0, -1]
waypoint3.time_from_start = Duration(0.0)

waypoint4 = JointTrajectoryPoint()
waypoint4.positions = [0, 0.5, 1]
waypoint4.time_from_start = Duration(1.0)

traj1 = JointTrajectory()
traj1.joint_names = ["left_shoulder","left_elbow", "left_wrist"]
traj1.points = [waypoint1, waypoint2]

traj2 = JointTrajectory()
traj2.joint_names = ["left_shoulder","left_elbow", "left_wrist"]
traj2.points = [waypoint3, waypoint4]

driving_forward = False
light_change_time = rospy.Time.now()
rate = rospy.Rate(1)

gripper_pub.publish(extended_pose)

while not rospy.is_shutdown():
  if driving_forward:
    drive_pub.publish(forward_twist)
    arm_pub.publish(traj1)
  else:
    drive_pub.publish(right_twist)
    arm_pub.publish(traj2)

  if rospy.Time.now() > light_change_time:
    driving_forward = not driving_forward
    light_change_time = rospy.Time.now() + rospy.Duration(3)

rate.sleep()
