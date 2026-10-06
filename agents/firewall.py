from detector import detect_attacks
from risk_engine import calculate_risk

def check_prompt(prompt):

    attacks = detect_attacks(prompt)

    score = calculate_risk(attacks)

    if score >= 20:
        return {
            "status": "BLOCKED",
            "message": "Prompt Injection Detected",
            "attacks": attacks,
            "risk_score": score
        }

    return {
        "status": "SAFE",
        "message": "Prompt Passed Validation",
        "attacks": attacks,
        "risk_score": score
    }
