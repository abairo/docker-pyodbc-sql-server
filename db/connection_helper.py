import os
from .db_connection import DBConnection


def get_connection():
    DRIVER = os.environ.get('DB_DRIVER', None)
    DATABASE = os.environ.get('DATABASE', None)
    PWD = os.environ.get('PWD', None)
    UID = os.environ.get('UID', None)
    SERVER = os.environ.get('SERVER', None)
    PORT = os.environ.get('PORT', None)

    return DBConnection(driver=DRIVER, server=SERVER, database=DATABASE, uid=UID, pwd=PWD, port=PORT)
