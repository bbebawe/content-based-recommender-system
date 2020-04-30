import csv

with open('new_movie_dataset_v4.csv', 'r', encoding='latin-1') as csv_file:
    reader = csv.reader(csv_file)

    with open('new_movie_dataset_v5.csv', 'w', encoding='latin-1', newline='') as new_file:
        csv_writer = csv.writer(new_file)
        firstLine = True
        for line in reader:
            # construct new line from certain columns [index, title, geners, director, writer, actors, keywords]
            new_line = line
            # skip first line which is column names
            if firstLine:
                csv_writer.writerow(new_line)
                firstLine = False
                continue
            new_line[6] = line[6].lower()
            # remove spaces and makes the words unique 
            new_line[7] = line[7].replace(" ", "").lower()
            new_line[8] = line[8].replace(" ", "").lower()
            new_line[9] = line[9].replace(" ", "").lower()
            csv_writer.writerow(new_line)
