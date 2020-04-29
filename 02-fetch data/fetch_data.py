# import requests, csv, and time modules 
import requests
import csv
import time


def main():
    # list of api keys 
    api_key_list = ["c38fe68", "4d860e32", "7be429a", "29b270ab", "e55b58e3", "52eee9b0", "3d71281b", "b4108055",
                    "72144220", "5b616f3", ]
    # api calls counter
    api_calls = 0
    api_key = None
    with open('./new_movie_dataset_v2.csv', 'r', encoding='utf-8') as csv_file:
        # use built in csv.reader() and pass it the file name to read
        # will return the result in a var
        reader = csv.reader(csv_file)
        with open('new_movie_dataset_v3.csv', 'w', newline='', encoding='utf-8') as new_file:
            firstLine = True
            writer = csv.writer(new_file)
            # loop over file and print content
            for line in reader:
                if firstLine:
                    writer.writerow(line)
                    firstLine = False
                    continue
                # change api keys on certain number of calls 
                api_calls = api_calls + 1
                if api_calls < 999:
                    api_key = api_key_list[0]
                elif api_calls < 1998:
                    api_key = api_key_list[1]
                elif api_calls < 2997:
                    api_key = api_key_list[2]
                elif api_calls < 3996:
                    api_key = api_key_list[3]
                elif api_calls < 4995:
                    api_key = api_key_list[4]
                elif api_calls < 5994:
                    api_key = api_key_list[5]
                elif api_calls < 6993:
                    api_key = api_key_list[6]
                elif api_calls < 7992:
                    api_key = api_key_list[7]
                elif api_calls < 8991:
                    api_key = api_key_list[8]
                elif api_calls < 9990:
                    api_key = api_key_list[9]

                new_line = line
                movie_title = line[6]
                release_year = line[5]
                # fetch api call and handle response data 
                try:
                    apiUrl = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_title}&y={release_year}&plot=full"
                    response = requests.get(apiUrl)
                    if response.status_code == 200:
                        movie_data = response.json()
                        new_line[7] = movie_data["Director"]
                        new_line[8] = movie_data["Writer"]
                        new_line[9] = movie_data["Actors"]
                        new_line[10] = movie_data["Poster"]
                        new_line[11] = movie_data["Ratings"]
                        writer.writerow(new_line)
                        print(f"done {movie_title}")
                        time.sleep(.1)
                    else:
                        print(response)
                except:
                    print(f"failed {movie_title}")
                    new_line[7] = ''
                    new_line[8] = ''
                    new_line[9] = ''
                    new_line[10] = ''
                    new_line[11] = ''
                    writer.writerow(new_line)
                    time.sleep(.1)


if __name__ == "__main__":
    main()
