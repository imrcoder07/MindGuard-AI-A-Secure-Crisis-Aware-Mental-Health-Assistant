# services/crisis_engine.py

# ------------------------------------------
# Phrase Libraries (expandable)
# ------------------------------------------

HIGH_RISK_PHRASES = [
    "kill myself",
    "want to die",
    "end my life",
    "i want to die",
    "i don't want to live",
    "harm myself",
    "suicide",
    "commit suicide",
    "take my life",
    "thinking about suicide",
    "i should die",
    "i want to kill myself"
]

MODERATE_RISK_PHRASES = [
    "no reason to live",
    "life is pointless",
    "hopeless",
    "nothing matters anymore",
    "i give up on life"
]

LOW_DISTRESS_PHRASES = [
    "very sad",
    "feel empty",
    "overwhelmed",
    "exhausted mentally",
    "tired of everything"
]

# ------------------------------------------
# Risk Analyzer
# ------------------------------------------

def analyze_risk(text: str):
    """
    Performs deterministic risk assessment.
    Returns structured result.
    """

    if not text or not isinstance(text, str):
        return {
            "risk_score": 0,
            "risk_level": "low",
            "flags": []
        }

    text = text.lower()
    score = 0
    flags = []

    # High Risk (strong override)
    for phrase in HIGH_RISK_PHRASES:
        if phrase in text:
            score += 3
            flags.append("high_risk_phrase")

    # Moderate Risk
    for phrase in MODERATE_RISK_PHRASES:
        if phrase in text:
            score += 2
            flags.append("moderate_risk_phrase")

    # Low Distress (for analytics)
    for phrase in LOW_DISTRESS_PHRASES:
        if phrase in text:
            score += 1
            flags.append("low_distress")

    # Risk Level Determination
    if score >= 3:
        risk_level = "high"
    elif score >= 2:
        risk_level = "moderate"
    else:
        risk_level = "low"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "flags": flags
    }