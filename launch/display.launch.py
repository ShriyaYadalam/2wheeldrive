# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource 
# from launch.conditions import IfCondition, UnlessCondition 
# from launch.substitutions import Command, LaunchConfiguration
# from launch_ros.actions import Node
# from launch_ros.substitutions import FindPackageShare
# from launch_ros.parameter_descriptions import ParameterValue
# from launch.actions import ExecuteProcess
# import xacro
# import os
# from ament_index_python.packages import get_package_share_directory

# def generate_launch_description():
#     pkg_share = FindPackageShare(package='2wheeldrive').find('2wheeldrive')
#     default_model_path = os.path.join(pkg_share, 'src', '2wheeldrive.urdf')
#     default_rviz_config_path = os.path.join(pkg_share, 'rviz', 'config.rviz')
#     default_map_yaml_path = os.path.join(pkg_share, 'maps', 'mapfinal.yaml') 
   

#     robot_state_publisher_node = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',  
#         # parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
#         parameters=[{'robot_description': ParameterValue(Command(['xacro ', LaunchConfiguration('model')]), value_type=str)}, {'use_sim_time': True}]
  
#     )
#     gaz = ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', '-world', '/home/shriya/world1.world'], output='screen')

#     joint_state_publisher_node = Node(
#         package='joint_state_publisher',
#         executable='joint_state_publisher',
#         name='joint_state_publisher',
#         arguments=[default_model_path],    
#         parameters=[{'robot_description': Command(['xacro ', default_model_path])}, {'use_sim_time': True}],
#         condition=UnlessCondition(LaunchConfiguration('gui'))
#     )
#     joint_state_publisher_gui_node = Node(
#         package='joint_state_publisher_gui',
#         executable='joint_state_publisher_gui',
#         name='joint_state_publisher_gui',
#         parameters=[{'use_sim_time': True}],
#         condition=IfCondition(LaunchConfiguration('gui'))
#     )
#     rviz_node = Node(
#         package='rviz2', 
#         executable='rviz2',
#         name='rviz2',
#         output='screen',
#         parameters=[{'use_sim_time': True}], 
#         arguments=['-d', LaunchConfiguration('rvizconfig')],
#     )

#     spawn_entity = Node(  
#     package='gazebo_ros',
#     executable='spawn_entity.py',
#     parameters=[{'use_sim_time': True}],
#     arguments=['-entity', '2wheeldrive', '-topic', 'robot_description', '-x', '10', '-y', '10'],
#     output='screen'
#     )
 
    # robot_localization_node = Node( 
    # package='robot_localization',
    # executable='ekf_node',   
    # name='ekf_node',
    # output='screen',
    # parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
    # )

#     map_server = Node(
#     package='nav2_map_server',
#     executable='map_server',
#     name='map_server',
#     output='screen',
#     parameters=[{'use_sim_time': True ,
#                 'yaml_filename': default_map_yaml_path}]
# )
    

#     amcl = Node(
#     package='nav2_amcl', 
#     executable='amcl',
#     name='amcl', 
#     output='screen',
#     parameters=[{
#                 'use_sim_time': True,  
#                 'alpha1': 0.2,
#                 'alpha2': 0.2,
#                 'alpha3': 0.2,
#                 'alpha4': 0.2,
#                 'base_frame_id': 'base_link',
#                 'global_frame_id': 'map',
#                 'odom_frame_id': 'odom',
#                 'scan_topic': 'scan',
#                 'transform_tolerance': 0.1,
#                 'max_particles': 2000,
#                 'min_particles': 500,
#             }] 
# )

 
# #     amcl = Node(
# #     package='nav2_amcl', 
# #     executable='amcl',
# #     name='amcl', 
# #     output='screen',
# #     parameters=[os.path.join(pkg_share, 'config', 'nav2_params.yaml'),  
# #                 {'use_sim_time': LaunchConfiguration('use_sim_time')}]
# # ) 
    

#     lifecycle_manager = Node(
#     package='nav2_lifecycle_manager',
#     executable='lifecycle_manager',
#     name='lifecycle_manager_localization',
#     output='screen',
#     parameters=[{'use_sim_time': True},
#                 {'autostart': True}, 
#                 {'node_names': ['map_server', 'amcl']}]
# )    
 
 
     
#     return LaunchDescription([
#         DeclareLaunchArgument(name='gui', default_value='True', description='Flag to enable joint_state_publisher_gui'),
#         DeclareLaunchArgument(name='model', default_value=default_model_path, description='Absolute path to robot model file'),
#         DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path, description='Absolute path to rviz config file'),
#         DeclareLaunchArgument(name='use_sim_time', default_value='True', description='Flag to enable use_sim_time'),
#         gaz,
#         joint_state_publisher_node,  
#         joint_state_publisher_gui_node, 
#         robot_state_publisher_node,
#         spawn_entity,
#         rviz_node, 
#         # robot_localization_node,   
#         map_server,
#         amcl,
#         lifecycle_manager,
  
#     ])  


from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource 
from launch.conditions import IfCondition, UnlessCondition 
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue
import xacro
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = FindPackageShare(package='2wheeldrive').find('2wheeldrive')
    default_model_path = os.path.join(pkg_share, 'src', '2wheeldrive.urdf')
    default_rviz_config_path = os.path.join(get_package_share_directory('nav2_bringup'), 'rviz', 'nav2_default_view.rviz')    
    default_map_yaml_path = '/home/shriya/ros2_ws/src/2wheeldrive/maps/mapfinal.yaml'
     
    print(f"Package share path: {pkg_share}")
    print(f"Map file path: {default_map_yaml_path}")
    print(f"Map file exists: {os.path.exists(default_map_yaml_path)}")
    
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher', 
        parameters=[{
            'robot_description': ParameterValue(Command(['xacro ', LaunchConfiguration('model')]), value_type=str),
            'use_sim_time': True
        }]
    )

    gaz = ExecuteProcess(
        cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', 
             '-world', '/home/shriya/world1.world'], 
        output='screen'
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',  
        parameters=[{
            'robot_description': ParameterValue(Command(['xacro ', default_model_path]), value_type=str),
            'use_sim_time': True
        }],
        condition=UnlessCondition(LaunchConfiguration('gui'))
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        parameters=[{'use_sim_time': True}],
        condition=IfCondition(LaunchConfiguration('gui'))
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        parameters=[{'use_sim_time': True}],
        arguments=['-entity', '2wheeldrive', '-topic', 'robot_description', '-x', '10', '-y', '10'],
        output='screen'
    )

    cmd_vel_bridge = Node( 
    package='topic_tools',
    executable='relay',
    name='cmd_vel_bridge',
    arguments=['/cmd_vel', '/demo/cmd_vel'],
    parameters=[{'use_sim_time': True}],
    output='screen'
    ) 

    relay_odom = Node(
    package='topic_tools',
    executable='relay',
    name='odom_relay',
    arguments=['/demo/odom', '/odom'],
    parameters=[{'use_sim_time': True}],
    output='screen'  
)


    map_server = Node( 
        package='nav2_map_server',
        executable='map_server',
        name='map_server',
        output='screen',
        parameters=[{
            'use_sim_time': True,   
            'yaml_filename': default_map_yaml_path,
            'topic_name': 'map',
            'frame_id': 'map'
        }],
    )

    static_tf_map_odom = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_tf_pub_map_odom',
        arguments=['0', '0', '0', '0', '0', '0', 'map', 'odom'],
        parameters=[{'use_sim_time': True}]
    ) 

    robot_localization_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_filter_node',
        output='screen',
        parameters=[os.path.join(pkg_share, 'config/ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
  
    )

    amcl = Node(
        package='nav2_amcl',  
        executable='amcl',
        name='amcl', 
        output='screen',   
        parameters=[{
            'use_sim_time': True,
            'alpha1': 0.2,
            'alpha2': 0.2,
            'alpha3': 0.2,
            'alpha4': 0.2,
            'base_frame_id': 'base_link',
            'global_frame_id': 'map',
            'odom_frame_id': 'odom',
            'scan_topic': 'scan',
            'transform_tolerance': 0.1,
            'max_particles': 2000,
            'min_particles': 500,
            'set_initial_pose': True, 
            'initial_pose.x': 10.0,
            'initial_pose.y': 10.0,
            'initial_pose.z': 0.0,
            'initial_pose.yaw': 0.0,            
        }] 
    )

    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_localization',
        output='screen',
        parameters=[{
            'use_sim_time': True,
            'autostart': True, 
            'node_names': ['map_server', 'amcl']   
        }]
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'use_sim_time': True}], 
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    return LaunchDescription([
        DeclareLaunchArgument(name='gui', default_value='True', 
                             description='Flag to enable joint_state_publisher_gui'),
        DeclareLaunchArgument(name='model', default_value=default_model_path, 
                             description='Absolute path to robot model file'),
        DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path, 
                             description='Absolute path to rviz config file'),
        DeclareLaunchArgument(name='use_sim_time', default_value='True',
                             description='Flag to enable use_sim_time'),
        
        # Start Gazebo and robot first 
        gaz, 
        cmd_vel_bridge,
        relay_odom, 
        robot_state_publisher_node,
        joint_state_publisher_node,   
        joint_state_publisher_gui_node, 
        spawn_entity,
        rviz_node,   
        robot_localization_node, 

        # static_tf_map_odom, 
          
        # Start navigation nodes with delay    
        TimerAction( 
            period=3.0,  # Increased delay
            actions=[lifecycle_manager ]
        ),
        
        TimerAction(
            period=5.0,  
            actions=[map_server, amcl]
        )
          
    ])
  