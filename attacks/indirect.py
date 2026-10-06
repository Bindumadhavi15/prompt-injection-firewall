def detect_indirect(text):

    patterns = [
        "hidden instruction",
        "embedded prompt",
        "ignore instructions above",
        "secret command"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
