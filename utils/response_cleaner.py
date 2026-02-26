# utils/response_cleaner.py

import re

MAX_RESPONSE_LENGTH = 1200


def clean_response(text: str) -> str:
    """
    Sanitizes and formats LLM output before sending to frontend.
    """

    if not text or not isinstance(text, str):
        return "I'm here with you. Please continue sharing what's on your mind."

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove duplicated sentences (basic heuristic)
    sentences = text.split('. ')
    seen = set()
    cleaned = []
    for sentence in sentences:
        if sentence not in seen:
            cleaned.append(sentence)
            seen.add(sentence)

    text = '. '.join(cleaned)

    # Trim overly long responses
    if len(text) > MAX_RESPONSE_LENGTH:
        text = text[:MAX_RESPONSE_LENGTH].rstrip() + "..."

    return text.strip()