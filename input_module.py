def get_user_input():
    print("\n=== AI Blog Generator ===")

    topic = input("Enter the blog topic: ").strip()

    while not topic:
        print("Topic cannot be empty.")
        topic = input("Enter the blog topic: ").strip()

    audience = input(
        "Enter the target audience (optional): "
    ).strip()

    tone = input(
        "Enter the preferred tone (e.g., professional, friendly, casual): "
    ).strip()

    if not tone:
        tone = "professional"

    return {
        "topic": topic,
        "audience": audience,
        "tone": tone
    }


if __name__ == "__main__":
    data = get_user_input()
    print("\nCollected Input:")
    print(data)