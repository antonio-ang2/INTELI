import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import gradio as gr


class InputNode(Node):
    def __init__(self):
        super().__init__('input_node')
        self.publisher_ = self.create_publisher(
            msg_type=String,
            topic='/llm',
            qos_profile=10
        )

        self.get_logger().info('Estou pronto para receber perguntas...')

    def run(self):
        try:
            while rclpy.ok():
                user_input = input("Faça uma pergunta: ")
                if user_input.lower() == "exit":
                    break
                self.publish_command(user_input)
        except KeyboardInterrupt:
            pass

    def publish_command(self, command):
        msg = String()
        msg.data = command
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publicando '{command}'")


class ROSGradioInterface:
    def __init__(self):
        rclpy.init()  # Inicialize o ROS 2 aqui
        self.input_node = InputNode()
        # Permite que o ROS inicie antes do Gradio
        rclpy.spin_once(self.input_node, timeout_sec=0.1)

    def send_question_to_ros(self, question):
        self.input_node.publish_command(question)

    def generate_response(self, prompt, chat_history):
        print('Sending question to ROS...')
        self.send_question_to_ros(prompt)
        response = "Aguardando resposta do ROS..."
        chat_history.append((prompt, response))
        return "", chat_history


if __name__ == "__main__":
    ros_interface = ROSGradioInterface()

    with gr.Blocks() as demo:
        title = "ROS + Gradio Interface"
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.ClearButton([msg, chatbot])

        msg.submit(ros_interface.generate_response,
                   [msg, chatbot], [msg, chatbot])

    demo.launch()
