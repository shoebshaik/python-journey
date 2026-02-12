"""Beginner-friendly PDF downloader and search tool.

This script downloads the Income Tax Act PDF (if needed), extracts text,
and lets the user search by keyword or section number.
"""

from pathlib import Path
import re

import requests
from pypdf import PdfReader

# 1) Source PDF URL (as required)
PDF_URL = "https://incometaxindia.gov.in/Documents/income-tax-act-1961-as-amended-by-finance-act-2025.pdf"

# Local file path where the PDF will be saved
PDF_FILE = Path(__file__).parent / "income-tax-act-1961.pdf"


def download_pdf_if_needed(url: str, file_path: Path) -> None:
    """Download the PDF only when it is not already present locally."""
    if file_path.exists():
        print(f"PDF already exists: {file_path}")
        return

    print("Downloading PDF... This may take a little time.")
    response = requests.get(url, timeout=60)
    response.raise_for_status()  # stop with an error if download failed

    file_path.write_bytes(response.content)
    print(f"Download complete: {file_path}")


def extract_pdf_text(file_path: Path) -> str:
    """Extract and combine text from all pages of the PDF."""
    print("Extracting text from PDF...")
    reader = PdfReader(str(file_path))

    all_pages_text = []
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""
        all_pages_text.append(page_text)

        # Optional progress update every 50 pages for large PDFs
        if page_number % 50 == 0:
            print(f"  Processed {page_number} pages...")

    full_text = "\n".join(all_pages_text)
    print("Text extraction complete.")
    return full_text


def split_into_paragraphs(text: str) -> list[str]:
    """Split text into paragraph-like chunks.

    PDFs are often messy, so we normalize multiple blank lines and then split.
    """
    normalized = re.sub(r"\n\s*\n+", "\n\n", text)
    paragraphs = [p.strip() for p in normalized.split("\n\n") if p.strip()]
    return paragraphs


def find_matches(paragraphs: list[str], query: str) -> list[int]:
    """Return indices of paragraphs that contain the query (case-insensitive)."""
    query_lower = query.lower().strip()
    return [i for i, para in enumerate(paragraphs) if query_lower in para.lower()]


def show_matches_with_context(paragraphs: list[str], match_indices: list[int], context_size: int = 1) -> None:
    """Display each matching paragraph with surrounding context paragraphs."""
    if not match_indices:
        print("No matches found.")
        return

    print(f"\nFound {len(match_indices)} matching paragraph(s). Showing results:\n")

    for count, idx in enumerate(match_indices, start=1):
        start = max(0, idx - context_size)
        end = min(len(paragraphs), idx + context_size + 1)

        print("=" * 80)
        print(f"Match {count} (paragraph {idx + 1}):")
        print("=" * 80)

        for para_index in range(start, end):
            label = "MATCH" if para_index == idx else "CONTEXT"
            print(f"\n[{label}] Paragraph {para_index + 1}:")
            print(paragraphs[para_index])

        print("\n")


def main() -> None:
    """Program flow."""
    try:
        # 2) Download if not already downloaded
        download_pdf_if_needed(PDF_URL, PDF_FILE)

        # 3) Extract text
        full_text = extract_pdf_text(PDF_FILE)
        paragraphs = split_into_paragraphs(full_text)

        if not paragraphs:
            print("Could not extract readable text from the PDF.")
            return

        # 4) Ask user for keyword/section number
        query = input("\nEnter a keyword or section number to search (example: 80C, salary, deduction): ").strip()

        if not query:
            print("Search text cannot be empty.")
            return

        # 5) Display matching paragraphs with surrounding context
        matches = find_matches(paragraphs, query)
        show_matches_with_context(paragraphs, matches, context_size=1)

    except requests.RequestException as error:
        print(f"Network/download error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
