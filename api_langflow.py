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
            "SplitText-j6HlH": {},
            "AstraDB-ygzpP": {},
            "OpenAIEmbeddings-RLDQw": {},
            "URL-V9koU": {},
            "ChatInput-UXGEz": {}
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
            "AstraDB-8EbmW": {},
            "OpenAIEmbeddings-xtphZ": {},
            "ChatInput-j3u2L": {},
            "RetrieverTool-9y7D2": {
                "description": "You're a Retrieval Tool to retrieve data related to the posts",
                "name": "RetrievePostaData"
            },
            "Agent-DGRUN": {},
            "ChatOutput-vG7DR": {}
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
