import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy import create_engine


cnx = create_engine('mysql+pymysql://developer:developer@localhost:3306/rec_sys').connect()


def combine_features(row):
    # return row['title'] + " " + row['keywords'] + " " + row['actors'] + " " + row['genres']
    return row['keywords'] + " " + row['actors'] + " " + row['genres']


def get_title_from_index(index, df):
    return df[df.movie_index == index]["title"].values[0]


# function gets movie index using its title
def get_index_from_title(title, df):
    return df[df.title == title]["movie_index"].values[0]


def get_recommendations(test_case):
    # df = pd.read_csv("data/compressed_movies_data.csv", encoding="utf8")
    sql = 'SELECT * FROM compressed_movies_data'
    df = pd.read_sql(sql, cnx)
    # features = ['title', 'keywords', 'actors', 'genres']
    features = ['keywords', 'actors', 'genres']

    print(df.head())
    for feature in features:
        # fillna function will fill the empty values 
        df[feature] = df[feature].fillna('')

    df["combined_features"] = df.apply(combine_features, axis=1)
    print(df["combined_features"].head())

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(df["combined_features"])
    print(count_matrix)
    cosine_sim = cosine_similarity(count_matrix)
    # print("cosine")

    movie_user_likes = test_case
    movie_index = get_index_from_title(movie_user_likes, df)

    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    recs = []
    i = 0
    # skip first element
    for element in sorted_similar_movies:
        title = get_title_from_index(element[0], df)
        print(element[1])
        recs.append(title)
        if i == 5:
            break
        i = i + 1

    return recs
