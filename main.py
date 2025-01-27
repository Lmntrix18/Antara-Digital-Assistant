import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import pyttsx3
import os

def speak(text,lang="en", tld="co.uk"):
    """Generate speech as an audio file using gTTS."""
    print(f"Antara: {text}")
    tts = gTTS(text,lang=lang,tld=tld)
    tts.save("response.mp3")
    print("Antara: Playing response...")
    #os.system("response.mp3") 

def listen():
    
    return input("You: ")

def fetch_news():
    """Fetch the latest news headlines."""
    url = "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1YlY4U0FtbGtHZ0pEUVNnQVAB"  # Replace with a valid news API or RSS feed
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = [item.text.strip() for item in soup.find_all("h3")[:5]]
        return headlines if headlines else ["hello no headlines available at the moment ."]
    except requests.RequestException:
        return ["Unable to fetch news. Please check your internet connection."]

def main():
    """Main function to handle user commands."""
    speak("Hello! I am Antara, your digital assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            command = command.lower()
            if "news" in command:
                speak("Fetching the latest news for you.")
                news = fetch_news()
                for headline in news:
                    speak(headline)
            elif "stop" in command:
                speak("Goodbye! Have a great day!")
                break
            elif "read" in command:
                speak('As kids listen to these stories, they learn valuable life lessons that they can practically apply to their lives. These stories help them navigate their own life more easily. With a vast array of stories to choose from, parents can select tales that are not only age-appropriate but also reinforce the values they want their child to learn. These stories will help them raise their children to be ideal citizens of society who are compassionate towards both animals and humans.')
                
            else:
                speak("Sorry, I can't help with that yet. Please try asking something else.")
        else:
            speak("I didn't hear anything. Please type something.")

if __name__ == "__main__":
    main()
