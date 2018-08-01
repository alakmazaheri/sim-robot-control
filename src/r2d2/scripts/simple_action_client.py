#!/usr/bin/env python

# CLIENT: Follow Joint Trajectory

import argparse
import sys
import rospy
import time
import actionlib

from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from rospy.rostime import Duration

def feedback_cb(feedback):
    print("[FEEDBACK]")
    print(feedback.error.positions)

# setup CLIENT
print("Initializing client node...")
rospy.init_node('traj_action_client')

print("Generating client...")
#client = actionlib.SimpleActionClient('myTraj', FollowJointTrajectoryAction)
client = actionlib.SimpleActionClient('r2d2_left_arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)

print("Waiting for server...")
client.wait_for_server()

# create goal
goal = FollowJointTrajectoryGoal()

# define goal trajectory
waypoint1 = JointTrajectoryPoint()
waypoint1.positions = [0, 1, .75]
waypoint1.time_from_start = Duration(0.0)

traj1 = JointTrajectory()
traj1.joint_names = ["left_shoulder","left_elbow", "left_wrist"]
traj1.points = [waypoint1]

# set goal trajectory
goal.trajectory = traj1

# send goal
client.send_goal(goal, feedback_cb=feedback_cb)
print("Sent goal")
 
client.wait_for_result()
print('[Result] State: %d'%(client.get_state()))

time.sleep(15)
