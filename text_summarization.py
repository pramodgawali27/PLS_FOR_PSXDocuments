# openai_helper.py
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
client = AzureOpenAI(
    azure_endpoint = "https://plstest.openai.azure.com/",
    api_key = "<api key>",
    api_version = "2024-05-01-preview",
)
chat_model_id = "PLSTest"
def generate_section_summary(section_text,security_input):
    """
    Sends a section of the document text to OpenAI API to generate a plain language summary.
    
    :param section_text: The text of a section of the document.
    :return: The summary of the section.
    """
    print(client.api_key)
    client.api_key=security_input
    print(client.api_key)
    prompt="""Generate Plain Language Summary
           """
    try:
        response = client.chat.completions.create(
         model=chat_model_id,
         messages= [
         {
            "role": "system",
             "content": f"{prompt}: {section_text}"
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



def has_more_than_10_words(text):
    # Split the text into words using whitespace
    words = text.split()
    
    # Check if the number of words is greater than 10
    if len(words) > 10:
        return True
    else:
        return False