import ollama


def generate_meta_description(blog):
    prompt = f"""
Write ONE SEO meta description for this blog.

STRICT RULES:
- Maximum 160 characters.
- Aim for 140-160 characters.
- Return ONLY the meta description.
- Do NOT write "Meta Description:".
- Do NOT explain your answer.
- Do NOT use quotation marks.
- Do NOT use bullet points.
- Do NOT add anything before or after the description.

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

    description = response["message"]["content"].strip()

    # Remove unwanted quotation marks
    description = description.strip('"').strip("'")

    # Remove common unwanted prefixes
    prefixes = [
        "Meta Description:",
        "Meta description:"
    ]

    for prefix in prefixes:
        if description.lower().startswith(prefix.lower()):
            description = description[len(prefix):].strip()

    # Guarantee maximum 160 characters
    if len(description) > 160:
        description = description[:157].rsplit(" ", 1)[0] + "..."

    return description


if __name__ == "__main__":
    blog = input("Enter blog text: ")

    print("\nGenerating meta description...\n")

    meta_description = generate_meta_description(blog)

    print("Meta Description:")
    print(meta_description)

    print(f"\nCharacter count: {len(meta_description)}")