#!/usr/bin/env python
import rospy, time
from rospy.rostime import Duration

from geometry_msgs.msg import Twist
from std_msgs.msg import Float64, Float64MultiArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

left_leg_pub = rospy.Publisher('left_leg_controller/command', JointTrajectory, queue_size=10)
right_leg_pub = rospy.Publisher('right_leg_controller/command', JointTrajectory, queue_size=10)

rospy.init_node('run_traj')



#define arm motions
wp1 = JointTrajectoryPoint()
wp1.positions =  [0, 0, 1.5, -1.5, 0.25]
wp1.time_from_start = Duration(0.0)

wp2R = JointTrajectoryPoint()
wp2R.positions = [0, 0, 0, 0, -0.25]
wp2R.time_from_start = Duration(0.25)

wp3 = JointTrajectoryPoint()
wp3.positions = [0, 0, -1.5, -1.5, -0.25]
wp3.time_from_start = Duration(1.0)

wp4 = JointTrajectoryPoint()
wp4.positions = [0, 0, 1.5, -1.5, 0.25]
wp4.time_from_start = Duration(2.0)

wp5 = JointTrajectoryPoint()
wp5.positions = [0, 0, -1.5, -1.5, -0.25]
wp5.time_from_start = Duration(3.0)

wp5L = JointTrajectoryPoint()
wp5L.positions = [0, 0, 0, 0, -0.25]
wp5L.time_from_start = Duration(3.25)

wp6 = JointTrajectoryPoint()
wp6.positions =  [0, 0, 1.5, -1.5, 0.25]
wp6.time_from_start = Duration(4)

traj1 = JointTrajectory()
traj1.joint_names = ["r_hip_x", "r_hip_z", "r_hip_y", "r_knee_y", "r_ankle_y"]
traj1.points = [wp1, wp2R, wp3, wp4, wp5, wp6]

traj2 = JointTrajectory()
traj2.joint_names = ["l_hip_x", "l_hip_z", "l_hip_y", "l_knee_y", "l_ankle_y"]
traj2.points = [wp1, wp3, wp4, wp5, wp5L, wp6]


rate = rospy.Rate(1)

while not rospy.is_shutdown():
    right_leg_pub.publish(traj1)
    left_leg_pub.publish(traj2)
    time.sleep(3)
    

rate.sleep()
