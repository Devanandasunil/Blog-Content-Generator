import os
from datetime import datetime

from input_module import get_user_input
from intent_module import detect_intent
from keyword_module import extract_keywords
from title_module import generate_titles
from blog_module import generate_blog
from summary_module import generate_summary
from meta_module import generate_meta_description


def save_output(topic, title, blog, summary, meta_description, intent, keywords):
    os.makedirs("outputs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"blog_{timestamp}.md"
    filepath = os.path.join("outputs", filename)

    content = f"""# {title}

**Topic:** {topic}

**Search Intent:** {intent}

## SEO Keywords

{chr(10).join(f"- {keyword}" for keyword in keywords)}

## Meta Description

{meta_description}

## Summary

{summary}

---

## Blog

{blog}
"""

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    return filepath


def main():
    print("\n" + "=" * 70)
    print("           AI BLOG GENERATOR")
    print("=" * 70)

    # --------------------------------------------------
    # 1. Collect user input
    # --------------------------------------------------
    user_data = get_user_input()

    topic = user_data["topic"]
    audience = user_data["audience"]
    tone = user_data["tone"]

    # --------------------------------------------------
    # 2. Detect search intent
    # --------------------------------------------------
    print("\n[1/6] Detecting search intent...")

    intent = detect_intent(topic)

    print(f"Search Intent: {intent}")

    # --------------------------------------------------
    # 3. Generate SEO keywords
    # --------------------------------------------------
    print("\n[2/6] Generating SEO keywords...")

    keywords = extract_keywords(topic)

    print("\nSEO Keywords:")
    for index, keyword in enumerate(keywords, start=1):
        print(f"{index}. {keyword}")

    # --------------------------------------------------
    # 4. Generate SEO titles
    # --------------------------------------------------
    print("\n[3/6] Generating SEO titles...")

    titles = generate_titles(topic, intent, keywords)

    if not titles:
        print("Could not generate titles.")
        return

    print("\nGenerated Titles:")
    for index, title in enumerate(titles, start=1):
        print(f"{index}. {title}")

    # --------------------------------------------------
    # 5. Let user choose a title
    # --------------------------------------------------
    print("\nChoose a title for your blog.")

    while True:
        try:
            choice = int(input(f"Enter title number (1-{len(titles)}): "))

            if 1 <= choice <= len(titles):
                selected_title = titles[choice - 1]
                break

            print("Please choose a valid title number.")

        except ValueError:
            print("Please enter a number.")

    print(f"\nSelected Title: {selected_title}")

    # --------------------------------------------------
    # 6. Generate blog
    # --------------------------------------------------
    print("\n[4/6] Generating blog...")
    print("This may take a little time with the local Ollama model.\n")

    blog = generate_blog(
        topic,
        audience,
        tone,
        intent,
        keywords,
        selected_title
    )

    print("\n" + "=" * 70)
    print("GENERATED BLOG")
    print("=" * 70)
    print(blog)
    print("=" * 70)

    # --------------------------------------------------
    # 7. Generate summary
    # --------------------------------------------------
    print("\n[5/6] Generating summary...")

    summary = generate_summary(blog)

    print("\nSummary:")
    print(summary)

    # --------------------------------------------------
    # 8. Generate meta description
    # --------------------------------------------------
    print("\n[6/6] Generating meta description...")

    meta_description = generate_meta_description(blog)

    print("\nMeta Description:")
    print(meta_description)

    # --------------------------------------------------
    # 9. Save everything
    # --------------------------------------------------
    filepath = save_output(
        topic,
        selected_title,
        blog,
        summary,
        meta_description,
        intent,
        keywords
    )

    print("\n" + "=" * 70)
    print("BLOG GENERATION COMPLETED!")
    print("=" * 70)

    print(f"\nFinal output saved to:")
    print(filepath)


if __name__ == "__main__":
    main()