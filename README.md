# docker-pyodbc-sql-server
This Skeleton aims to provide for python projects, that need a connection with Microsoft SQL Server, a minimal configuration. Follow the instructions or feel free to modify.
___
## Instructions
Edit the docker-compose.yml file and add a command to start your project, example:

```sh
command: python app.py
```
___
Create a .env and .db_env files with the next content in the root of project:
*.env*
```
DB_DRIVER=
DATABASE=some_table
PWD=$0M3P#55WORD
UID=sa
SERVER=DB
PORT=1433
```
*.db_env*
```
ACCEPT_EULA=Y
SA_PASSWORD=$0M3P#55WORD
MSSQL_PID=Express
```

___

Run the project:

```
docker-compose build
docker-compose up --force-recreate
```

Example of usage with flask:

```python
from flask import Flask
from db.connection_helper import get_connection


app = Flask(__name__)

@app.route("/")
def get_any_content():
    with get_connection() as db_connection:
        result = db_connection.execute('SELECT * FROM some_table')
        response = ''
        for row in result:
            response += ' - '.join(map(str, row)) + '| '
        
        return response, 200


app.run(host='0.0.0.0', port=8000)

```

**That's all folks!**