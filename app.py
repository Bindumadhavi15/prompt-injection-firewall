from agents.firewall import check_prompt

print("=== Prompt Injection Firewall ===")

user_prompt = input("Enter a prompt: ")

result = check_prompt(user_prompt)

print("\nResult:")
print("Status:", result["status"])
print("Message:", result["message"])
