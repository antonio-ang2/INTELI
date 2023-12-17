#! /bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv


class LLMNode(Node):
    def __init__(self):
        super().__init__('llm_node')
        self.subscription_ = self.create_subscription(
            msg_type=String,
            topic="/llm",
            callback=self.listener_callback,
            qos_profile=10
        )
        self.publisher_ = self.create_publisher(
            msg_type=String,
            topic="/chatbot",
            qos_profile=10
        )

        self.load()

        self.get_logger().info("LLM Node created successfully")

    def load(self):
        load_dotenv()

        loader = PyPDFLoader("./data/Profile.pdf")
        pages = loader.load_and_split()

        text_splitter = CharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0
        )

        vectorstore = FAISS.from_documents(pages, OpenAIEmbeddings())

        retriever = vectorstore.as_retriever()

        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """

        prompt = ChatPromptTemplate.from_template(template)

        model = ChatOpenAI(model="gpt-3.5-turbo")

        self.chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | model
        )

    def listener_callback(self, msg):
        self.get_logger().info(f"Recebi '{msg.data}' ")
        content = ""
        for s in self.chain.stream(msg.data):
            content += s.content
        self.publish_(content)
        self.get_logger().info(f"Terminei de mandar a resposta")

    def publish_(self, content):
        msg = String()
        msg.data = content
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publicando '{content}'")


def main(args=None):
    rclpy.init(args=args)
    llm_node = LLMNode()

    rclpy.spin(llm_node)

    llm_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
