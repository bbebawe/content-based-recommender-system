from connection_pool import ConnectionPool

"""
Autocomplete class has a method get_similar_titles() which takes query as title name 
and return all movie titles from the database that are like this query 
"""


class Autocomplete:
    # create connection pool object
    connection_pool = ConnectionPool()

    def get_similar_titles(self, query):
        print("similar titles called")
        db_connection = self.connection_pool.get_pool_connection()
        cursor = db_connection.cursor(buffered=True)
        sql = """ SELECT title FROM full_movies_data WHERE title LIKE %s"""
        search_query = f"%{query}%"
        cursor.execute(sql, (search_query,))
        result = cursor.fetchall()
        titles_list = []
        for title in result:
            titles_list.append(title[0])
        # return result list to request 
        return titles_list
