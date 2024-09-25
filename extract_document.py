# form_recognizer_helper.py
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AZURE_FORM_RECOGNIZER_ENDPOINT = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT")
AZURE_FORM_RECOGNIZER_KEY = os.getenv("AZURE_FORM_RECOGNIZER_KEY")

def extract_text_and_structure_from_pdf(pdf_file_path):
    """
    Uses Azure Form Recognizer to extract structured text from a PDF document.

    :param pdf_file_path: Path to the PDF file.
    :return: Extracted text with structure.
    """
    client = DocumentAnalysisClient(
        endpoint=AZURE_FORM_RECOGNIZER_ENDPOINT,
        credential=AzureKeyCredential(AZURE_FORM_RECOGNIZER_KEY)
    )

    with open(pdf_file_path, "rb") as f:
        poller = client.begin_analyze_document("prebuilt-layout", document=f)
        result = poller.result()

    structured_text = []
    for page in result.paragraphs:
        page_text = f"Page 1:\n"
        #for line in page.spans:
        #    page_text += f"{line.}\n"
        structured_text.append(page.content)

    return structured_text

def extract_text_from_pdf(pdf_file_path):
    """
    Uses PyPDF2 to extract plain text from a PDF.

    :param pdf_file_path: Path to the PDF file.
    :return: Extracted text.
    """
    reader = PdfReader(pdf_file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
