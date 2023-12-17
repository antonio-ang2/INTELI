#! /bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class OutputNode(Node):
    def __init__(self):
        super().__init__('output_node')
        self.subscription_ = self.create_subscription(
            msg_type=String,
            topic="/chatbot",
            callback=self.listener_callback,
            qos_profile=10
        )

        self.get_logger().info("Ouvindo ao /chatbot")

    def listener_callback(self, msg):

        print(f"[RESPONSE] [CHATBOT] {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    output_node = OutputNode()

    rclpy.spin(output_node)

    output_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
