import os
import re
from pypdf import PdfReader

PDF_DIR = r"C:\Users\Lenovo\Desktop\script\pdf_for_embedd"

def clean_text(text):
    if not text:
        return ""
    # Replace multiple newlines/spaces with single space
    return re.sub(r'\s+', ' ', text).strip()

def extract_specs(pdf_path):
    print(f"Analyzing {os.path.basename(pdf_path)}...")
    specs = {
        'tops': 0.0,
        'cpu_freq': 0.0,  # in MHz
        'cpu_cores': "Unknown",
        'model': "Unknown"
    }
    
    try:
        reader = PdfReader(pdf_path)
        # Read first 5 pages or all if less
        text = ""
        for i in range(min(5, len(reader.pages))):
            text += reader.pages[i].extract_text() + "\n"
        
        text = clean_text(text)
        
        # 1. AI Performance (TOPS)
        # Patterns: "X TOPS", "X.X TOPS", "X T", "X.X T"
        # Be careful not to match "TOPS" inside generic text without numbers
        tops_matches = re.findall(r'(\d+(?:\.\d+)?)\s*(?:TOPS|Tops|T\b)', text, re.IGNORECASE)
        if tops_matches:
            # Take the max value found, assuming it mentions peak performance
            specs['tops'] = max([float(m) for m in tops_matches])

        # 2. CPU Frequency
        # Patterns: "X GHz", "X MHz"
        idx = 0
        freq_matches = re.findall(r'(\d+(?:\.\d+)?)\s*(GHz|MHz)', text, re.IGNORECASE)
        max_freq = 0.0
        for val, unit in freq_matches:
            val = float(val)
            if unit.lower() == 'ghz':
                val *= 1000
            if val > max_freq and val < 10000: # Filter out unrealistic values like 2026 (year)
                max_freq = val
        specs['cpu_freq'] = max_freq

        # 3. CPU Cores/Architecture
        # Cortex-A, Cortex-M, RISC-V
        cores = []
        if re.search(r'Cortex-?A\d+', text, re.IGNORECASE):
            cores.append(re.search(r'Cortex-?A\d+', text, re.IGNORECASE).group(0))
        if re.search(r'Cortex-?M\d+', text, re.IGNORECASE):
            cores.append(re.search(r'Cortex-?M\d+', text, re.IGNORECASE).group(0))
        if re.search(r'RISC-?V', text, re.IGNORECASE):
            cores.append("RISC-V")
            
        if cores:
            specs['cpu_cores'] = ", ".join(list(set(cores)))

        # Attempt to find board model name if possible (often first few words or near "Model")
        # This is hard to do generically, will use filename as primary ID
        
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")

    return specs

def main():
    if not os.path.exists(PDF_DIR):
        print(f"Directory not found: {PDF_DIR}")
        return

    results = []
    
    for filename in os.listdir(PDF_DIR):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(PDF_DIR, filename)
            specs = extract_specs(path)
            specs['filename'] = filename
            results.append(specs)

    # Ranking Logic
    # 1. TOPS (Descending)
    # 2. CPU Frequency (Descending)
    results.sort(key=lambda x: (x['tops'], x['cpu_freq']), reverse=True)

    print("\n" + "="*80)
    print(f"{'Rank':<5} | {'Board (File)':<30} | {'AI (TOPS)':<10} | {'CPU Freq (MHz)':<15} | {'Core Arch':<20}")
    print("-" * 80)
    
    for i, res in enumerate(results):
        print(f"{i+1:<5} | {res['filename']:<30} | {res['tops']:<10} | {res['cpu_freq']:<15.1f} | {res['cpu_cores']:<20}")
    print("="*80)

if __name__ == "__main__":
    main()
