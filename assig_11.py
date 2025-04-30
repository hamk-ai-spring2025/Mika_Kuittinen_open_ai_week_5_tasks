import openai

def generate_markdown_article(topic):
    system_prompt = (
        "You are a scientific writer assistant. Generate a markdown-formatted article in fluent academic English. "
        "The article must include: a title, abstract, introduction, main sections (with subheadings), conclusion, and a reference list. "
        "All references must follow APA style and be cited within the text and listed at the end. "
        "Output only valid markdown. Do not include any explanation or comments."
    )

    user_prompt = f"Write a scientific article on the topic: {topic}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Or gpt-3.5-turbo if needed
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )

        content = response['choices'][0]['message']['content'].strip()

        filename = "article_output.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Markdown article saved to: {filename}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Test with fixed topic (you can replace with input() if needed)
    topic = "Edge computing in 5G networks"
    generate_markdown_article(topic)