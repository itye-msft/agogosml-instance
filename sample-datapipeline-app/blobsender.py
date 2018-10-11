"""
Helper to upload data into blob storage
"""

import os
import logging
import uuid
import dotenv

from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings


def uploadblob(content):
    """ Uploads content string into blob storage
    """
    storage_account = os.environ['AZURE_STORAGE_ACCOUNT']
    storage_key = os.environ['AZURE_STORAGE_ACCESS_KEY']
    storage_container = os.environ['AZURE_STORAGE_CONTAINER'] # Build name is the container

    # Generate guid for filename
    blob_name = str(uuid.uuid4()) + '.json'

    block_blob_service = BlockBlobService(account_name=storage_account, account_key=storage_key)

    # Upload the CSV file to Azure cloud
    block_blob_service.create_blob_from_bytes(
        storage_container, blob_name, content.encode('ASCII'),
        content_settings=ContentSettings('application/json'))


if __name__ == "__main__":
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)
    dotenv.load_dotenv('.env')
