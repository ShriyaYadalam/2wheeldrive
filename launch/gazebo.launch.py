import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Get package directory
    pkg_share = get_package_share_directory('2wheeldrive')
    urdf_file = os.path.join(pkg_share, 'src', '2wheeldrive.urdf')
    
    # Read and sanitize URDF
    with open(urdf_file, 'r', encoding='utf-8') as infp:
        robot_desc = infp.read()
    if '<?xml version="1.0" encoding=' in robot_desc:
        end_of_declaration = robot_desc.find('?>') + 2
        robot_desc = robot_desc[end_of_declaration:].strip()
        robot_desc = '<?xml version="1.0"?>\n' + robot_desc
    
    # Gazebo launch file
    gazebo_launch_file = os.path.join(
        get_package_share_directory('gazebo_ros'),
        'launch',
        'gazebo.launch.py'
    )
    
    # Print debug info
    print(f"URDF file: {urdf_file}")
    print(f"File exists: {os.path.exists(urdf_file)}")

    # Launch Description
    return LaunchDescription([
        # Start Gazebo first
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch_file),
            launch_arguments={'world': 'empty.world'}.items()
        ),
        
        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_desc,
                'use_sim_time': True
            }]
        ),
        
        # Static TF between footprint and base_link
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='tf_footprint_base',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'],
            parameters=[{'use_sim_time': True}]
        ),
        
        # Spawn the robot after a 5s delay to ensure Gazebo is up
        TimerAction(
            period=5.0,  # wait a bit longer for Gazebo to fully come up
            actions=[
                Node(
                    package='gazebo_ros',
                    executable='spawn_entity.py',
                    name='spawn_model',
                    arguments=['-topic', 'robot_description', '-entity', 'amr_urdf_v3'],
                    output='screen'
                )
            ]
        ),
        
        # Publish calibration message after the robot is spawned
        TimerAction(
            period=8.0,  # wait a bit more before calibration
            actions=[
                ExecuteProcess(
                    cmd=['ros2', 'topic', 'pub', '--once', '/calibrated', 'std_msgs/msg/Bool', 'data: true'],
                    name='fake_joint_calibration'
                )
            ]
        )
    ])
