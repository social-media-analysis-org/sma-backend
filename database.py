import os
from dotenv import load_dotenv
from astrapy import DataAPIClient

load_dotenv()

client = DataAPIClient(os.getenv('ASTRA_DB_ENDPOINT'))
database = client.get_database(os.getenv('ASTRA_DB_TOKEN'))
collection = database.get_collection(os.getenv('ASTRA_DB_COLLECTION'))
