import os
import sys
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound


def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)

    with audio_file as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language='pt-BR')
        return text
    except sr.UnknownValueError:
        return "Não foi possível reconhecer a fala."
    except sr.RequestError:
        return "Erro na requisição ao serviço de reconhecimento de fala."


def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, src='pt', dest='en')
    return translation.text


def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("desabafo.mp3")
    playsound.playsound("desabafo.mp3")
    os.remove("desabafo.mp3")


def transcribe_translate_speak(audio_path):
    recognized_text = transcribe_audio(audio_path)

    if recognized_text:
        print("Texto reconhecido:", recognized_text)
        translated_text = translate_text(recognized_text)
        print("Texto traduzido:", translated_text)
        speak_text(translated_text)
    else:
        print("Não foi possível reconhecer a fala no arquivo fornecido.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python nome_do_arquivo.py caminho_para_o_arquivo_de_audio")
    else:
        audio_file_path = sys.argv[1]
        transcribe_translate_speak(audio_file_path)
