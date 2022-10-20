import os

from ament_index_python.packages import get_package_share_directory
# from ament_index_python.packages import get_prefix_for_package

from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
# from launch.actions import ExecuteProcess
# from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    remaro_worlds_path = get_package_share_directory('remaro_worlds')

    world_path = os.path.join(remaro_worlds_path, 'worlds', 'min_pipes.world')

    min_pipes_world = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={
           'gz_args': '-r ' + world_path
        }.items(),
    )

    min_pipes_environment_path = os.path.join(
        remaro_worlds_path, 'models', 'min_pipes_environment')

    min_pipes_environment_spawn = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'min_pipes',
            '-file', min_pipes_environment_path,
            '-name', 'min_pipes_environment']
    )

    min_pipes_objects_path = os.path.join(
        remaro_worlds_path, 'models', 'min_pipes_objects')

    min_pipes_objects_spawn = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'min_pipes',
            '-file', min_pipes_objects_path,
            '-name', 'min_pipes_objects']
    )

    return LaunchDescription([
        min_pipes_world,
        min_pipes_environment_spawn,
        min_pipes_objects_spawn,
    ])
