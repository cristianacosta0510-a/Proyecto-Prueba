import fitz
doc = fitz.open(r"C:\Users\Dell 5490\Downloads\Subir Proyecto a GIT.pdf")
text = ""
for page in doc:
    text += page.get_text()
with open("pdf_text.txt", "w", encoding="utf-8") as f:
    f.write(text)
