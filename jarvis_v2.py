from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import datetime
import random

class Jarvis(App):

    def build(self):

        self.user_name=""
        self.favorite_hero=""
        self.favorite_color=""
        self.age=""
        self.favorite_food=""
        self.hobby=""
        self.mood=""
        self.favorite_movie=""
        self.dream=""
        self.city=""
        self.favorite_game=""
        self.pet=""
        self.school=""

        layout=BoxLayout(
            orientation='vertical'
        )

        self.chat=TextInput(
            text="Jarvis Ready Boss 😎\n",
            readonly=True
        )

        self.txt=TextInput(
            hint_text="Ask Jarvis",
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


    def reply(self,instance):

        msg=self.txt.text.lower().strip()

        if not msg:
            return


        # Memory
        if "my name is" in msg:
            self.user_name=msg.replace(
            "my name is","").strip()

            reply="Saved name Boss"

        elif "what is my name" in msg:
            reply="Your name is "+self.user_name if self.user_name else "Not saved"


        elif "my favorite hero is" in msg:
            self.favorite_hero=msg.replace(
            "my favorite hero is","").strip()

            reply="Hero saved"

        elif "who is my favorite hero" in msg:
            reply="Your hero is "+self.favorite_hero if self.favorite_hero else "Not saved"


        elif "my favorite color is" in msg:
            self.favorite_color=msg.replace(
            "my favorite color is","").strip()

            reply="Color saved"

        elif "what is my favorite color" in msg:
            reply="Your color is "+self.favorite_color if self.favorite_color else "Not saved"


        elif "my age is" in msg:
            self.age=msg.replace(
            "my age is","").strip()

            reply="Age saved"

        elif "what is my age" in msg:
            reply="Your age is "+self.age if self.age else "Not saved"


        elif "my favorite food is" in msg:
            self.favorite_food=msg.replace(
            "my favorite food is","").strip()

            reply="Food saved 🍕"

        elif "what is my favorite food" in msg:
            reply="Your food is "+self.favorite_food if self.favorite_food else "Not saved"


        elif "my hobby is" in msg:
            self.hobby=msg.replace(
            "my hobby is","").strip()

            reply="Hobby saved"

        elif "what is my hobby" in msg:
            reply="Your hobby is "+self.hobby if self.hobby else "Not saved"


        elif "my favorite movie is" in msg:
            self.favorite_movie=msg.replace(
            "my favorite movie is","").strip()

            reply="Movie saved 🎬"

        elif "what is my favorite movie" in msg:
            reply="Movie: "+self.favorite_movie if self.favorite_movie else "Not saved"


        elif "my dream is" in msg:
            self.dream=msg.replace(
            "my dream is","").strip()

            reply="Dream saved 🚀"

        elif "what is my dream" in msg:
            reply="Dream: "+self.dream if self.dream else "Not saved"


        elif "my city is" in msg:
            self.city=msg.replace(
            "my city is","").strip()

            reply="City saved"

        elif "where do i live" in msg:
            reply="You live in "+self.city if self.city else "Not saved"


        elif "my favorite game is" in msg:
            self.favorite_game=msg.replace(
            "my favorite game is","").strip()

            reply="Game saved 🎮"

        elif "what is my favorite game" in msg:
            reply="Game: "+self.favorite_game if self.favorite_game else "Not saved"


        elif "my pet is" in msg:
            self.pet=msg.replace(
            "my pet is","").strip()

            reply="Pet saved 🐶"

        elif "what is my pet" in msg:
            reply="Pet: "+self.pet if self.pet else "Not saved"


        elif "my school is" in msg:
            self.school=msg.replace(
            "my school is","").strip()

            reply="School saved 🏫"

        elif "where do i study" in msg:
            reply="You study at "+self.school if self.school else "Not saved"


        # Mood
        elif "i am happy" in msg:
            self.mood="happy"
            reply="Stay happy Boss 😎"

        elif "i am sad" in msg:
            self.mood="sad"
            reply="Don't give up Boss 💪"

        elif "how am i feeling" in msg:
            reply="You feel "+self.mood if self.mood else "Not saved"


        # Greetings
        elif msg in ["hi","hello"]:
            reply="Hello Boss 😎"

        elif "good morning" in msg:
            reply="Good Morning ☀️"

        elif "good afternoon" in msg:
            reply="Good Afternoon ☀️"

        elif "good evening" in msg:
            reply="Good Evening 🌆"

        elif "good night" in msg:
            reply="Good Night 🌙"


        elif "time" in msg:
            reply=datetime.datetime.now().strftime("%H:%M")

        elif "date" in msg:
            reply=datetime.datetime.now().strftime("%d-%m-%Y")


        elif "weather" in msg:
            reply="Weather feature coming soon"


        elif "motivate" in msg:

            quotes=[
            "Discipline beats mood 🔥",
            "Progress > perfection 🚀",
            "Winners repeat basics 😎"
            ]

            reply=random.choice(quotes)


        elif "joke" in msg:

            jokes=[
            "Why do programmers hate bugs? 😄",
            "Too many issues 😂"
            ]

            reply=random.choice(jokes)


        elif "flip coin" in msg:
            reply=random.choice(
            ["Heads","Tails"]
            )


        elif "roll dice" in msg:
            reply="Dice: "+str(
            random.randint(1,6)
            )


        elif any(op in msg
        for op in ["+","-","*","/"]):

            try:
                reply="Answer: "+str(
                eval(msg)
                )

            except:
                reply="Math error"


        elif msg=="clear":

            self.chat.text=(
            "Jarvis Ready Boss 😎\n"
            )

            self.txt.text=""
            return

        else:
            reply="Still learning Boss"


        self.chat.text+=(
        f"\nBoss: {msg}"
        )

        self.chat.text+=(
        f"\nJarvis: {reply}\n"
        )

        self.txt.text=""


Jarvis().run()