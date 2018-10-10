import sys
import os

def add_num(x, y):
    return x + y


if __name__ == '__main__':
    print("These are the passed env vars:")
    print(os.environ['EH_CONN_STRING'])
    print(os.environ['BLOB_ST_CONN_STRING'])
    print(os.environ['BUILD_NAME'])
    print(os.environ['AZURE_STORAGE_ACCOUNT'])
    print(os.environ['AZURE_STORAGE_ACCESS_KEY'])
    print(os.environ['EVENT_HUB_NAMESPACE'])
    print(os.environ['EVENT_HUB_NAME'])
    print(os.environ['EVENT_HUB_SAS_POLICY'])
    print(os.environ['EVENT_HUB_SAS_KEY'])