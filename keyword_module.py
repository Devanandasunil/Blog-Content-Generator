import ollama


def extract_keywords(topic):
    prompt = f"""
You are an SEO keyword research expert.

For the following blog topic:

"{topic}"

Generate SEO keywords.

Return exactly 10 keywords:
- 1 primary keyword
- 4 secondary keywords
- 5 long-tail keywords

Return ONLY the keywords as a numbered list.
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

    content = response["message"]["content"].strip()

    keywords = []

    for line in content.splitlines():
        line = line.strip()

        if not line:
            continue

        # Remove numbering such as "1.", "2.", etc.
        if "." in line[:3]:
            line = line.split(".", 1)[1].strip()

        if line:
            keywords.append(line)

    return keywords[:10]


if __name__ == "__main__":
    topic = input("Enter a topic: ").strip()

    if topic:
        keywords = extract_keywords(topic)

        print("\nSEO Keywords:")
        for index, keyword in enumerate(keywords, start=1):
            print(f"{index}. {keyword}")
    else:
        print("Topic cannot be empty.")