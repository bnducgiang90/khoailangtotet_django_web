from django.db import connections, connection, transaction
from django.db.models.query import RawQuerySet
from django.db.models.sql.query import RawQuery
from psycopg2._psycopg import cursor, connection as pg_connection


class postgresqldb:
    def __init__(self):
        self.__connection: pg_connection = None
        self.__cursor: cursor = None

    def connect(self):
        self.__connection: pg_connection = connections['postgresql_khoailangdb']
        self.__cursor = self.__connection.cursor()


    def getdata(self):
        self.__connection: pg_connection = connections['postgresql_khoailangdb']
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        self.__cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = self.__cursor.fetchone()
        return row
