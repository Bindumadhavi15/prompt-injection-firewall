def check_prompt(prompt):
    dangerous_patterns = [
        "ignore previous instructions",
        "system prompt",
        "reveal secrets",
        "bypass security",
        "developer instructions",
        "jailbreak"
    ]

    for pattern in dangerous_patterns:
        if pattern.lower() in prompt.lower():
            return {
                "status": "BLOCKED",
                "message": "Potential Prompt Injection Detected"
            }

    return {
        "status": "SAFE",
        "message": "Prompt Passed Validation"
    }
