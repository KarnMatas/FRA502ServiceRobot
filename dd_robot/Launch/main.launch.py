import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

import xacro


def generate_launch_description():

    pkg_dir = os.path.join(
        get_package_share_directory('dd_robot')) #ชื่อ package

    world_file_name = "world3.world"
    world_path = os.path.join(pkg_dir, world_file_name)
    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', world_path],
        output='screen')

    urdf_path = os.path.join(pkg_dir,'mooncake.urdf')
    urdf = open(urdf_path).read()
	# urdf_file_name = 'mooncake.urdf'
	# urdf = os.path.join(pkg_dir, urdf_file_name)
    ### For URDF ###
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': urdf}]
    )


    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'mooncake',"-x 1.0","-y 1.0","-z 0.0"],
                    #    arguments=['-entity', 'mooncake', '-file', urdf,"-x 1.0","-y 1.0","-z 0.0"],
                       output='screen')

    # load_joint_state_controller = ExecuteProcess(
    #     cmd=['ros2', 'control', 'load_controller', '--set-state', 'start',
    #          'joint_state_broadcaster'],
    #     output='screen'
    # )

    # load_joint_trajectory_controller = ExecuteProcess(
    #     cmd=['ros2', 'control', 'load_controller', '--set-state', 'start', 'velocity_controller'],
    #     output='screen'
    # )

    # load_imu_sensor_broadcaster = ExecuteProcess(
    #     cmd=['ros2', 'control', 'load_controller', 'imu_sensor_broadcaster'],
    #     output='screen'
    # )

    rviz_file_name = 'mapping.rviz'
    rviz_file_path = os.path.join(pkg_dir, rviz_file_name)
    rviz = ExecuteProcess(
        cmd=['rviz2', '-d', rviz_file_path],
        output='screen')

    return LaunchDescription([
        # RegisterEventHandler(
        #     event_handler=OnProcessExit(
        #         target_action=spawn_entity,
        #         on_exit=[load_joint_state_controller],
        #     )
        # ),
        # RegisterEventHandler(
        #     event_handler=OnProcessExit(
        #         target_action=load_joint_state_controller,
        #         on_exit=[load_joint_trajectory_controller],
        #     )
        # ),
        # RegisterEventHandler(
        #     event_handler=OnProcessExit(
        #         target_action=load_joint_trajectory_controller,
        #         on_exit=[load_imu_sensor_broadcaster],
        #     )
        # ),
        gazebo,
        spawn_entity,
        node_robot_state_publisher,
        rviz,
    ])