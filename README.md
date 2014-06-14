
* to simulate the behavior of turtlrbot of auto-navigation, please puth this follow three file in you catkin_ws/rharmony/rbx1/rbx1_nav/nodes/, and make sure they have the access of read and wriet. run chmod a+x final_project.py talker.py clamArm_listener.py

* run the following command to see the simulation:
   roslaunch rbx1_bringup fake_turtlebot.launch
   roslaunch rbx1_nav fake_move_base_blank_map.launch
   rosrun rviz rviz -d `rospack find rbx1_nav` /nav.rviz
   rosrun rbx1_nav final_project.py
   rosrun rbx1_nav clamArm_listener.py
   rosrun rbx1_nav talker.py



