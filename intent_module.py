import ollama


def detect_intent(topic):
    prompt = f"""
You are an SEO expert.

Analyze the search intent of this topic:

"{topic}"

Choose exactly ONE of these categories:

- Informational
- Commercial
- Transactional
- Navigational

Return ONLY the category name.
Do not provide explanations.
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    intent = response["message"]["content"].strip()

    valid_intents = [
        "Informational",
        "Commercial",
        "Transactional",
        "Navigational"
    ]

    for valid_intent in valid_intents:
        if valid_intent.lower() in intent.lower():
            return valid_intent

    return "Informational"


if __name__ == "__main__":
    topic = input("Enter a topic: ").strip()

    if topic:
        result = detect_intent(topic)
        print(f"\nDetected Intent: {result}")
    else:
        print("Topic cannot be empty.")