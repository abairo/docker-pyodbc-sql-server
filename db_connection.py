import pyodbc


class DBConnection():

    def __init__(self, server:str, database:str, uid:str, pwd:str, driver:str = None, port:int = None):
        if not driver:
            drivers = [item for item in pyodbc.drivers()]
            driver = drivers[-1]
        if port:
            server += ',' + str(port)

        connection_string = self._build_conn_string(driver, server, database, uid, pwd)
        self._connection = pyodbc.connect(connection_string)
        self._cursor = self._connection.cursor()

    def _build_conn_string(self, driver, server, database, uid, pwd):
        return f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}'

    def __enter__(self):
       return self

    def execute(self, query:str):
        return self._cursor.execute(query)

    def __exit__(self, exc_type, exc_value, traceback):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()
