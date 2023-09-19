import os

"""import needed modules """
from os import getenv

""" store the value of  HBNB_TYPE_STORAGE environment variable in """
storageType = os.getenv("HBNB_TYPE_STORAGE")

""" import the needed storage class based on HBNB_TYPE_STORAGE environment variable """
if storageType == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

""" relaod storage """
storage.reload()
