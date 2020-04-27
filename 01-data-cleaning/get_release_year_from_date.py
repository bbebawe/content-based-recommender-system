# import csv module which is used to read and write csv files 
import csv
# import datetime module which is used to split the year from the date 
from datetime import datetime
# open csv file 
with open('new_movie_dataset.csv', 'r', encoding='utf-8') as csv_file:
    # read old data file 
    reader = csv.reader(csv_file)
    with open('new_movie_dataset_v2.csv', 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        # loop over file line and write them to the new file
        firstLine = True
        for line in reader:
            new_line = line
            # skip first line form processing as it contains column names 
            if firstLine:
                writer.writerow(new_line)
                firstLine = False
                continue
            # get release date value 
            release_date = new_line[5]
            # split year from date and write it to the new file 
            release_year = datetime.strptime(release_date,'%d/%m/%Y')
            new_line[5] = release_year.year
            writer.writerow(new_line)
