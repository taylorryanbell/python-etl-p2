# Python ETL Project 2
# Taylor Bell
# 12.09.21

from pgsql import query
import sql
import requests
import json
from datetime import datetime


# Function to call API and return movie data as dictionary
def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()


# Main method
if __name__ == '__main__':
    # get some movie data from the API - FOR TEST
    # print(get_movie_data('WarGames'))

    # drop and create the schema and table
    query(sql.create_table_movie_list)

    # open and run through original json file
    only_2018_titles = []
    with open('datasets/json/movies.json', 'r') as json_file:
        given_dictionary_list = json.load(json_file)
        for movie in given_dictionary_list:
            if movie["year"] >= 2018:
                only_2018_titles.append(movie["title"])  # append only the title

    # remove duplicates by making a list of a set of the 2018 titles
    no_duplicates = list(set(only_2018_titles))

    # instantiate a dictionary to hold all data,
    # where key is movie title and value is movie dictionary
    all_data = []

    # API call that fills the dictionary with "title : movie info"
    for movie_title in no_duplicates:
        all_data.append(get_movie_data(movie_title))

    # Filter out movies with no English version
    english_only = []
    for dictionary in all_data:
        if dictionary['Response'] != 'False' and 'English' in dictionary['Language']:
            english_only.append(dictionary)

    # Remove unnecessary rows
    required_columns = []  # the list that will hold all rows with only require columns
    keys_to_keep = ["Title", "Rated", "Released", "Runtime", "Genre", "Director",
                    "Writer", "Actors", "Plot", "Awards", "Poster"]
    for movie in english_only:
        subset = {key: movie[key] for key in keys_to_keep}
        required_columns.append(subset)

    # Remove any rows missing required information, and filter for years 2018 and up
    valid_data = []
    for dictionary in required_columns:
        if ('N/A' not in dictionary.values()) and (datetime.strptime(dictionary["Released"], "%d %b %Y").year >= 2018):
            valid_data.append(dictionary)

    # Cleaning and inserting the data
    for movie in valid_data:
        # clean the runtime and lists
        movie["Runtime"] = int(movie["Runtime"].replace(' min', ''))
        movie["Genre"] = movie["Genre"].split(', ')
        movie["Writer"] = movie["Writer"].split(', ')
        movie["Actors"] = movie["Actors"].split(', ')

        # Create a list of the cleaned data for each movie
        row_list = [movie["Title"], movie["Rated"], movie["Released"], movie["Runtime"],
                    movie["Genre"], movie["Director"], movie["Writer"], movie["Actors"],
                    movie["Plot"], movie["Awards"], movie["Poster"]]

        # add the row to the table in pgSQL database
        query(sql.insert_movie, row_list)