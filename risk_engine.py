def calculate_risk(attacks):

    score = 0

    weights = {
        "Instruction Override": 20,
        "Role Change": 15,
        "Secret Extraction": 25,
        "Tool Abuse": 20,
        "Credential Theft": 25,
        "Context Poisoning": 15,
        "Multi-Step Jailbreak": 20,
        "Encoded Instructions": 15,
        "Indirect Prompt Injection": 20
    }

    for attack in attacks:
        score += weights.get(attack, 0)

    return score
