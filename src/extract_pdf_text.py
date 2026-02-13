import os
from pypdf import PdfReader

def extract_text_from_pdfs(directory):
    output_file = os.path.join(directory, "extracted_content.txt")
    
    with open(output_file, "w", encoding="utf-8") as out:
        for filename in os.listdir(directory):
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(directory, filename)
                try:
                    reader = PdfReader(pdf_path)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text() + "\n"
                    
                    out.write(f"--- START OF FILE: {filename} ---\n")
                    out.write(text)
                    out.write(f"\n--- END OF FILE: {filename} ---\n\n")
                    print(f"Successfully extracted text from: {filename}")
                except Exception as e:
                    print(f"Error extracting text from {filename}: {e}")
                    out.write(f"--- ERROR EXTRACTING FILE: {filename} ---\n")
                    out.write(str(e))
                    out.write(f"\n--- END OF ERROR: {filename} ---\n\n")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Extracting PDFs in: {current_dir}")
    extract_text_from_pdfs(current_dir)
