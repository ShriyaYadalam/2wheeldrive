# import os
# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
# from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare

# def generate_launch_description():

#     nav2_pkg_share = FindPackageShare('2wheeldrive').find('2wheeldrive')

#     param_file = os.path.join(nav2_pkg_share, 'config', 'nav2_params.yaml')

#     map_yaml_file = os.path.join(nav2_pkg_share, 'maps', 'mapfinal.yaml')

#     declare_param_file_cmd = DeclareLaunchArgument(
#         'params_file',
#         default_value=param_file,
#         description='Full path to the ROS2 parameters file to use for all launched nodes'
#     )
    
#     declare_map_yaml_cmd = DeclareLaunchArgument(
#         'map',  
#         default_value=map_yaml_file,
#         description='Full path to map yaml file to load'
#     )
    
#     map_server_node = Node(
#         package='nav2_map_server',
#         executable='map_server',
#         name='map_server', 
#         output='screen',
#         parameters=[{'yaml_filename': LaunchConfiguration('map')}]
#     )

#     amcl_node = Node(
#         package='nav2_amcl',
#         executable='amcl',
#         name='amcl',
#         output='screen',
#         parameters=[LaunchConfiguration('params_file')]
#     )

#     planner_server_node = Node(
#         package='nav2_planner',
#         executable='planner_server',
#         name='planner_server',
#         output='screen',
#         parameters=[LaunchConfiguration('params_file')]
#     )

#     controller_server_node = Node(
#         package='nav2_controller',
#         executable='controller_server',
#         name='controller_server',
#         output='screen',
#         parameters=[LaunchConfiguration('params_file')]
#     )

#     behavior_server_node = Node(
#         package='nav2_behavior_tree',
#         executable='behavior_server',
#         name='behavior_server',
#         output='screen',
#         parameters=[LaunchConfiguration('params_file')]
#     )

#     bt_navigator_node = Node(
#         package='nav2_bt_navigator',
#         executable='bt_navigator',
#         name='bt_navigator',
#         output='screen',
#         parameters=[LaunchConfiguration('params_file')]
#     )

#     lifecycle_manager_node = Node(
#         package='nav2_lifecycle_manager',
#         executable='lifecycle_manager',
#         name='lifecycle_manager_navigation',
#         output='screen',
#         parameters=[{'use_sim_time': False},
#                     {'autostart': True},
#                     {'node_names': ['map_server',
#                                     'amcl',
#                                     'planner_server',
#                                     'controller_server',
#                                     'behavior_server',
#                                     'bt_navigator']}]
#     )

#     return LaunchDescription([
#         declare_param_file_cmd,
#         declare_map_yaml_cmd,
#         map_server_node,
#         amcl_node,
#         planner_server_node,
#         controller_server_node,
#         behavior_server_node,
#         bt_navigator_node,
#         lifecycle_manager_node,
#     ])
