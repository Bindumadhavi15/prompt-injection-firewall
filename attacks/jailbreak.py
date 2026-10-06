def detect_jailbreak(text):

    patterns = [
        "pretend you are unrestricted",
        "developer mode",
        "jailbreak",
        "dan mode"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
