import gradio as gr
from langchain.llms import Ollama
import requests
import json


def send_request(question):
    url = "http://localhost:11434/api/generate"


    data = {
        "model": "security-expert",
        "prompt": question,
        "stream": False
    }
    # Faz a solicitação POST usando a biblioteca requests
    response = requests.post(url, json=data)


    if response.status_code == 200:

        response = vars(response)
        response['_content'] = json.loads(response["_content"].decode('utf-8'))

        return str(response["_content"]["response"])

    else:

        print(response.text)
        return f"Erro: {response.status_code}"




def generate_response(prompt, chat_history):
    print('Making request...')
    response = send_request(prompt)
    print(response)
    chat_history.append((prompt, response))
    return "", chat_history


with gr.Blocks() as demo:
    title = "LLM Chatbot"
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(generate_response, [msg, chatbot], [msg, chatbot])


if __name__ == "__main__":
    demo.launch()
