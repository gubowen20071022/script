# Embedded Chip Competition Research Project

This project contains research data, scripts, and reports for the 2026 National University Student Embedded Chip and System Design Competition (Chip Application Track).

## 📂 Project Structure

```
script/
├── src/                      # Python source code
│   ├── analyze_boards.py     # Extract hardware specs from PDFs
│   ├── extract_all_pdfs.py   # Extract text from all PDFs
│   ├── research_pdf.py       # Crawler script (BS4)
│   └── research_pdf_std.py   # Crawler script (Std Lib)
├── data/                     # Data files
│   ├── pdfs/                 # Original PDF datasheets
│   │   ├── extracted_text/   # Text extracted from PDFs
│   │   └── ...
│   └── temp/                 # Temporary data (HTML, raw txt)
└── reports/                  # Generated reports
    └── pdf_summary_report.md # Final summary report
```

## 🚀 Usage

1.  **Extract Text**: Run `python src/extract_all_pdfs.py` to convert PDFs in `data/pdfs` to text.
2.  **Analyze Specs**: Run `python src/analyze_boards.py` to analyze hardware specifications.
3.  **View Report**: Check `reports/pdf_summary_report.md`.
