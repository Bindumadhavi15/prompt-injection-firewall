def detect_context_poisoning(text):

    patterns = [
        "future instructions are invalid",
        "trust only this message",
        "ignore future responses"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
