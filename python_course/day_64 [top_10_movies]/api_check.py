import requests

APIKEY = '7575b562bc49ab6cf76fc6dd10326118'
movie = input("Enter movie: ")
SEARCH_API_ENDPOINT = 'https://api.themoviedb.org/3/search/movie'
search_parameters = {
    'api_key': APIKEY,
    'query': movie
}

response = requests.get(url=SEARCH_API_ENDPOINT, params=search_parameters)
response.raise_for_status()
data = response.json()['results']

print(data)

# movie_id = 624860
# TMDB_API_ENDPOINT = f'https://api.themoviedb.org/3/movie/{movie_id}'
# TMDB_parameters = {
#     'api_key':APIKEY,
# }
# response2 = requests.get(url=TMDB_API_ENDPOINT, params=TMDB_parameters)
# response2.raise_for_status()
# movie_data = response2.json()
# print()