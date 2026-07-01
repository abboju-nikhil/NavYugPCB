import fitz  # PyMuPDF
from pathlib import Path

class PDFReader:
    def read_pdf(self, pdf_path: str | Path) -> str:
        """Reads a PDF file and extracts all text."""
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF not found at: {pdf_path}")

        text = ""
        # Using context manager to ensure the file closes automatically
        with fitz.open(pdf_path) as document:
            for page in document:
                text += page.get_text()

        return text