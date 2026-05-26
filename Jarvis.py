import json
import os
import datetime
import webbrowser
import random

from difflib import SequenceMatcher
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

MEMORY="jarvis_memory.json"

# ===== MEMORY LOAD =====

if os.path.exists(MEMORY):
    with open(MEMORY,"r") as f:
        data=json.load(f)
else:
    data={}


def save():
    with open(MEMORY,"w") as f:
        json.dump(data,f,indent=4)


class Jarvis(App):

    def build(self):

        self.activate=False

        self.apps={

        "youtube":"https://youtube.com",
        "google":"https://google.com",
        "instagram":"https://instagram.com",
        "facebook":"https://facebook.com",
        "spotify":"https://spotify.com",
        "chatgpt":"https://chatgpt.com",
        "telegram":"https://telegram.org",
        "whatsapp":"https://wa.me",
        "capcut":"https://www.capcut.com",
        "free fire":"https://ff.garena.com",
        "phonepe":"https://phonepe.com",
        "flipkart":"https://flipkart.com"

        }

        self.dictionary={

        "ai":"Artificial Intelligence",
        "python":"Programming language",
        "discipline":"Self control + consistency",
        "motivation":"Reason to act",
        "success":"Achieving goals"

        }


        self.commands=[

        "hello",
        "jarvis activate",
        "jarvis sleep",
        "time",
        "date",
        "motivate me",
        "study tip",

        "my goal is",
        "what is my goal",

        "remember this",
        "what do you remember",

        "my favorite subject is",
        "what is my favorite subject",

        "my name is",
        "what is my name",

        "my favorite hero is",
        "who is my favorite hero",

        "my favorite color is",
        "what is my favorite color",

        "my age is",
        "what is my age",

        "my favorite food is",
        "what is my favorite food",

        "my hobby is",
        "what is my hobby",

        "my favorite movie is",
        "what is my favorite movie",

        "my dream is",
        "what is my dream",

        "my city is",
        "where do i live",

        "my favorite game is",
        "what is my favorite game",

        "my pet is",
        "what is my pet",

        "my school is",
        "where do i study",

        "who am i",
        "who is iron man",
        "where is taj mahal",

        "flip coin",
        "roll dice",

        "joke",
        "clear",
        "bye"

        ]

        layout=BoxLayout(
        orientation="vertical"
        )


        self.chat=TextInput(

        text=
        "===================\n"
        "JARVIS ULTIMATE AI\n"
        "Welcome Boss 😎\n"
        "Type: jarvis activate\n"
        "===================\n",

        readonly=True

        )


        self.txt=TextInput(
        hint_text="Ask Jarvis Boss",
        multiline=False
        )

        self.txt.bind(
        on_text_validate=self.reply
        )

        btn=Button(text="Send")

        btn.bind(
        on_press=self.reply
        )

        layout.add_widget(self.chat)
        layout.add_widget(self.txt)
        layout.add_widget(btn)

        return layout



    def speak(self,text):

        self.chat.text+=(
        "\nJarvis: "+text+"\n"
        )



    def reply(self,instance):

        msg=self.txt.text.lower().strip()

        if not msg:
            return


        # SMART MATCH

        best=""
        highest=0

        for x in self.commands+list(self.apps.keys()):

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


        self.chat.text+=(
        "\nBoss: "+msg
        )


        # ACTIVATION

        if not self.activate:

            if "hello" in msg or \
            "jarvis activate" in msg:

                self.activate=True

                self.speak(
                "Hello Boss. Systems online."
                )

            else:

                self.speak(
                "Jarvis sleeping..."
                )

            self.txt.text=""
            return



        # OPEN APPS

        if msg in self.apps:

            webbrowser.open(
            self.apps[msg]
            )

            self.speak(
            "Opening "+msg
            )


        elif "my goal is" in msg:

            data["goal"]=msg.replace(
            "my goal is",""
            ).strip()

            save()

            self.speak(
            "Goal saved Boss"
            )


        elif "what is my goal" in msg:

            self.speak(
            data.get(
            "goal",
            "No goal saved"
            )
            )


        elif "remember this" in msg:

            data["note"]=msg.replace(
            "remember this",""
            ).strip()

            save()

            self.speak(
            "Saved Boss"
            )


        elif "what do you remember" in msg:

            self.speak(
            data.get(
            "note",
            "Nothing saved"
            )
            )


        elif "time"==msg:

            self.speak(
            datetime.datetime.now().strftime("%H:%M")
            )


        elif "date"==msg:

            self.speak(
            datetime.datetime.now().strftime("%d-%m-%Y")
            )


        elif "motivate" in msg:

            self.speak(

            random.choice([

            "Discipline beats mood 🔥",
            "Progress > perfection 🚀",
            "Winners repeat basics 😎"

            ])
            )


        elif "study tip" in msg:

            self.speak(
            "Deep focus + consistency"
            )


        elif msg.startswith("meaning"):

            word=msg.replace(
            "meaning",""
            ).strip()

            self.speak(
            self.dictionary.get(
            word,
            "Meaning not found"
            )
            )


        elif "search " in msg:

            q=msg.replace(
            "search ",
            ""
            )

            webbrowser.open(
            "https://google.com/search?q="+q
            )

            self.speak(
            "Searching "+q
            )


        elif "youtube search" in msg:

            q=msg.replace(
            "youtube search",
            ""
            )

            webbrowser.open(
            "https://youtube.com/results?search_query="+q
            )

            self.speak(
            "Opening YouTube"
            )


        elif any(
        x in msg
        for x in
        ["+","-","*","/"]
        ):

            try:

                self.speak(
                "Answer: "+
                str(eval(msg))
                )

            except:

                self.speak(
                "Math error"
                )


        elif "flip coin" in msg:

            self.speak(
            random.choice(
            ["Heads","Tails"]
            )
            )


        elif "roll dice" in msg:

            self.speak(
            str(
            random.randint(1,6)
            )
            )


        elif "joke" in msg:

            self.speak(
            random.choice([

            "Why programmers hate bugs 😂",

            "Too many issues 😆"

            ])
            )


        elif msg=="who is iron man":

            self.speak(
            "Tony Stark Boss"
            )


        elif msg=="where is taj mahal":

            self.speak(
            "Agra India Boss"
            )


        elif msg=="who am i":

            self.speak(
            "Boss aap legend ho 😎"
            )


        elif msg=="clear":

            self.chat.text=(

            "===================\n"
            "JARVIS ULTIMATE AI\n"
            "Welcome Boss 😎\n"
            "Type: jarvis activate\n"
            "===================\n"

            )

            return


        elif msg=="jarvis sleep":

            self.activate=False

            self.speak(
            "Going offline Boss"
            )


        elif msg=="bye":

            App.get_running_app().stop()


        else:

            self.speak(
            "Still learning Boss"
            )

        self.txt.text=""


Jarvis().run()
