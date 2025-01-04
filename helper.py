import os
import csv
import requests
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

def array_to_csv(data: List[Dict], output_file: str, delimiter: str = ','):
    if not data:
        raise ValueError("Input data cannot be empty")

    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Input must be a list of dictionaries")

    headers = list(data[0].keys())

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
            return {'success': True}
    except IOError as e:
        print(f"Error writing to file: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

def fetch_csv_file():
    storage_url = os.getenv('STORAGE_API')
    payload = {}
    files = {}
    headers = {}

    try:
        response = requests.request("GET", storage_url, headers=headers, data=payload, files=files)
        response.raise_for_status()
        return {'data': response.text}
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

def upload_csv_file(file_path: str):
    storage_url = os.getenv('STORAGE_API')
    payload = {}
    files = [
        ('file', ('social_instagram.csv', open(file_path, 'rb'), 'text/csv'))
    ]
    headers = {}

    try:
        response = requests.request("PUT", storage_url, headers=headers, data=payload, files=files)
        response.raise_for_status()
        return {'success': True}
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")

def get_message(data):
    try:
        if data and "outputs" in data and len(data["outputs"]) > 0:
            output = data["outputs"][0]
            if output and "outputs" in output and len(output["outputs"]) > 0:
                new_output = output["outputs"][0]
                if "artifacts" in new_output and "message" in new_output["artifacts"]:
                    message = new_output["artifacts"]["message"]
                    return message
        return "Something went wrong!"
    except Exception as e:
        return f"An error occurred: {e}"
