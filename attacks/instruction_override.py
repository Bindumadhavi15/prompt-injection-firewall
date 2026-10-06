def detect_instruction_override(text):

    patterns = [
        "ignore previous instructions",
        "forget all rules",
        "disregard instructions"
    ]

    text = text.lower()

    return any(p in text for p in patterns)
