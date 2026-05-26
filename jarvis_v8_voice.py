import webbrowser
import datetime
import os
from gtts import gTTS

print("========== JARVIS V8 ==========")
print("Welcome Boss")
print("===============================")

activate=False

apps={

"youtube":"https://youtube.com",
"instagram":"https://instagram.com",
"google":"https://google.com",
"chatgpt":"https://chatgpt.com"

}

def speak(text):

    print("Jarvis:",text)

    try:

        voice=gTTS(
        text=text,
        lang="en"
        )

        voice.save(
        "jarvis.mp3"
        )

        os.system(
        "xdg-open jarvis.mp3"
        )

    except:

        print(
        "Voice unavailable Boss"
        )


while True:

    app=input(
    "Boss: "
    ).lower()


    if activate==False:

        if app=="hello" or app=="jarvis activate":

            activate=True

            speak(
            "Hello Boss. Jarvis systems online."
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
        datetime.datetime.now().strftime(
        "%H:%M"
        )
        )


    elif app=="date":

        speak(
        datetime.datetime.now().strftime(
        "%d-%m-%Y"
        )
        )


    elif app=="mission":

        speak(
        "Boss today's mission. Study and improve."
        )


    elif app=="weather":

        speak(
        "Opening weather"
        )

        webbrowser.open(
        "https://google.com/search?q=weather"
        )


    elif app=="news":

        speak(
        "Opening latest news"
        )

        webbrowser.open(
        "https://news.google.com"
        )


    elif app=="who created you":

        speak(
        "Boss, you are building me."
        )


    elif app=="where is taj mahal":

        speak(
        "Taj Mahal is in Agra India Boss"
        )


    elif app=="jarvis sleep":

        activate=False

        speak(
        "Going to sleep Boss"
        )


    elif app=="bye":

        speak(
        "Goodbye Boss"
        )

        break


    else:

        speak(
        "Command samajh nahi aaya Boss"
        )