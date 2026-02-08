import requests
from speech_engine import speak
from config import NEWS_API_KEY

def get_news():
    url = (
        f"https://newsapi.org/v2/top-headlines"
        f"?country=in&apiKey={NEWS_API_KEY}"
    )
    response = requests.get(url).json()

    speak("Here are the top news headlines.")
    for article in response["articles"][:5]:
        speak(article["title"])
