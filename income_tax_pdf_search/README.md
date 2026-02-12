# Income Tax Act 1961 PDF Search (Beginner Friendly)

This small Python program:
1. Downloads the Income Tax Act PDF from a fixed URL (only the first time).
2. Saves it locally.
3. Extracts text from the PDF.
4. Asks you for a keyword or section number.
5. Shows matching paragraphs with surrounding context.

## File
- `search_income_tax_act.py`

## Requirements
- Python 3.9+
- Internet connection (only needed for first download)

Install required packages:

```bash
pip install requests pypdf
```

## Run
From the repository root:

```bash
python income_tax_pdf_search/search_income_tax_act.py
```

## Example search inputs
- `80C`
- `house property`
- `deduction`
- `section 10`

## Notes
- The PDF is saved as `income_tax_pdf_search/income-tax-act-1961.pdf`.
- If the file already exists, the program will reuse it and skip download.
- PDF text extraction can be imperfect because PDFs are designed for display, not plain text parsing.
