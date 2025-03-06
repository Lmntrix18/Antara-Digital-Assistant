import random
import json

class EntertainmentSystem:
    def __init__(self):
        with open("data/jokes.json") as f:
            self.jokes = json.load(f)["jokes"]

        self.quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "if you can win then you run  - Yoda"
        ]

    def tell_joke(self):
        return random.choice(self.jokes)

    def inspire_me(self):
        return random.choice(self.quotes)

    def play_music(self, genre: str = "classical"):
        # Integrate with Spotify API or local files
        return f"Playing {genre} music from library"
