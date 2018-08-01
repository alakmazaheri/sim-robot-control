#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random
from geometry_msgs.msg import Pose, Point, Quaternion

orient = [Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0)),
          Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))] # <1>
pose = [Pose(Point( 0, 0, 0), orient[0]),
        Pose(Point(0, 0, 0), orient[1])] # <2>
moveit_commander.roscpp_initialize(sys.argv) # <3>
rospy.init_node('poppy_wave_arm',anonymous=True)
group = [moveit_commander.MoveGroupCommander("left_leg"),
         moveit_commander.MoveGroupCommander("right_leg")]


# now, wave arms around randomly 
while not rospy.is_shutdown():
  pose[0].position.x =  0 + random.uniform(-0.1, 0.1)
  pose[1].position.x = 0 + random.uniform(-0.1, 0.1)
  for side in [0,1]:
    pose[side].position.z =  0 + random.uniform(-0.1, 0.1)
    group[side].set_pose_target(pose[side])
    group[side].go(True)

moveit_commander.roscpp_shutdown()
