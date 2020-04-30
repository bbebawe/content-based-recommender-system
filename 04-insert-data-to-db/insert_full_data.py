import csv
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="developer",
    passwd="developer",
    database="rec_sys"  # this is optional
)
with open('full_new_movie_dataset_v4.csv', 'r', encoding='latin-1') as csv_file:
    reader = csv.reader(csv_file)
    firstLine = True
    for line in reader:
        new_line = line
        cursor = db.cursor()
        if firstLine:
            firstLine = False
            continue
        sql = """ INSERT INTO full_movies_data(movie_index, genres, homepage, keywords, overview ,production_year, title, director,writer,actors, poster, ratings)
                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (
            new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], new_line[5], new_line[6], new_line[7],
            new_line[8], new_line[9], new_line[10], new_line[11])
        cursor.execute(sql, values)
        db.commit()
        # print(cursor)
