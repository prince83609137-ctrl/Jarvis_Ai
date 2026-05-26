import webbrowser
import datetime
import json
import os
from difflib import SequenceMatcher

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

def speak(text):

    print("Jarvis:",text)

print("============================")
print("JARVIS V6")
print("Welcome Boss")
print("============================")

activate=False

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
"battery",
"mission",
"open camera",
"motivate me",
"study tip",
"remember",
"what do you remember",
"my goal is",
"what is my goal",
"who is iron man",
"where is taj mahal",
"hello",
"jarvis activate",
"jarvis sleep",
"bye"

]

while True:

    app=input(
    "Boss: "
    ).lower()

    # activation

    if not activate:

        if "hello" in app or "jarvis activate" in app:

            activate=True

            speak(
            "Hello Boss. Systems online."
            )

        else:

            print(
            "Jarvis sleeping..."
            )

        continue

    # smart correction

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

    elif app=="battery":

        speak(
        "Boss battery feature coming online"
        )

    elif app=="open camera":

        speak(
        "Opening camera Boss"
        )

        webbrowser.open(
        "https://google.com/search?q=camera"
        )

    elif app=="mission":

        speak(
        "Boss today's mission: Study, train and improve."
        )

    elif app=="my goal is":

        goal=input(
        "Goal: "
        )

        data["goal"]=goal

        save()

        speak(
        "Goal saved Boss"
        )

    elif app=="what is my goal":

        speak(
        data.get(
        "goal",
        "Goal nahi mila Boss"
        )
        )

    elif app=="remember":

        x=input(
        "Kya yaad rakhu Boss: "
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