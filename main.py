import pgsql
import sql
import requests

def get_movie_data(title):
    headers = {"Authorization": "9855f49b"}
    request_url = f"https://www.omdbapi.com/?t={title}&apikey=686eed26"
    return requests.get(request_url, headers=headers).json()

if __name__ == '__main__':

    # get some movie data from the API
    print(get_movie_data('WarGames'))
