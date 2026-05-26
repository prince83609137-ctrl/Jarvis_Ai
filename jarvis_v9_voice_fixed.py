import webbrowser
import datetime
import os
from gtts import gTTS

print("========== JARVIS V9 ==========")
print("Welcome Boss")

activate=False

apps={

"youtube":"https://youtube.com",
"google":"https://google.com",
"chatgpt":"https://chatgpt.com"

}

def speak(text):

    print("Jarvis:",text)

    try:

        tts=gTTS(
        text=text,
        lang="en"
        )

        tts.save(
        "/sdcard/jarvis.mp3"
        )

        os.system(
        'am start -a android.intent.action.VIEW -d file:///sdcard/jarvis.mp3 -t audio/mp3'
        )

    except Exception as e:

        print(
        "Voice error:",
        e
        )

while True:

    app=input(
    "Boss: "
    ).lower()

    if activate==False:

        if app=="hello":

            activate=True

            speak(
            "Hello Boss. Jarvis online."
            )

        else:

            print(
            "Jarvis sleeping..."
            )

        continue


    if app in apps:

        speak(
        f"Opening {app}"
        )

        webbrowser.open(
        apps[app]
        )

    elif app=="time":

        speak(
        datetime.datetime.now().strftime("%H:%M")
        )

    elif app=="weather":

        speak(
        "Opening weather"
        )

        webbrowser.open(
        "https://google.com/search?q=weather"
        )

    elif app=="bye":

        speak(
        "Goodbye Boss"
        )

        break