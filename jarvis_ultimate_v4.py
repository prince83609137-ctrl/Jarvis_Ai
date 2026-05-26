import webbrowser
import datetime
import json
import os
from difflib import SequenceMatcher

MEMORY="jarvis_memory.json"

# MEMORY LOAD

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

print("================================")
print("JARVIS ULTIMATE V4 ACTIVATED")
print("Welcome Boss")
print("Systems Online")
print("================================")

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

    # OPEN APPS

    if app in apps:

        print(
        "Jarvis: Opening",
        app
        )

        webbrowser.open(
        apps[app]
        )

    # TIME

    elif app=="time":

        print(
        "Jarvis:",
        datetime.datetime.now().strftime(
        "%H:%M"
        )
        )

    # DATE

    elif app=="date":

        print(
        "Jarvis:",
        datetime.datetime.now().strftime(
        "%d-%m-%Y"
        )
        )

    # GOAL SAVE

    elif "my goal is" in app:

        goal=input(
        "Jarvis: Goal batao Boss: "
        )

        data["goal"]=goal

        save()

        print(
        "Jarvis: Goal save ho gaya Boss"
        )

    elif "what is my goal" in app:

        print(
        "Jarvis:",
        data.get(
        "goal",
        "Goal nahi mila Boss"
        )
        )

    # MEMORY

    elif app=="remember":

        x=input(
        "Jarvis: Kya yaad rakhu Boss: "
        )

        data["memory"]=x

        save()

        print(
        "Jarvis: Yaad rakh liya Boss"
        )

    elif app=="what do you remember":

        print(
        "Jarvis:",
        data.get(
        "memory",
        "Kuch yaad nahi Boss"
        )
        )

    # MOTIVATION

    elif app=="motivate me":

        print(
        "Jarvis: Boss, discipline beats motivation."
        )

    elif app=="study tip":

        print(
        "Jarvis: Boss, deep focus + consistency."
        )

    # AI STYLE REPLIES

    elif app=="who is iron man":

        print(
        "Jarvis: Boss, Iron Man is Tony Stark."
        )

    elif app=="where is taj mahal":

        print(
        "Jarvis: Boss, Taj Mahal Agra India me hai."
        )

    elif app=="hello":

        print(
        "Jarvis: Hello Boss. Systems online."
        )

    # GOOGLE SEARCH

    elif "search " in app:

        q=app.replace(
        "search ",
        ""
        )

        print(
        "Jarvis: Searching",
        q
        )

        webbrowser.open(
        "https://google.com/search?q="+q
        )

    # YOUTUBE SEARCH

    elif "youtube search " in app:

        q=app.replace(
        "youtube search ",
        ""
        )

        print(
        "Jarvis: Opening YouTube results"
        )

        webbrowser.open(
        "https://youtube.com/results?search_query="+q
        )

    elif app=="bye":

        print(
        "Jarvis: Goodbye Boss"
        )

        break

    else:

        print(
        "Jarvis: Command samajh nahi aaya Boss"
        )