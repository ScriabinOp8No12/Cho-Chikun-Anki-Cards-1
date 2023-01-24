import PyPDF2

# Open the PDF file in read-only mode
with open(r"C:\Users\nharw\Desktop\PDF2Anki Project\Cho Chikun LD1.pdf", 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfReader(file)

    # Iterate over every page
    for page in range(len(pdf.pages)):
        # Extract the text from the page
        text = pdf.pages[page].extract_text()

        # Save the text to a file
        with open(f'page_{page}.txt', 'w') as output:
            output.write(text)