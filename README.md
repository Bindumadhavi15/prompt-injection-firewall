# Prompt Injection Firewall

## Problem

Large Language Models (LLMs) are vulnerable to prompt injection attacks where users attempt to bypass security controls and access restricted information.

## Solution

This project implements a Prompt Injection Firewall that analyzes user prompts before they reach the AI system and blocks potentially malicious instructions.

## Architecture

User Input
↓
Prompt Firewall
↓
Threat Detection
↓
Allow / Block Decision

## Features

- Detects common prompt injection patterns
- Blocks suspicious instructions
- Allows normal user prompts
- Lightweight Python implementation
- Easy to extend with additional security rules

## Setup Steps

### Clone Repository

```bash
git clone https://github.com/your-username/prompt-injection-firewall.git
```

### Run Application

```bash
python app.py
```

## Project Structure

```text
prompt-injection-firewall/
├── README.md
├── app.py
├── requirements.txt
├── agents/
├── screenshots/
└── testcases/
```
