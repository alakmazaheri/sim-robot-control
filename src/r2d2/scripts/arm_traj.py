#!/usr/bin/env python
import rospy, time
from rospy.rostime import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

rospy.init_node('arm_traj_loop')
left_arm_pub = rospy.Publisher('r2d2_left_arm_controller/command', JointTrajectory, queue_size=10)
right_arm_pub = rospy.Publisher('r2d2_right_arm_controller/command', JointTrajectory, queue_size=10)

waypoint1 = JointTrajectoryPoint()
waypoint1.positions = [0.25, -1.5, 0.0]
waypoint1.time_from_start = Duration(0.0)

waypoint2 = JointTrajectoryPoint()
waypoint2.positions = [0.75, -2.0, 0.75]
waypoint2.time_from_start = Duration(1.0)

waypoint3 = JointTrajectoryPoint()
waypoint3.positions = [-0.15, -3.0, -1]
waypoint3.time_from_start = Duration(3.0)

waypoint4 = JointTrajectoryPoint()
waypoint4.positions = [0, 0.5, 1]
waypoint4.time_from_start = Duration(5.0)

left_traj = JointTrajectory()
left_traj.joint_names = ["left_shoulder","left_elbow", "left_wrist"]
left_traj.points = [waypoint1, waypoint2, waypoint3, waypoint4]

waypoint5 = JointTrajectoryPoint()
waypoint5.positions = [0.25, -1.5, 0.0]
waypoint5.time_from_start = Duration(1.0)

waypoint6 = JointTrajectoryPoint()
waypoint6.positions = [0.75, -2.0, 0.75]
waypoint6.time_from_start = Duration(2.0)

waypoint7 = JointTrajectoryPoint()
waypoint7.positions = [-0.15, -3.0, -1]
waypoint7.time_from_start = Duration(4.0)

waypoint8 = JointTrajectoryPoint()
waypoint8.positions = [0, 0.5, 1]
waypoint8.time_from_start = Duration(6.0)

right_traj = JointTrajectory()
right_traj.joint_names = ["right_shoulder","right_elbow", "right_wrist"]
right_traj.points = [waypoint5, waypoint6, waypoint7, waypoint8]

rospy.sleep(1)
left_arm_pub.publish(left_traj)
right_arm_pub.publish(right_traj)
rospy.sleep(1)
