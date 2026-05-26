import json
import os
import datetime
import webbrowser
from difflib import SequenceMatcher

MEMORY="memory.json"

if os.path.exists(MEMORY):

    with open(MEMORY,"r") as f:
        data=json.load(f)

else:

    data={}

def save():

    with open(MEMORY,"w") as f:
        json.dump(data,f)

print("================================")
print("===== JARVIS ULTIMATE AI =====")
print("===== Welcome Boss =====")
print("================================")

apps={

"youtube":"https://youtube.com",
"google":"https://google.com",
"instagram":"https://instagram.com",
"facebook":"https://facebook.com",
"spotify":"https://spotify.com",
"chatgpt":"https://chatgpt.com",
"free fire":"https://ff.garena.com",
"free fire max":"https://ff.garena.com",
"capcut":"https://www.capcut.com",
"phonepe":"https://phonepe.com",
"telegram":"https://telegram.org",
"flipkart":"https://flipkart.com"

}

dictionary={

"ai":"Artificial Intelligence",
"python":"Programming language",
"success":"Achieving goals",
"discipline":"Self control and consistency",
"motivation":"Reason to take action"

}

commands=[

"hello",
"how are you",
"my goal is",
"what is my goal",
"my favorite subject is",
"what is my favorite subject",
"time",
"date",
"motivate me",
"study tip",
"meaning",
"who am i",
"bye"

]

while True:

    msg=input(
    "Boss: "
    ).lower()

    # SMART AI SPELL CORRECTION

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

    # MEMORY

    if "my goal is" in msg:

        goal=input(
        "Jarvis: Goal bataiye Boss: "
        )

        data["goal"]=goal

        save()

        print(
        "Jarvis: Goal yaad rakh liya Boss"
        )

    elif "what is my goal" in msg:

        print(
        "Jarvis:",
        data.get(
        "goal",
        "Goal nahi mila Boss"
        )
        )

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
        "Subject nahi mila Boss"
        )
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
        "Jarvis: Boss time:",
        t
        )

    elif "date" in msg:

        d=datetime.datetime.now().strftime(
        "%d-%m-%Y"
        )

        print(
        "Jarvis: Boss date:",
        d
        )

    elif "motivate me" in msg:

        print(
        "Jarvis: Boss, discipline motivation se bada hota hai."
        )

    elif "study tip" in msg:

        print(
        "Jarvis: Boss, 45 min focus + 10 min break."
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
        "Boss meaning nahi mila"
        )
        )

    elif msg in apps:

        print(
        "Jarvis: Boss opening",
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