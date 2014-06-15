# This is the description of simulation of turtlebot behavior

* file description:
   * final_project.py : in charge of the behavior of turtlebot.
   * talker.py : in charge of publish the goal position, we set it up to publish a goal position every 15 second.
   * clamArm_listener.py : in charge of subscribe to topic 'anotherchatter' of whether the turtle have arrived the goal position.
   * map_building.txt : a simple description of how to map the environment in both simulation and real robot.

* Note: 
   to simulate the behavior of turtlebot of auto-navigation, please put the following three file in your \<br \>
	`catkin_ws/rharmony/rbx1/rbx1_nav/nodes/` \<br \>
   and make sure they have the access of read and write. run command: \<br \>
	`chmod a+x final_project.py talker.py clamArm_listener.py`

* Details: follow these step you can make your turtlebot listening a goal position command,and auto-navigate to the goal position.
   * first thing we need to do is connect two laptop, call turtlebot_laptop and your_laptop.  
   * we need to bring up a turtlebot, if you are in simulation, please run in your_laptop: \<br \> 
       `roslaunch rbx1_bringup fake_turtlebot.launch` \<br \>
     if you are using real robot, pleast run in turtlebot_laptop: \<br \>
	`roslaunch rbx1_bringup turtlebot_minimal_create.launch`
  
   * connect to the Kinnect in your_laptop or turtlebot_laptop: \<br \>
 	`roslaunch rbx1_bringup fake_laser.launch`

   * bring up your map, if you are in simulation and you don't record any map before, please run: \<br \>
	`roslaunch rbx1_nav fake_move_base_blank_map.launch` \<br \>
     if you are runing a real turtlebot and you created a map called test_map_5.yaml, please run: \<br \>
	`roslaunch rbx1_nav fake_amcl.launch map:=test_map_5.yaml`
   
   * visualized your auto-navigation in rviz \<br \> 
     for simulation,please run : \<br \>
	`rosrun rviz rviz -d 'rospack find rbx1_nav' /nav.rviz` \<br \>
     for real turtlebot, please run: \<br \>
	`rosrun rviz rviz -d 'rospack find rbx1_nav' /amcl.rviz`
   
   * run these command in your_laptop: \<br \>
	`rosrun rbx1_nav final_project.py` \<br \>
	`rosrun rbx1_nav clamArm_listener.py` \<br \>
	`rosrun rbx1_nav talker.py`
  

  So far, you should see that the turtlebot receiving a goal positon from Quarotor every 15 second, and move to it, and then publish his state to calmArm


