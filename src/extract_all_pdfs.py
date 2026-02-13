
import os
from pypdf import PdfReader

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(PROJECT_ROOT, "data", "pdfs")
OUTPUT_DIR = os.path.join(PDF_DIR, "extracted_text")

def extract_text(pdf_path, output_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted: {os.path.basename(pdf_path)}")
    except Exception as e:
        print(f"Failed to extract {os.path.basename(pdf_path)}: {e}")

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, filename)
            txt_filename = filename + ".txt"
            output_path = os.path.join(OUTPUT_DIR, txt_filename)
            extract_text(pdf_path, output_path)

if __name__ == "__main__":
    main()
