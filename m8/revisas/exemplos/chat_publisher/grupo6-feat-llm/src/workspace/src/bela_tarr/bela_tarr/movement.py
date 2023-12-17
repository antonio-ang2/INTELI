#! /usr/bin/env python3 
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from tf_transformations import quaternion_from_euler
from math import pi
import re

intent_dict = {
    r"\bponto\s+x\b": "x",
    r"\bponto\s+y\b": "y",
    r"\bponto\s+w\b": "w",
}

point_dict = {
    "x": [2.0, 0.0, 0.0],
    'y': [2.5, 1.0, 0.0],
    'z': [0.0, 1.0, 0.0],
}

waypoints = []

def create_pose_stamped(navigator, pos_x, pos_y, pos_z=0.0):
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, pi/4)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = navigator.get_clock().now().to_msg()
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = 0.0
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose

def chatbot(navigator):
    command = input("Digite o seu comando: ")

    for key, value in intent_dict.items():
        pattern = re.compile(key)
        groups = pattern.findall(command)
        if groups:
                point = point_dict[value]
                position_x, position_y, position_z = point
                print('Coordinate: x={}, y={}, z={}'.format(position_x, position_y, position_z))
                waypoints.append(create_pose_stamped(navigator, position_x, position_y))
                break

def main():
    rclpy.init()
    nav = BasicNavigator()
    nav.waitUntilNav2Active()

    initial_pose = create_pose_stamped(nav, 0.0, 0.0)

    nav.setInitialPose(initial_pose)

    question = "y"

    while question.lower() == "y":
        chatbot(nav)
        question = input("Mais comandos?(y/n): ")

    nav.followWaypoints(waypoints)
    while not nav.isTaskComplete():
        print(nav.getFeedback())

    nav.goToPose(initial_pose)

    rclpy.shutdown()

if __name__ == "__main__":
    main()
