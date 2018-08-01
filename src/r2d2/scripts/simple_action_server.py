#! /usr/bin/env python

# SERVER : Follow Joint Trajectory

import rospy
import numpy
import time
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal, FollowJointTrajectoryResult, FollowJointTrajectoryFeedback
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def do_trajectory(goal):
        joint_names = goal.trajectory.joint_names
        trajectory_points = goal.trajectory.points
	print("GOAL TRAJECTORY:")
	print(goal.trajectory)

	# publish normally???
	left_arm_pub = rospy.Publisher('r2d2_left_arm_controller/command', JointTrajectory, queue_size=10)
	left_arm_pub.publish(goal.trajectory)
	# print("Published")

	start_time = time.time()
	print(time.time() - start_time)
	while(time.time() - start_time < 10):	
		print(time.time() - start_time)	
		feedback = FollowJointTrajectoryFeedback()

		feedback.desired = JointTrajectoryPoint()
		feedback.desired = goal.trajectory.points[0]

		# get actual positions from joint state or robot publisher ...	
		feedback.actual = JointTrajectoryPoint()
		feedback.actual.positions = [0, 0, 0]

		feedback.error = JointTrajectoryPoint()
		feedback.error.positions = numpy.subtract(feedback.desired.positions,feedback.actual.positions)

		server.publish_feedback(feedback)
		
		time.sleep(1.0)

	result = FollowJointTrajectoryResult()
	server.set_succeeded(result, "Trajectory completed successfully")
	print(result.SUCCESSFUL)

print("Initializing server node...")
rospy.init_node('traj_action_server')

print("Generating server...")
server = actionlib.SimpleActionServer('r2d2_left_arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction, do_trajectory, False)
# server = actionlib.SimpleActionServer('myTraj', FollowJointTrajectoryAction, do_trajectory, False)
server.start()
rospy.spin()
