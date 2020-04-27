import csv
from datetime import datetime

with open('new_movie_dataset.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    with open('new_movie_dataset_v2.csv', 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        # loop over file line and write them to the new file
        firstLine = True
        for line in reader:
            new_line = line
            if firstLine:
                writer.writerow(new_line)
                firstLine = False
                continue
            release_date = new_line[5]
            release_year = datetime.strptime(release_date,'%d/%m/%Y')
            new_line[5] = release_year.year
            writer.writerow(new_line)
