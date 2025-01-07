import os
from dotenv import load_dotenv
from astrapy import DataAPIClient
from astrapy.constants import VectorMetric
from astrapy.info import CollectionVectorServiceOptions

load_dotenv()

client = DataAPIClient(os.getenv('ASTRA_DB_TOKEN'))
database = client.get_database(os.getenv('ASTRA_DB_ENDPOINT'))

collection = database.get_collection(os.getenv('ASTRA_DB_COLLECTION'))
vector_collection = database.get_collection(os.getenv('ASTRA_DB_VECTOR_COLLECTION'))
engagement_collection = database.get_collection(os.getenv('ENGAGEMENT_COLLECTION'))

def delete_collection(collection_name: str):
    database.drop_collection(collection_name)

def create_collection(collection_name: str):
    database.create_collection(collection_name)

    # database.create_collection(
    #     collection_name,
    #     dimension=1024,
    #     metric=VectorMetric.COSINE,
    #     service=CollectionVectorServiceOptions(
    #         provider="nvidia",
    #         model_name="NV-Embed-QA",
    #     ),
    # )
