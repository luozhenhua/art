#!/usr/bin/env python
#
# this is the class for database connection and operation
#

import MySQLdb


db_config = {
  'user': 'arts',
  'password': 'arts',
  'host': '127.0.0.1',
  'database': 'arts',
}


class Mysql():

    def __init__(self, config=None):
        self.conf = db_config
        self.user = self.conf["user"]
        self.pwd = self.conf["password"]
        self.host = self.conf["host"]
        self.database = self.conf["database"]
        self.db = None

    def connect(self):
        try:
            self.db = MySQLdb.connect(self.host, self.user, self.pwd, self.database)
        except:
            print("Connect to database failed!!!")

    def query(self):
        try:
            # prepare a cursor object using cursor() method
            cursor = self.db.cursor()

            # execute SQL query using execute() method.
            cursor.execute("SELECT VERSION()")

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()

            print("Database version : %s " % data)
        except:
            print("Connect to database failed!!!")

    def disconnect(self):
        self.db.close()

