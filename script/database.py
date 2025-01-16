import sqlite3
import mysql.connector
import psycopg2
from pymongo import MongoClient

class BaseDatabase:
    def connect(self):
        raise NotImplementedError("Connect method must be implemented")

    def execute_query(self, query, params=None):
        raise NotImplementedError("Execute method must be implemented")

    def close(self):
        raise NotImplementedError("Close method must be implemented")

class SQLiteConnector(BaseDatabase):

    def __init__(self, path):
        self.path = path
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.path)

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        return cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()
class MySQLConnector(BaseDatabase):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        return cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()

class PostgreSQLConnector(BaseDatabase):
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        return cursor.fetchall()

    def close(self):
        if self.connection:
            self.connection.close()

class MongoDBConnector(BaseDatabase):
    def __init__(self, uri, database):
        self.uri = uri
        self.database_name = database
        self.client = None
        self.db = None

    def connect(self):
        self.client = MongoClient(self.uri)
        self.db = self.client[self.database_name]

    def execute_query(self, collection_name, operation, *args, **kwargs):
        collection = self.db[collection_name]
        method = getattr(collection, operation)
        return method(*args, **kwargs)

    def close(self):
        if self.client:
            self.client.close()


if __name__ == "__main__":
    sqlite_conn = SQLiteConnector("example.db")
    sqlite_conn.connect()
    sqlite_conn.execute_query("CREATE TABLE IF NOT EXISTS test (id INTEGER, name TEXT)")
    sqlite_conn.execute_query("INSERT INTO test (id, name) VALUES (?, ?)", (1, "Alice"))
    result = sqlite_conn.execute_query("SELECT * FROM test")
    print(result)
    sqlite_conn.close()

    mysql_conn = MySQLConnector("localhost", "root", "password", "testdb")
    mysql_conn.connect()
    mysql_conn.execute_query("CREATE TABLE IF NOT EXISTS test (id INT, name VARCHAR(255))")
    mysql_conn.execute_query("INSERT INTO test (id, name) VALUES (%s, %s)", (1, "Bob"))
    result = mysql_conn.execute_query("SELECT * FROM test")
    print(result)
    mysql_conn.close()

    pgsql_conn = PostgreSQLConnector("localhost", "user", "password", "testdb")
    pgsql_conn.connect()
    pgsql_conn.execute_query("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name TEXT)")
    pgsql_conn.execute_query("INSERT INTO test (name) VALUES (%s)", ("Charlie",))
    result = pgsql_conn.execute_query("SELECT * FROM test")
    print(result)
    pgsql_conn.close()

    mongo_conn = MongoDBConnector("mongodb://localhost:27017", "testdb")
    mongo_conn.connect()
    mongo_conn.execute_query("test", "insert_one", {"_id": 1, "name": "Diana"})
    result = mongo_conn.execute_query("test", "find_one", {"_id": 1})
    print(result)
    mongo_conn.close()
