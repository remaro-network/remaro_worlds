import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import OpaqueFunction
from launch.conditions import LaunchConfigurationEquals
from launch.conditions import LaunchConfigurationNotEquals
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression

from launch_ros.actions import Node


def generate_launch_description():
    silent = LaunchConfiguration('silent')
    def configure_logging(context, *args, **kwargs):
        if silent.perform(context) == 'true':
            import logging
            logging.getLogger().setLevel(logging.ERROR)
        return []
    
    silent_arg = DeclareLaunchArgument(
        'silent',
        default_value='false',
        description='Suppress all output (launch logs + node logs)'
    )
    
    remaro_worlds_path = get_package_share_directory('remaro_worlds')

    gui = LaunchConfiguration('gui')
    gui_arg = DeclareLaunchArgument(
        'gui',
        default_value='true',
        description='Run with gui (true/false)')
    
    
    
    print_output = PythonExpression([
        '"log" if "', LaunchConfiguration('silent'), '" == "true" else "', LaunchConfiguration('print_output'), '"'
    ])


    print_output_arg = DeclareLaunchArgument(
        'print_output',
        default_value='screen',
        description='Whether to print output to terminal (screen/log)'
    )

    
    def launch_gz_sim(context, *args, **kwargs):
        pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
        remaro_worlds_path = get_package_share_directory('remaro_worlds')
        world_path = os.path.join(remaro_worlds_path, 'worlds', 'min_pipes.world')

        resolved_output = print_output.perform(context)
        resolved_gui = gui.perform(context)

        gz_args = '-r '
        if resolved_output == 'screen':
            gz_args += '-v 1 '
        else:
            gz_args += '-v 0 '

        if resolved_gui == 'false':
            gz_args += '-s '

        gz_args += world_path

        return [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
                launch_arguments={'gz_args': gz_args}.items()
            )
        ]

    min_pipes_environment_path = os.path.join(
        remaro_worlds_path, 'models', 'min_pipes_environment')

    min_pipes_environment_spawn = Node(
        package='ros_gz_sim',
        executable='create',
        output=print_output,
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
        output=print_output,
        arguments=[
            '-world', 'min_pipes',
            '-file', min_pipes_objects_path,
            '-name', 'min_pipes_objects']
    )

    small_min_pipes_pipeline_path = os.path.join(
        remaro_worlds_path, 'models', 'small_min_pipes_pipeline')

    small_min_pipes_pipeline_spawn = Node(
        package='ros_gz_sim',
        executable='create',
        output=print_output,
        arguments=[
            '-world', 'min_pipes',
            '-file', small_min_pipes_pipeline_path,
            '-name', 'min_pipes_pipeline']
    )

    return LaunchDescription([
        gui_arg,
        print_output_arg,
        silent_arg,
        OpaqueFunction(function=configure_logging),
        OpaqueFunction(function=launch_gz_sim),
        min_pipes_environment_spawn,
        min_pipes_objects_spawn,
        small_min_pipes_pipeline_spawn,
    ])
