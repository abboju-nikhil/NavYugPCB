import fitz  # PyMuPDF

pdf_path = "knowledge/datasheets/LM340.pdf"

doc = fitz.open(pdf_path)

print(f"Pages: {len(doc)}")
print("=" * 50)

for page_num, page in enumerate(doc, start=1):
    print(f"\n----- Page {page_num} -----\n")
    print(page.get_text())

doc.close()