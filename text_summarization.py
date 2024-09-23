# openai_helper.py
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = OpenAI()
client.api_key = "sk-whE029zy6o5ZwTQA9oJ5sOkzMv8ACerR82dmmtHnN_T3BlbkFJe0zRwUgcI_Hu-oJ3s_SmZ61HJ3CpZ3Gf_LEd7HLlcA"

def generate_section_summary(section_text):
    """
    Sends a section of the document text to OpenAI API to generate a plain language summary.
    
    :param section_text: The text of a section of the document.
    :return: The summary of the section.
    """
    try:
        response = client.completions.create(
            model="davinci-002",  # Use GPT-3 or GPT-4 engine
            prompt=f"Summarize this section in plain language: {section_text}",
            max_tokens=2048,  # Adjust token count based on summary length
            temperature=0.7  # Adjust temperature for creativity
        )
        # Return the generated summary
        return response.choices[0].text.strip()

    except Exception as e:
        return f"Error generating summary: {str(e)}"
