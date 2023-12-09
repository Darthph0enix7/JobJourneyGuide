import fitz  # PyMuPDF

def extract_text_with_positions(pdf_path):
    doc = fitz.open(pdf_path)
    text_positions = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for b in blocks:
            if "lines" in b:
                for line in b["lines"]:
                    for span in line["spans"]:
                        text_positions.append({
                            "text": span["text"],
                            "position": {
                                "x0": span["bbox"][0],
                                "y0": span["bbox"][1],
                                "x1": span["bbox"][2],
                                "y1": span["bbox"][3]
                            }
                        })
    return text_positions

pdf_text_positions = extract_text_with_positions("/path/to/your/pdf")
for item in pdf_text_positions:
    print(f"Text: {item['text']}, Position: {item['position']}")
