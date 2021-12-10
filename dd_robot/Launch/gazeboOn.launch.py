import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
	#use_sim_time = LaunchConfiguration('use_sim_time', default='false')
	#gz = ExecuteProcess(
	#		cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so',
	#		 'Worlds/BuildingScene.world'],
	#		output='screen'
	#)
	use_sim_time = LaunchConfiguration('use_sim_time', default='true')
	pkg_fra502 = get_package_share_directory('dd_robot')
	world_file_name = 'world2.world'
	print("world_file_name : {}".format(world_file_name))
	world = os.path.join(
		pkg_fra502,
		world_file_name)

	gz = ExecuteProcess(
		cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', world],
		output='screen')
	
	return LaunchDescription([
		gz
        
  	])
