import ollama


def generate_summary(blog):
    prompt = f"""
Summarize the following blog in exactly 3-5 concise sentences.

STRICT RULES:
- Return ONLY the summary.
- Do NOT write "Summary:".
- Do NOT write "Here is a summary".
- Do NOT add explanations.
- Do NOT use bullet points.

Blog:
{blog}
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

    summary = response["message"]["content"].strip()

    # Remove unwanted prefixes if the model adds them
    prefixes = [
        "Summary:",
        "Here is a summary:",
        "Here is a summary of the blog:",
        "Here is a summary of the blog post:"
    ]

    for prefix in prefixes:
        if summary.lower().startswith(prefix.lower()):
            summary = summary[len(prefix):].strip()

    return summary


if __name__ == "__main__":
    blog = input("Enter blog text: ")

    print("\nGenerating summary...\n")

    summary = generate_summary(blog)

    print("Summary:")
    print(summary)