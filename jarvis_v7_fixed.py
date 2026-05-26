import webbrowser
import datetime

print("========== JARVIS V7 ==========")
print("Welcome Boss")
print("===============================")

activate=False

apps={

"youtube":"https://youtube.com",
"instagram":"https://instagram.com",
"google":"https://google.com",
"chatgpt":"https://chatgpt.com"

}

while True:

    app=input("Boss: ").lower()

    if activate==False:

        if app=="hello" or app=="jarvis activate":

            activate=True

            print("Jarvis: Hello Boss. Systems online.")

        else:

            print("Jarvis sleeping...")

        continue


    if app in apps:

        print("Jarvis: Opening",app)

        webbrowser.open(
        apps[app]
        )


    elif app=="time":

        print(
        "Jarvis:",
        datetime.datetime.now().strftime("%H:%M")
        )


    elif app=="date":

        print(
        "Jarvis:",
        datetime.datetime.now().strftime("%d-%m-%Y")
        )


    elif app=="mission":

        print(
        "Jarvis: Boss today's mission: Study and improve."
        )


    elif app=="weather":

        print(
        "Jarvis: Opening weather"
        )

        webbrowser.open(
        "https://google.com/search?q=weather"
        )


    elif app=="news":

        print(
        "Jarvis: Opening latest news"
        )

        webbrowser.open(
        "https://news.google.com"
        )


    elif app=="who created you":

        print(
        "Jarvis: Boss, you are building me."
        )


    elif app=="where is taj mahal":

        print(
        "Jarvis: Taj Mahal Agra India me hai Boss"
        )


    elif app=="jarvis sleep":

        activate=False

        print(
        "Jarvis: Going to sleep Boss"
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