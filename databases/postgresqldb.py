from collections import namedtuple

from django.db import connections, connection, transaction
from django.db.models.query import RawQuerySet
from django.db.models.sql.query import RawQuery


# from psycopg2._psycopg import cursor, connection as pg_connection


class postgresqldb:
    def __init__(self):
        self.__connection = None
        self.__cursor = None

    def connect(self):
        self.__connection = connections['postgresql_khoailangdb']
        self.__cursor = self.__connection.cursor()

    def getdatas(self):
        with connections['postgresql_khoailangdb'].cursor() as _cursor:
            _cursor.execute('SELECT "USERNAME", "PASSWORD", "FULLNAME", "EMAIL", "BIRTHDAY" FROM "KL_USERS"')
            # "Return all rows from a cursor as a dict"
            _columns = [col[0] for col in _cursor.description]
            return [
                dict(zip(_columns, row))
                for row in _cursor.fetchall()
            ]

    def getallusers(self):
        with connections['postgresql_khoailangdb'].cursor() as _cursor:
            _cursor.execute('SELECT "USERNAME", "PASSWORD", "FULLNAME", "EMAIL", "BIRTHDAY" FROM "KL_USERS"')
            # "Return all rows from a cursor as a namedtuple"
            _desc = _cursor.description
            nt_result = namedtuple('Result', [col[0] for col in _desc])
            return [nt_result(*row) for row in _cursor.fetchall()]
