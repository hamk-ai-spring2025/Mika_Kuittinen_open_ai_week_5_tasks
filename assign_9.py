import os
import openai
from PIL import Image
import markdown

# Fetch OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_product_description(image_path, user_input=None):
    # Load the image
    image = Image.open(image_path)
    
    # Optionally process the image (resize, etc.)
    image.show()  # This will open the image for preview

    # Create OpenAI prompt based on user input and image
    prompt = f"Generate a product description for the following product: {user_input if user_input else 'Ford Mustang, a powerful sports car loved by youth.'}"
    
    # OpenAI API request to generate text
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Using GPT-4 model
        messages=[
            {"role": "system", "content": "You are a creative marketing assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    
    description = response['choices'][0]['message']['content'].strip()
    
    # Create Markdown content
    markdown_content = f"![Product Image]({image_path})\n\n## Product Description\n{description}\n\n## Marketing Slogans\n* 'Ford Mustang, the sports car loved by youth!'\n* 'Ford Mustang, the most powerful sports car on the market!'\n* 'The best-selling car in Europe!'"

    # Save Markdown file
    output_filename = os.path.splitext(image_path)[0] + '_description.md'
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    
    print(f"Markdown file created: {output_filename}")

# Example usage
image_path = r'C:\pics\assig_9.jpg'  # Path to your Ford Mustang image
user_input = "Ford Mustang, a powerful sports car loved by youth"
generate_product_description(image_path, user_input)

# Määritä tiedostopolku
file_path = r'C:\pics\assig_9.md'

# Lue alkuperäinen tiedosto
with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
    content = file.read()

# Korjaa virheelliset merkit (esim. muuttamalla '�' takaisin oikeaksi merkkiksi)
content = content.replace('�', 'ä')  # Voit vaihtaa kaikki virheelliset merkit oikeiksi merkeiksi

# Tallenna korjattu tiedosto
corrected_file_path = r'C:\pics\assig_9_corrected.md'
with open(corrected_file_path, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"Tiedosto on korjattu ja tallennettu polkuun: {corrected_file_path}")