import psycopg2
from abc import ABC , abstractmethod
from vault.credentials import Credentials

class DBConnector(ABC):
    def __init__(self):
        c=Credentials()
        return psycopg2.connect(**c.get_db_config())
