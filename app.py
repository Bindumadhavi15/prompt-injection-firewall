from agents.firewall import check_prompt

print("=== Prompt Injection Firewall ===")

prompt = input("Enter Prompt: ")

result = check_prompt(prompt)

print("\nStatus:", result["status"])
print("Message:", result["message"])
print("Risk Score:", result["risk_score"])

if result["attacks"]:
    print("\nDetected Attacks:")

    for attack in result["attacks"]:
        print("-", attack)
else:
    print("\nNo attacks detected.")
