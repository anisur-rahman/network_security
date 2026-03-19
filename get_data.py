import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()
MongoDB_URI = os.getenv("MongoDB_URI")
print(MongoDB_URI)

import certifi

ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging


class NetworkExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)
