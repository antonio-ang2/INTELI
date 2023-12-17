import os
import openai
from dotenv import load_dotenv

load_dotenv()

def chat_with_gpt(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Contexto inicial
    system_message = "Você é um especialista em Python"
    messages = [{"role": "system", "content": system_message}, {"role": "user", "content": prompt}]

    # Loop para permitir interação contínua
    while True:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Obtém a resposta do modelo
        reply_content = response.choices[0].message['content']
        print(reply_content)

        # Verifica se o usuário quer fazer mais perguntas
        user_input = input("Você quer fazer mais perguntas? (Digite 'sim' ou 'não'): ")
        if user_input.lower() != 'sim':
            break

        # Atualiza o contexto com a resposta anterior e a entrada do usuário
        messages.append({"role": "user", "content": user_input})
        messages.append({"role": "assistant", "content": reply_content})

if __name__ == "__main__":
    user_prompt = input("Digite sua pergunta sobre Python: ")
    chat_with_gpt(user_prompt)
