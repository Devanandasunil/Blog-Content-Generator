import ollama


def generate_blog(topic, audience, tone, intent, keywords, title):
    keyword_text = ", ".join(keywords)

    prompt = f"""
You are an expert SEO blog writer.

Write a high-quality blog article using the information below.

Topic:
{topic}

Title:
{title}

Target Audience:
{audience}

Tone:
{tone}

Search Intent:
{intent}

SEO Keywords:
{keyword_text}

Requirements:

1. Write approximately 800-1000 words.
2. Start with the exact title.
3. Write a compelling introduction.
4. Use clear H2 and H3 headings.
5. Explain the topic accurately and naturally.
6. Naturally include the provided SEO keywords.
7. Avoid keyword stuffing.
8. Use short paragraphs for readability.
9. Include examples where useful.
10. Include a conclusion.
11. Do not mention that you are an AI.
12. Do not include meta descriptions or SEO analysis.
13. Return ONLY the blog article in Markdown format.

Structure:

# Title

Introduction

## Main Section

Content

## Another Section

Content

## Conclusion

Content
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

    blog = response["message"]["content"].strip()

    return blog


if __name__ == "__main__":
    topic = input("Enter topic: ").strip()
    audience = input("Enter target audience: ").strip()
    tone = input("Enter tone: ").strip()
    intent = input("Enter search intent: ").strip()
    title = input("Enter blog title: ").strip()

    keywords_input = input(
        "Enter keywords separated by commas: "
    ).strip()

    keywords = [
        keyword.strip()
        for keyword in keywords_input.split(",")
        if keyword.strip()
    ]

    if topic and title:
        print("\nGenerating blog...\n")

        blog = generate_blog(
            topic,
            audience,
            tone,
            intent,
            keywords,
            title
        )

        print("=" * 70)
        print(blog)
        print("=" * 70)

    else:
        print("Topic and title are required.")