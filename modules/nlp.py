import re
from typing import Dict, Literal

IntentType = Literal["weather", "news", "joke", "unknown"]

class NLPEngine:
    """Regex-based intent classifier with type safety"""
    
    PATTERNS: Dict[IntentType, str] = {
        "weather": r"(temperature|weather|forecast)",
        "news": r"\b(news|headlines)\b",
        "joke": r"\b(joke|funny)\b"
    }

    def classify_intent(self, text: str) -> IntentType:
        """Classify user input into predefined intents"""
        text_lower = text.lower()
        for intent, pattern in self.PATTERNS.items():
            if re.search(pattern, text_lower):
                return intent
        return "unknown"
