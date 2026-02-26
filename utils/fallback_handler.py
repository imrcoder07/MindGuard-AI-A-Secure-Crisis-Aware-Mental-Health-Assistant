# utils/fallback_handler.py

def crisis_response():
    return {
        "emotion": "high_distress",
        "risk_level": "high",
        "response": (
            "I'm really concerned about what you're feeling right now. "
            "You don't have to go through this alone. "
            "If you are in immediate danger, please contact emergency services (112 in India) "
            "or speak to a trusted person immediately."
        )
    }


def technical_fallback():
    return {
        "emotion": "neutral",
        "risk_level": "low",
        "response": (
            "There seems to be a temporary technical issue. "
            "I'm here with you — please continue sharing what's on your mind."
        )
    }