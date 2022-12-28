
#!/usr/bin/env python

import os
import time
import dotenv
dotenv.load_dotenv()
import openai
import speech_recognition as sr
import cozmo
from gtts import gTTS
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

# TODO: should append context of conversation


response = ask(prompt)
print(response)

def cozmo_program(robot: cozmo.robot.Robot):
    r = sr.Recognizer()

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
        robot.say_text(response).wait_for_completed()

cozmo.run_program(cozmo_program)


