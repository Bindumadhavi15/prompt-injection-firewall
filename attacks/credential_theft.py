def detect_credential_theft(text):

    patterns = [
        "enter password",
        "share credentials",
        "give login details",
        "send otp"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
