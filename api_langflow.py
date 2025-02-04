import os
import requests
from dotenv import load_dotenv

load_dotenv()

def add_data_in_rag(input_message: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv('DATASTAX_LANGFLOW_TOKEN')
    }

    payload = {
        "input_value": input_message,
        "output_type": "text",
        "input_type": "chat",
        "tweaks": {
            "SplitText-3y1E9": {},
            "AstraDB-IFai9": {},
            "OpenAIEmbeddings-2DEjQ": {},
            "URL-vv37c": {},
            "ChatInput-pUibl": {}
        }
    }

    url = os.getenv('UPDATE_RAG_API')

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print("Response Status Code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_result(input_message: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv('DATASTAX_LANGFLOW_TOKEN')
    }

    payload = {
        "input_value": input_message,
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {
            "AstraDB-9Bl2g": {},
            "OpenAIEmbeddings-NhvT4": {},
            "ChatInput-2rQeF": {},
            "RetrieverTool-GHlBs": {
                "description": "You're a Retrieval Tool to retrieve data related to the posts",
                "name": "RetrievePostaData"
            },
            "Agent-jDKNq": {},
            "ChatOutput-2CetC": {}
        }
    }

    url = os.getenv('RETRIEVE_DATA_API')

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print("Response Status Code:", response.status_code)

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def query_engagement(input_message: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.getenv('DATASTAX_LANGFLOW_TOKEN')
    }

    payload = {
        "input_value": input_message,
        "output_type": "chat",
        "input_type": "chat",
        "tweaks": {
            "AstraDBToolComponent-XhyxA": {},
            "Agent-IlD5x": {},
            "ChatInput-KH1Cr": {},
            "ChatOutput-wlgiN": {},
            "Prompt-6IRnb": {
                "template": "Find the average engagement rate of all the posts for the given post type\nPost Type: {type}",
                "type": ""
            }
        }
    }

    url = os.getenv('QUERY_ENGAGEMENT_API')

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print("Response Status Code:", response.status_code)

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
