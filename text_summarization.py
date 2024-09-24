# openai_helper.py
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = AzureOpenAI(
    azure_endpoint = "https://plstest.openai.azure.com/",
    api_key = "ac4ac1867bcc48779a4e5cbaa16b5f9c",
    api_version = "2024-05-01-preview",
)
chat_model_id = "PLSTest"
def generate_section_summary(section_text):
    """
    Sends a section of the document text to OpenAI API to generate a plain language summary.
    
    :param section_text: The text of a section of the document.
    :return: The summary of the section.
    """
    try:
        response = client.chat.completions.create(
         model=chat_model_id,
         messages= [
         {
            "role": "system",
             "content": f"Summarize this section in plain language: {section_text}"
         }
        ],
        max_tokens=800,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
        )
       
        print(response)
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating summary: {str(e)}"
