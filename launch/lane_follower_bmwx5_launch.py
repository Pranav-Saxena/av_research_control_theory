import os
import launch
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.substitutions.path_join_substitution import PathJoinSubstitution
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController

def generate_launch_description():
    package_dir = get_package_share_directory('av_research_control_theory')
    world = LaunchConfiguration('world')

    webots = WebotsLauncher(
        world=PathJoinSubstitution([package_dir, 'worlds', world]),
        ros2_supervisor=True
    )

    robot_description_path = os.path.join(package_dir, 'resource', 'my_vehicle.urdf')
    my_vehicle_driver = WebotsController(
        robot_name='vehicle',
        parameters=[
            {'robot_description': robot_description_path}
        ],
        respawn=True
    )
    lane_follower = Node(
        package='av_research_control_theory',
        executable='lane_follower',
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='bmwx5.wbt',
            description='Choose one of the world files from `/av_research_control_theory/worlds` directory'
        ),
        webots,
        webots._supervisor,
        my_vehicle_driver,
        lane_follower,

        # This action will kill all nodes once the Webots simulation has exited
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[
                    launch.actions.EmitEvent(event=launch.events.Shutdown())
                ],
            )
        )
    ])
