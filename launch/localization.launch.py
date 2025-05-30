# from launch import LaunchDescription
# from launch_ros.actions import Node
# from launch.substitutions import LaunchConfiguration
# from launch.actions import DeclareLaunchArgument
# import os

# def generate_launch_description():
#     map_path = LaunchConfiguration('map')
#     use_sim_time = LaunchConfiguration('use_sim_time')

#     return LaunchDescription([  
#         DeclareLaunchArgument('map', default_value='/home/shriya/ros2_ws/src/2wheeldrive/maps/mapfinal.yaml'),
#         DeclareLaunchArgument('use_sim_time', default_value='true'),

#         Node(  
#             package='nav2_map_server',  
#             executable='map_server',
#             name='map_server',
#             output='screen',
#             parameters=[{
#                 'use_sim_time': use_sim_time,
#                 'yaml_filename': map_path
#             }]
#         ),

#         Node(
#             package='nav2_amcl',
#             executable='amcl',
#             name='amcl',
#             output='screen',
#             parameters=['/home/shriya/ros2_ws/src/2wheeldrive/config/amcl.yaml', {'use_sim_time': use_sim_time}]
#         ),

#         Node(
#             package='robot_localization',
#             executable='ekf_node',
#             name='ekf_node',
#             output='screen',
#             parameters=['/home/shriya/ros2_ws/src/2wheeldrive/config/ekf.yaml']
#         ),

#         Node(
#             package='nav2_lifecycle_manager',  
#             executable='lifecycle_manager',
#             name='lifecycle_manager',
#             output='screen',
#             parameters=[{
#                 'use_sim_time': use_sim_time,
#                 'autostart': True,
#                 'node_names': ['map_server', 'amcl']
#             }]
#         ),
#     ])