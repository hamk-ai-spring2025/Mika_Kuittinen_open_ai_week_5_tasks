import openai
import json
import os
import re

def generate_dictionary_entry(word: str):
    system_prompt = (
        "You are an English dictionary generator. Respond with valid JSON only, without any explanation or extra text. "
        "The JSON object must include the following keys: word, definition, synonyms, antonyms, and examples. "
        "All content must be in English."
    )

    user_prompt = f"Create a dictionary entry for the word: {word}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # or gpt-3.5-turbo if needed
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.5
        )

        raw_output = response['choices'][0]['message']['content'].strip()

        # Remove Markdown formatting if present (like ```json ... ```)
        cleaned = re.sub(r"^```json|```$", "", raw_output.strip(), flags=re.MULTILINE).strip()

        try:
            result = json.loads(cleaned)

            required_keys = ["word", "definition", "synonyms", "antonyms", "examples"]
            if not all(key in result for key in required_keys):
                print(f"⚠️ Word '{word}': JSON is missing required keys.")
                return None

            print(f"✅ Word '{word}' processed successfully.")
            return result

        except json.JSONDecodeError:
            print(f"⚠️ Word '{word}': Invalid JSON:\n{cleaned}\n")
            return None

    except Exception as e:
        print(f"⚠️ Word '{word}': API error: {e}")
        return None

def save_individual_file(word: str, data: dict):
    filename = f"word_{word}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"📄 Saved: {filename}")

def save_combined_file(entries: list):
    filename = "dictionary_all.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=4, ensure_ascii=False)
    print(f"\n📘 All entries saved to: {filename}")

if __name__ == "__main__":
    user_input = input("Enter one or more words, separated by commas (e.g. freedom, expensive, fast): ")
    words = [w.strip() for w in user_input.split(",") if w.strip()]
    combined_entries = []

    for word in words:
        print(f"\n🔍 Processing word: '{word}'...")
        result = generate_dictionary_entry(word)
        if result:
            print(json.dumps(result, indent=4, ensure_ascii=False))
            save_individual_file(word, result)
            combined_entries.append(result)

    if combined_entries:
        save_combined_file(combined_entries)