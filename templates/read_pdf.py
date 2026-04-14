import sys
import subprocess

try:
    import PyPDF2
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

pdf_path = r"C:\Users\Dell 5490\Downloads\Tarea - Consultas.pdf"
txt_path = r"c:\Proyecto\templates\pdf_content.txt"

try:
    reader = PyPDF2.PdfReader(pdf_path)
    with open(txt_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            f.write(f"\n--- PAGE {i+1} ---\n")
            text = page.extract_text()
            if text:
                f.write(text)
    print(f"Extraido en {txt_path}")
except Exception as e:
    print(f"Error: {e}")
