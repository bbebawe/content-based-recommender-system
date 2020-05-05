# import pandas and sklearn modules
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# function gets movie title using its index
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


# function gets movie index using its title
def get_index_from_title(title):
    return df[df.title == title]["movie_index"].values[0]


##################################################

# Step 1: Read CSV File and store it into DataFrame (df)
df = pd.read_csv("compressed_movie_dataset_v5.csv",  encoding="latin-1")


##################################################

# Step 2: Select Features to base CB-RecSys
# features = ['title', 'keywords', 'actors', 'genres']
features = ['keywords', 'actors', 'genres']

##################################################

# Step 3: Create a column in Data Frame which combines all selected features

# clean the data and remove invalid values and fill them with empty string
for feature in features:
    df[feature] = df[feature].fillna('')


# function to combine movie features in one row (vector)
def combine_features(row):
    # return row['title'] + " " + row['keywords'] + " " + row['actors'] + " " + row['genres']
    return row['keywords'] + " " + row['actors'] + " " + row['genres']


# apply combine features function to data frame, axis to combine vertically
df["combined_features"] = df.apply(combine_features, axis=1)


#################################################

# Step 4: Create count matrix from this new combined column
# built in class used to represent text as vectors 
vectorizer = CountVectorizer()

# fit the data to train the vectorizer to count the words
count_matrix = vectorizer.fit_transform(df["combined_features"])

##################################################

# Step 5: Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

# test case
movie_user_likes = "ex machina".lower()

##################################################

# Step 6: Get index of this movie from its title
movie_index = get_index_from_title(movie_user_likes)

# find similar movies similar to the move that user liked
# enumerate function loops throw list and return the item as well as its index
# enumerate will return list of tuple with index and cosine similarly
similar_movies = list(enumerate(cosine_sim[movie_index]))

# print(similar_movies)
##################################################

# Step 7: Get a list of similar movies in descending order of similarity score
# takes lambda function to sort movies
sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
# print(sorted_similar_movies)

##################################################

# Step 8: Print titles of first 10 movies
print("----- Recommendations For", movie_user_likes)
i = 0
# skip first element
for element in sorted_similar_movies:
    i = i + 1
    if i == 1:
        continue
    print(get_title_from_index(element[0]))
    print(element)
    if i > 5:
        break

# evaluation
