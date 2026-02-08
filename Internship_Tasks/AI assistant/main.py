import datetime
from speech_engine import speak, listen
from reminder import set_reminder
from weather import get_weather
from news import get_news

def run_assistant():
    speak("Hello! I am your personal assistant.")

    while True:
        command = listen()

        if "reminder" in command:
            speak("In how many minutes?")
            mins = int(listen())
            set_reminder(mins)

        elif "weather" in command:
            speak("Which city?")
            city = listen()
            get_weather(city)

        elif "news" in command:
            get_news()

        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {now}")

        elif "exit" in command:
            speak("Goodbye!")
            break

        else:
            speak("Command not recognized.")

run_assistant()
