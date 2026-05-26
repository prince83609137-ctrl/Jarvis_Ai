import webbrowser
import datetime
import json
import os
from difflib import SequenceMatcher

# Voice (optional)
VOICE=False

try:
    import pyttsx3

    engine=pyttsx3.init()

    VOICE=True

except:
    VOICE=False


def speak(text):

    print("Jarvis:",text)

    if VOICE:

        engine.say(text)

        engine.runAndWait()


MEMORY="jarvis_memory.json"

if os.path.exists(MEMORY):

    with open(MEMORY,"r") as f:

        data=json.load(f)

else:

    data={}

def save():

    with open(MEMORY,"w") as f:

        json.dump(
        data,
        f,
        indent=4
        )

print("==========================")
print("JARVIS FINAL ULTIMATE")
print("Welcome Boss")
print("==========================")

apps={

"youtube":"https://youtube.com",

"instagram":"https://instagram.com",

"facebook":"https://facebook.com",

"spotify":"https://spotify.com",

"chatgpt":"https://chatgpt.com",

"telegram":"https://telegram.org",

"google":"https://google.com",

"whatsapp":"https://wa.me"

}

commands=[

"time",
"date",
"motivate me",
"study tip",
"my goal is",
"what is my goal",
"remember",
"what do you remember",
"who is iron man",
"where is taj mahal",
"hello",
"bye"

]

while True:

    app=input(
    "Boss: "
    ).lower()

    best=""
    highest=0

    for x in commands+list(apps.keys()):

        score=SequenceMatcher(
        None,
        app,
        x
        ).ratio()

        if score>highest:

            highest=score

            best=x

    if highest>0.80:

        app=best

    if app in apps:

        speak(
        f"Opening {app} Boss"
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

    elif "my goal is" in app:

        goal=input(
        "Goal: "
        )

        data["goal"]=goal

        save()

        speak(
        "Goal saved Boss"
        )

    elif "what is my goal" in app:

        speak(
        data.get(
        "goal",
        "Goal nahi mila Boss"
        )
        )

    elif app=="remember":

        x=input(
        "Kya yaad rakhu: "
        )

        data["memory"]=x

        save()

        speak(
        "Yaad rakh liya Boss"
        )

    elif app=="what do you remember":

        speak(
        data.get(
        "memory",
        "Kuch yaad nahi Boss"
        )
        )

    elif app=="motivate me":

        speak(
        "Discipline beats motivation Boss"
        )

    elif app=="study tip":

        speak(
        "Deep focus and consistency Boss"
        )

    elif app=="who is iron man":

        speak(
        "Tony Stark Boss"
        )

    elif app=="where is taj mahal":

        speak(
        "Taj Mahal Agra India me hai Boss"
        )

    elif "search " in app:

        q=app.replace(
        "search ",
        ""
        )

        speak(
        f"Searching {q}"
        )

        webbrowser.open(
        "https://google.com/search?q="+q
        )

    elif "youtube search " in app:

        q=app.replace(
        "youtube search ",
        ""
        )

        webbrowser.open(
        "https://youtube.com/results?search_query="+q
        )

    elif app=="hello":

        speak(
        "Hello Boss Systems online"
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