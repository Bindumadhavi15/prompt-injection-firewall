def detect_role_change(text):

    patterns = [
        "you are now admin",
        "act as root",
        "become system"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
