from PyPDF2 import PdfReader
from PIL import Image
import pytesseract


def scan_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

    return text


def scan_image(file_path):

    image = Image.open(file_path)

    return pytesseract.image_to_string(image)
