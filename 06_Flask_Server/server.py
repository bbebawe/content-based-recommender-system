from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from flask_caching import Cache
from connection_pool import ConnectionPool
from autocomplete import Autocomplete
import engine

app = Flask(__name__)
CORS(app)

# tell Flask to use the above defined config
app.config['CACHE_TYPE'] = 'simple'
app.cache = Cache(app)

# creat connection pool object
connection_pool = ConnectionPool()
title_autocomplete = Autocomplete()


@app.cache.memoize(timeout=100)
def get_similar_titles(query):
    return title_autocomplete.get_similar_titles(query)


def get_full_recommendations_data(recs):
    result = []
    # buffered=True allows to read the result as buffered
    db_connection = connection_pool.get_pool_connection()
    cursor = db_connection.cursor(buffered=True)
    for movie in recs:
        sql = """ SELECT * FROM full_movies_data WHERE title = %s """
        cursor.execute(sql, (movie,))
        query_result = cursor.fetchone()
        result.append(query_result)

    return result


@app.cache.memoize(timeout=100)
def getRecommendations(movie):
    return engine.get_recommendations(movie.lower())


@app.route("/api/getRecs")  # route to /
def index():  # function that is linked to both / and /index
    movie = request.args.get('movie')
    print("Getting Recs for ", movie)
    recs = getRecommendations(movie)
    result = get_full_recommendations_data(recs)
    return jsonify(result)
    # return jsonify(recs)


@app.route("/api/autocomplete")
def autocomplete():
    query = request.args.get('query')
    titles = get_similar_titles(query)
    return jsonify(titles)


# this line will run the app when the script is run
if __name__ == "__main__":
    app.run(port=5000, debug=True)
