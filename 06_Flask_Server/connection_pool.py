import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling

"""
ConnectionPool class is used to create connection pool to the database 
"""


class ConnectionPool:
    HOST = 'localhost'
    USER = 'developer'
    PASSWORD = 'developer'
    DATABASE = 'rec_sys'

    def get_pool_connection(self):
        try:
            connection_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="recs_pool",
                                                                          pool_size=5,
                                                                          pool_reset_session=True,
                                                                          host=self.HOST,
                                                                          database=self.DATABASE,
                                                                          user=self.USER,
                                                                          password=self.PASSWORD)
            connection = connection_pool.get_connection()
            db_info = connection.get_server_info()
            print("Connected to MySQL database using connection pool ", db_info)
            return connection
        except Error:
            print("Error Connection to Database", Error)
