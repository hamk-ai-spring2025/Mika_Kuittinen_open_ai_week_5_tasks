import markdown
import pdfkit

def convert_markdown_to_pdf(input_md="article_output.md", output_pdf="article_output.pdf"):
    try:
        # Lue markdown-tiedosto
        with open(input_md, "r", encoding="utf-8") as f:
            text = f.read()

        # Muunna markdown HTML:ksi
        html = markdown.markdown(text)

        # Tee PDF
        pdfkit.from_string(html, output_pdf)

        print(f"✅ PDF saved as: {output_pdf}")
    except Exception as e:
        print(f"❌ Error during PDF conversion: {e}")

if __name__ == "__main__":
    convert_markdown_to_pdf()