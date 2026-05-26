import json
import os
import datetime
import webbrowser
from difflib import SequenceMatcher

MEMORY="jarvis_memory.json"

# Load Memory
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

print("===================================")
print(" JARVIS ULTIMATE MASTER AI ")
print(" Welcome Boss ")
print("===================================")

apps={

"youtube":"https://youtube.com",

"google":"https://google.com",

"instagram":"https://instagram.com",

"facebook":"https://facebook.com",

"spotify":"https://spotify.com",

"chatgpt":"https://chatgpt.com",

"free fire":"https://ff.garena.com",

"capcut":"https://www.capcut.com",

"telegram":"https://telegram.org",

"phonepe":"https://phonepe.com",

"flipkart":"https://flipkart.com"

}

dictionary={

"ai":"Artificial Intelligence",

"python":"Programming Language",

"discipline":"Self control and consistency",

"success":"Achieving goals",

"motivation":"Reason to take action"

}

commands=[

"hello",
"how are you",

"my goal is",
"what is my goal",

"my favorite subject is",
"what is my favorite subject",

"remember this",

"who am i",

"time",
"date",

"motivate me",

"study tip",

"meaning",

"bye"

]

while True:

    msg=input(
    "Boss: "
    ).lower()

    # AI STYLE MATCHING

    best=""
    highest=0

    for cmd in commands+list(apps.keys()):

        score=SequenceMatcher(
            None,
            msg,
            cmd
        ).ratio()

        if score>highest:

            highest=score

            best=cmd

    if highest>0.45:

        print(
        "Jarvis: Boss samjha:",
        best
        )

        msg=best

    # GOAL MEMORY

    if "my goal is" in msg:

        goal=input(
        "Jarvis: Goal bataiye Boss: "
        )

        data["goal"]=goal

        save()

        print(
        "Jarvis: Goal save kar liya Boss"
        )

    elif "what is my goal" in msg:

        print(
        "Jarvis:",
        data.get(
        "goal",
        "Goal nahi mila Boss"
        )
        )

    # SUBJECT MEMORY

    elif "my favorite subject is" in msg:

        subject=input(
        "Jarvis: Subject bataiye Boss: "
        )

        data["subject"]=subject

        save()

        print(
        "Jarvis: Subject yaad rakh liya Boss"
        )

    elif "what is my favorite subject" in msg:

        print(
        "Jarvis:",
        data.get(
        "subject",
        "Subject nahi mila"
        )
        )

    # NOTES

    elif "remember this" in msg:

        note=input(
        "Jarvis: Kya yaad rakhu Boss: "
        )

        data["note"]=note

        save()

        print(
        "Jarvis: Yaad rakh liya Boss"
        )

    elif "who am i" in msg:

        print(
        "Jarvis: Boss aap legend ho 😄"
        )

    elif "hello" in msg:

        print(
        "Jarvis: Hello Boss"
        )

    elif "how are you" in msg:

        print(
        "Jarvis: Main online hoon Boss"
        )

    elif "time" in msg:

        t=datetime.datetime.now().strftime(
        "%H:%M"
        )

        print(
        "Jarvis: Time:",
        t
        )

    elif "date" in msg:

        d=datetime.datetime.now().strftime(
        "%d-%m-%Y"
        )

        print(
        "Jarvis: Date:",
        d
        )

    elif "motivate me" in msg:

        print(
        "Jarvis: Boss, discipline motivation se bada hota hai."
        )

    elif "study tip" in msg:

        print(
        "Jarvis: Boss, deep focus + consistency."
        )

    elif msg.startswith(
    "meaning"
    ):

        word=input(
        "Word: "
        )

        print(
        "Jarvis:",
        dictionary.get(
        word,
        "Meaning nahi mila"
        )
        )

    elif msg in apps:

        print(
        "Jarvis: Opening",
        msg
        )

        webbrowser.open(
        apps[msg]
        )

    elif "bye" in msg:

        print(
        "Jarvis: Goodbye Boss"
        )

        break

    else:

        print(
        "Jarvis: Boss samjha nahi"
        )