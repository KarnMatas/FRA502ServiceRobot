from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
	use_sim_time = LaunchConfiguration('use_sim_time', default='false')
	gz = ExecuteProcess(
			cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so',
			 'Worlds/BuildingScene.world'],
			output='screen'
	)
	spawn_entity = Node(package='gazebo_ros', node_executable='spawn_entity.py',
                arguments=['-entity', 'mulecar', '-file', 'Models/myfirsturdf.urdf'],
                output='screen')
	return LaunchDescription([
		#gz,
		#spawn_entity,
		DeclareLaunchArgument(
		    'use_sim_time',
		    default_value='false',
		    description='Use simulation (Gazebo) clock if true'),
		Node(
		    package='robot_state_publisher',
		    executable='robot_state_publisher',
		    name='robot_state_publisher',
		    output='screen',
		    parameters=[{'use_sim_time': use_sim_time}],
		    arguments=['Models/myfirsturdf.urdf'])
        
  	])
