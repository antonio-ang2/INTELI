#!/usr/bin/env python3

import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ola_mundo',
            executable='ola',  # Substitua pelo nome real do seu executável
            output='screen',
        ),
    ])
