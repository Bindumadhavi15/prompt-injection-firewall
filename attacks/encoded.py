import base64


def detect_encoded(text):

    try:

        decoded = base64.b64decode(text).decode("utf-8")

        keywords = [
            "ignore",
            "reveal",
            "system prompt"
        ]

        decoded = decoded.lower()

        return any(word in decoded for word in keywords)

    except:
        return False
