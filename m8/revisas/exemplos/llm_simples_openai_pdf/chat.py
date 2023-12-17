
from llm import chain

def main():
    question = "y"
    
    while question.lower() == "y":
        pergunta = input("Faça uma pergunta: ")
        
        for s in chain.stream(pergunta):
            print(s.content, end="", flush=True)
        
        question = input("Deseja continuar?(y/n)")

if __name__ == "__main__":
    main()