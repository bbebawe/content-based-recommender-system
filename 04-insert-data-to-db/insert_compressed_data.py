import csv
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="developer",
    passwd="developer",
    database="rec_sys"  
)
with open('new_movie_dataset_v5.csv', 'r', encoding='latin-1') as csv_file:
    reader = csv.reader(csv_file)
    firstLine = True
    for line in reader:
        new_line = line
        cursor = db.cursor()
        if firstLine:
            firstLine = False
            continue
        sql = """ INSERT INTO compressed_movies_data(movie_index, genres, keywords, production_year, title, director,writer,actors)
                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s )"""
        values = (
            new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], new_line[5], new_line[6], new_line[7])
        cursor.execute(sql, values)
        db.commit()
        # print(cursor)
