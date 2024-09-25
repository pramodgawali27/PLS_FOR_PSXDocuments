# app.py
import streamlit as st
from extract_document import extract_text_and_structure_from_pdf
from text_summarization import generate_section_summary, has_more_than_10_words
from reportlab.pdfgen import canvas
from io import BytesIO

# Set up Streamlit page configuration
st.set_page_config(page_title="Structured PDF Summarizer", page_icon="📄", layout="centered")

# Title of the web app
st.title("📄 PDF Summarizer with Structure")

# File uploader for PDFs
uploaded_file = st.file_uploader("Upload your PDF for summarization", type=['pdf'])

if uploaded_file is not None:
    # Save the uploaded file
    with open("uploaded_document.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Extract structured text from the PDF
    structured_text = extract_text_and_structure_from_pdf("uploaded_document.pdf")
    
    st.write("---------------**Extracted Document Structure and Text**------:")
    for page in structured_text:
        st.write(page)

    # Summarize each page or section
    st.write("------------**Plain Language Summary**--------------")
    summarized_sections = []
    for page_text in structured_text:
        with st.spinner(f"Summarizing Page..."):
            #print(f"{page_text}\n")
            if has_more_than_10_words(page_text):
               st.write(f"**Orginal Text** :-- {page_text}")
               
               summary = generate_section_summary(page_text)
               st.write(f"**Plain Language Summary** :-- {summary}")
               summarized_sections.append(summary)
               st.write(summary)

    # Button to generate the summarized PDF
    if st.button("Generate Summarized PDF"):
        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        for i, summary in enumerate(summarized_sections):
            p.drawString(100, 750 - (i * 50), f"Page {i+1} Summary: {summary}")

        p.save()
        buffer.seek(0)

        # Offer download of summarized PDF
        st.download_button(
            label="Download Summarized PDF",
            data=buffer,
            file_name="summarized_document.pdf",
            mime="application/pdf"
        )


