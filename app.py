
#!/usr/bin/env python

import os
import time
import dotenv
dotenv.load_dotenv()
import openai
import speech_recognition as sr
import pycozmo
import pyttsx3
from pydub import AudioSegment

openai.api_key = os.getenv('OPENAI_API_KEY')

model_engine = "text-davinci-003"
prompt = "Pretend you are an artificial intelligence running inside a cozmo robot. I will chat with you."

# Generate a response
def ask(prompt):
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        top_p=1,
        temperature=0.7,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text

r = sr.Recognizer()
tts = pyttsx3.init()
tts.setProperty('rate', 150)    # Speed percent
tts.setProperty('volume', 0.9)  # Volume 0-1

# TODO: should append context of conversation
with pycozmo.connect() as cli:
    response = ask(prompt)
    print(response)

    while 1:
        # get some input
        speech = sr.Microphone(device_index=2)
        with speech as source:
            print("say something!…")
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            recog = r.recognize_google(audio, language = 'en-US')
            print("You said: " + recog)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            continue

        response = ask(recog)

        print("the response from GPT was ", response)

        tts.save_to_file(response, 'tmp.mp3')
        tts.runAndWait()

        time.sleep(2)

        sound = AudioSegment.from_mp3('tmp.mp3')
        sound.export('out.wav', format="wav")

        cli.play_audio("out.wav")
        cli.wait_for(pycozmo.event.EvtAudioCompleted)