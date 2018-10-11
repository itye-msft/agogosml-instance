"""
Transforms data into the final output data
"""

import json
import logging

logger = logging.getLogger(__name__)

def transform(data):
    """ Applies simple transformation to the data
    Expects data:
        raw_data = {
        "intValue": "42",
        "floatValue": "3.14159265358979",
        "timeValue": "2018-10-09T20:21:51.039Z",
        "boolValue": "false",
        "stringValue": "abc% - &XYZ"
        }
    """
    logger.info('Transforming data {}'.format(data))
    parsed_json = json.loads(data)
    parsed_json['intValue'] = parsed_json['intValue'] + 1 # Very simple transform :)
    return json.dumps(parsed_json)


if __name__ == "__main__":
    LOG_FMT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=LOG_FMT)
