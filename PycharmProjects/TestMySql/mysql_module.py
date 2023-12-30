
class Mysql():
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        import mysql.connector

        print('Connecting to MySQL database...')
        # Connect to database
        cnx = mysql.connector.connect(user=self.user, password=self.password,
                                      host=self.host,
                                      database='classicmodels')
        # Return connection object
        return cnx

    def disconnect(self):
        print('Disconnecting from MySQL database...')
        # Disconnect from database
        # Return nothing

    def execute(self, query):
        print('Executing MySQL query...')
        # Execute query
        # Return result

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()