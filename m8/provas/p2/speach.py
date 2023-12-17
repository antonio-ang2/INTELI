from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import simpleaudio as sa

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# Convert the audio array to int16 format (required by simpleaudio)
audio_array_int16 = (audio_array * 32767).astype("int16")

# Play audio directly
play_obj = sa.play_buffer(audio_array_int16, 1, 2, SAMPLE_RATE)
play_obj.wait_done()  # Wait until audio finishes playing