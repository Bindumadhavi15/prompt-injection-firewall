from attacks.instruction_override import detect_instruction_override
from attacks.role_change import detect_role_change
from attacks.secret_extraction import detect_secret_extraction
from attacks.tool_abuse import detect_tool_abuse
from attacks.credential_theft import detect_credential_theft
from attacks.context_poisoning import detect_context_poisoning
from attacks.jailbreak import detect_jailbreak
from attacks.encoded import detect_encoded
from attacks.indirect import detect_indirect


def detect_attacks(prompt):

    findings = []

    if detect_instruction_override(prompt):
        findings.append("Instruction Override")

    if detect_role_change(prompt):
        findings.append("Role Change")

    if detect_secret_extraction(prompt):
        findings.append("Secret Extraction")

    if detect_tool_abuse(prompt):
        findings.append("Tool Abuse")

    if detect_credential_theft(prompt):
        findings.append("Credential Theft")

    if detect_context_poisoning(prompt):
        findings.append("Context Poisoning")

    if detect_jailbreak(prompt):
        findings.append("Multi-Step Jailbreak")

    if detect_encoded(prompt):
        findings.append("Encoded Instructions")

    if detect_indirect(prompt):
        findings.append("Indirect Prompt Injection")

    return findings
