import webbrowser
import datetime
import json
import os

MEMORY="memory.json"

if os.path.exists(MEMORY):

    with open(MEMORY,"r") as f:

        data=json.load(f)

else:

    data={}

def save():

    with open(MEMORY,"w") as f:

        json.dump(data,f)

print("===== JARVIS APP CONTROL =====")
print("Jarvis: Welcome Boss")

apps={

"youtube":"https://youtube.com",

"whatsapp":"https://wa.me",

"instagram":"https://instagram.com",

"telegram":"https://telegram.org",

"chatgpt":"https://chatgpt.com"

}

while True:

    app=input(
    "Boss: "
    ).lower()

    if app in apps:

        print(
        "Jarvis: Opening",
        app
        )

        webbrowser.open(
        apps[app]
        )

    elif "time" in app:

        t=datetime.datetime.now().strftime(
        "%H:%M"
        )

        print(
        "Jarvis: Boss current time:",
        t
        )

    elif "date" in app:

        d=datetime.datetime.now().strftime(
        "%d-%m-%Y"
        )

        print(
        "Jarvis: Boss today's date:",
        d
        )

    elif "motivate me" in app:

        print(
        "Jarvis: Boss, discipline beats motivation."
        )

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

    elif app=="bye":

        print(
        "Jarvis: Goodbye Boss"
        )

        break

    else:

        print(
        "Jarvis: Command nahi samjha Boss"
        )