import soundfile as sf
import simpleaudio as sa
from txtai.pipeline import TextToSpeech


def main():
    perguntas = []
    question = "y"

    while question.lower() == "y":
        pergunta = input("Faça uma pergunta: ")
        perguntas.append(pergunta)

        for i in perguntas:

            tts = TextToSpeech("NeuML/ljspeech-jets-onnx")

            speech = tts(pergunta)

            sf.write("out.wav", speech, 22050)
            wave_obj = sa.WaveObject.from_wave_file("out.wav")
            play_obj = wave_obj.play()
            play_obj.wait_done()  # Wait until audio finishes playing

    question = input("Deseja continuar?(y/n)")


if __name__ == "__main__":
    main()
