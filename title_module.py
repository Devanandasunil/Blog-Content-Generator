import ollama
import re


def generate_titles(topic, intent, keywords):
    keyword_text = ", ".join(keywords)

    prompt = f"""
You are an expert SEO content writer.

Create exactly 5 SEO-friendly blog titles for this topic:

Topic: {topic}
Search Intent: {intent}
Keywords: {keyword_text}

Rules:
1. Return ONLY the 5 titles.
2. Put each title on a separate line.
3. Number them 1 to 5.
4. Do NOT provide explanations.
5. Do NOT add introductions.
6. Do NOT add character counts.
7. Keep titles clear, natural, and engaging.
8. Keep titles under 70 characters when possible.

Example format:

1. How AI Is Transforming E-commerce
2. The Future of AI in Online Shopping
3. AI in E-commerce: Benefits and Applications
4. How Artificial Intelligence Improves Online Retail
5. AI-Powered E-commerce: A Complete Guide
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

    titles = []

    for line in content.splitlines():
        line = line.strip()

        # Match only lines beginning with 1. through 5.
        match = re.match(r"^[1-5][.)]\s*(.+)$", line)

        if match:
            title = match.group(1).strip()

            # Remove surrounding quotation marks
            title = title.strip('"').strip("'")

            # Ignore obvious explanation lines
            explanation_words = [
                "this title",
                "here are",
                "these titles",
                "this emphasizes",
                "this highlights"
            ]

            if not any(
                word in title.lower()
                for word in explanation_words
            ):
                titles.append(title)

    return titles[:5]


if __name__ == "__main__":
    topic = input("Enter topic: ").strip()
    intent = input("Enter search intent: ").strip()

    keywords_input = input(
        "Enter keywords separated by commas: "
    ).strip()

    keywords = [
        keyword.strip()
        for keyword in keywords_input.split(",")
        if keyword.strip()
    ]

    if topic and intent and keywords:
        titles = generate_titles(topic, intent, keywords)

        print("\nSEO Blog Titles:")

        for index, title in enumerate(titles, start=1):
            print(f"{index}. {title}")

    else:
        print("Topic, intent and keywords are required.")