from gtts import gTTS
tts = gTTS('hello world', lang='en')
tts.save('hello.mp3')