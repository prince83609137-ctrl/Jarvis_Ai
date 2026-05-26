from gtts import gTTS
from playsound import playsound

voice = gTTS("Hello Boss, Jarvis ready hai", lang="en")

voice.save("jarvis.mp3")

playsound("jarvis.mp3")