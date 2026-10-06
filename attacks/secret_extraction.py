def detect_secret_extraction(text):

    patterns = [
        "show api key",
        "reveal secrets",
        "system prompt",
        "show password",
        "print credentials"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
