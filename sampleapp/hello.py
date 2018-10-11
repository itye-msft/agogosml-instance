import sys
import os

def add_num(x, y):
    return x + y



if __name__ == '__main__':
    print("These are the passed env vars:")
    print(os.environ['EH_CONN_STRING'])
    print(os.environ['BLOB_ST_CONN_STRING'])
    print(os.environ['BUILD_NAME'])