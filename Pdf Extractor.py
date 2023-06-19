from PyPDF2 import PdfReader, PdfWriter

pdf_path = "Edexcel Final Revision_230602_164124.pdf"
file_base_name = pdf_path.replace('.pdf', '')

pdf_read = PdfReader(pdf_path)
print(len(pdf_read.pages))

new_pdf = PdfWriter()

for page in range(0,105):
    new_pdf.add_page(pdf_read.pages[page])

print(len(new_pdf.pages))
new_pdf.write("Extracted.pdf")
new_pdf.close()