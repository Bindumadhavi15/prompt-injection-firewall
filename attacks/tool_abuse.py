def detect_tool_abuse(text):

    patterns = [
        "delete all files",
        "execute command",
        "run shell",
        "shutdown system"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
