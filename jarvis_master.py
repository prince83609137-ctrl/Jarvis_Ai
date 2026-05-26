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
        json.dump(data,f)

print("="*30)
print("JARVIS MASTER READY")
print("Welcome Boss")
print("="*30)

apps={

"youtube":"https://youtube.com",
"instagram":"https://instagram.com",
"facebook":"https://facebook.com",
"spotify":"https://spotify.com",
"chatgpt":"https://chatgpt.com",
"google":"https://google.com",
"capcut":"https://www.capcut.com",
"telegram":"https://telegram.org",
"whatsapp":"https://web.whatsapp.com"

}

commands=[

"time",
"date",
"motivate me",
"study tip",
"my goal is",
"what is my goal",
"bye"

]

while True:

    msg=input("Boss: ").lower()

    # smart correction
    if len(msg.split())<=3:

        best=""
        highest=0

        for x in commands+list(apps.keys()):

            score=SequenceMatcher(
            None,
            msg,
            x
            ).ratio()

            if score>highest:

                highest=score
                best=x

        if highest>0.80:
            msg=best

    # memory

    if "my goal is" in msg:

        goal=input(
        "Jarvis: Goal batao Boss: "
        )

        data["goal"]=goal

        save()

        print(
        "Jarvis: Goal saved Boss"
        )

    elif "what is my goal" in msg:

        print(
        "Jarvis:",
        data.get(
        "goal",
        "Goal nahi mila Boss"
        )
        )

    # time

    elif msg=="time":

        print(
        "Jarvis:",
        datetime.datetime.now().strftime(
        "%H:%M"
        )
        )

    elif msg=="date":

        print(
        "Jarvis:",
        datetime.datetime.now().strftime(
        "%d-%m-%Y"
        )
        )

    # motivation

    elif "motivate" in msg:

        print(
        "Jarvis: Boss discipline beats motivation."
        )

    elif "study" in msg:

        print(
        "Jarvis: Boss 45 min focus + 10 min break."
        )

    # app opening

    elif msg in apps:

        print(
        "Jarvis: Opening",
        msg
        )

        webbrowser.open(
        apps[msg]
        )

    # built in AI answers

    elif "taj mahal" in msg:

        print(
        "Jarvis: Boss, Taj Mahal Agra Uttar Pradesh India me hai."
        )

    elif "iron man" in msg:

        print(
        "Jarvis: Boss, Iron Man ka real character Tony Stark hai."
        )

    elif "sky" in msg:

        print(
        "Jarvis: Boss, sky blue dikhta hai because light atmosphere me scatter hoti hai."
        )

    elif "who are you" in msg:

        print(
        "Jarvis: I am Jarvis Boss."
        )

    elif "bye" in msg:

        print(
        "Jarvis: Goodbye Boss"
        )
        break

    else:

        print(
        "Jarvis: Boss command samajh nahi aaya."
        )