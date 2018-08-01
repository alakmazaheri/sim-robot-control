#!/usr/bin/env python
import sys, rospy, tf, moveit_commander, random
from geometry_msgs.msg import Pose, Point, Quaternion

orient = Quaternion(*tf.transformations.quaternion_from_euler(3.14, 0, -0))
pose = Pose(Point(0, 0, 0), orient)
moveit_commander.roscpp_initialize(sys.argv) # <3>
rospy.init_node('poppy_bend',anonymous=True)
group = moveit_commander.MoveGroupCommander("chest")


# now, wave arms around randomly 
while not rospy.is_shutdown():
    group.set_pose_target(pose)
    group.go(True)

moveit_commander.roscpp_shutdown()
