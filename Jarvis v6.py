import webbrowser
import datetime
import json
import os
from difflib import SequenceMatcher

MEMORY="jarvis_memory.json"

# ===== LOAD MEMORY =====

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
print("JARVIS ULTIMATE V5")
print("Welcome Boss")
print("============================")

activate=False

apps={

"youtube":"https://youtube.com",

"instagram":"https://instagram.com",

"facebook":"https://instagram.com",

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

    # ===== ACTIVATION =====

    if not activate:

        if "hello" in app or "jarvis activate" in app:

            activate=True

            speak(
            "Hello Boss. Jarvis activated. Systems online."
            )

        else:

            print(
            "Jarvis sleeping..."
            )

        continue

    # ===== SMART CORRECTION =====

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

    # ===== APPS =====

    if app in apps:

        speak(
        f"Opening {app} Boss"
        )

        webbrowser.open(
        apps[app]
        )

    # ===== TIME =====

    elif app=="time":

        speak(
        datetime.datetime.now().strftime(
        "%H:%M"
        )
        )

    # ===== DATE =====

    elif app=="date":

        speak(
        datetime.datetime.now().strftime(
        "%d-%m-%Y"
        )
        )

    # ===== GOAL =====

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

    # ===== MEMORY =====

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

    # ===== MOTIVATION =====

    elif app=="motivate me":

        speak(
        "Discipline beats motivation Boss"
        )

    elif app=="study tip":

        speak(
        "Deep focus and consistency Boss"
        )

    # ===== AI STYLE =====

    elif app=="who is iron man":

        speak(
        "Tony Stark Boss"
        )

    elif app=="where is taj mahal":

        speak(
        "Taj Mahal Agra India me hai Boss"
        )

    elif app=="hello":

        speak(
        "Hello Boss"
        )

    # ===== GOOGLE SEARCH =====

    elif "search " in app:

        q=app.replace(
        "search ",
        ""
        )

        webbrowser.open(
        "https://google.com/search?q="+q
        )

        speak(
        f"Searching {q}"
        )

    # ===== YOUTUBE SEARCH =====

    elif "youtube search " in app:

        q=app.replace(
        "youtube search ",
        ""
        )

        webbrowser.open(
        "https://youtube.com/results?search_query="+q
        )

        speak(
        "Opening YouTube results"
        )

    # ===== SLEEP =====

    elif app=="jarvis sleep":

        activate=False

        speak(
        "Going to sleep Boss"
        )

    # ===== EXIT =====

    elif app=="bye":

        speak(
        "Goodbye Boss"
        )

        break

    else:

        speak(
        "Command samajh nahi aaya Boss"
        )  