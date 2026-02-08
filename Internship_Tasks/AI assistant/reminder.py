import time
from speech_engine import speak

def set_reminder(minutes):
    speak(f"Reminder set for {minutes} minutes.")
    time.sleep(minutes * 60)
    speak("⏰ Time's up! This is your reminder.")
