import json
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # This is to load your API keys from .env

TMDB_TRENDING_PATH = 'trending/tv/week'
TMDB_SEARCH_API_REQUEST = f'https://api.themoviedb.org/3/{TMDB_TRENDING_PATH}?'

#def get_top_10_weekly_trending_shows():
response = requests.get(
    TMDB_SEARCH_API_REQUEST,
    params={
        'api_key': os.getenv('TMDB_API_KEY')
    }
)
# Encodes response into a python json dictionary.
json_data = response.json()
#print(json_data)

# Convert json_data to a formatted pretty
# json string that is easy for humans to read.
# Mouse over function to get definition of indent and sort_keys
#pretty_json_data = json.dumps(json_data, indent=4, sort_keys=True)
#print(pretty_json_data)

tv_shows = json_data['results']

# Add Parsing Code Here

# Print out the response data (tv shows) in formatted form:
# names, popularity, vote_count
show_data = []
for show in tv_shows:
    data = {
        'name': show['name'],
        'popularity': show['popularity'],
        'vote_count': show['vote_count'],
        'vote_average': show['vote_average']
    }
    show_data.append(data)
    print("----------------------------------\n")
    print(f'Name: "{show["name"]}"')
    print(f'Popularity: {show["popularity"]}')
    print(f"Vote count: {show['vote_count']}\n")


# Sort and print out the following in formatted form:
# names and vote_average (in-order of average)

# Sort the list of show data by vote_average key in descending order
sorted_show_data = sorted(show_data, key=lambda x: x['vote_average'], reverse=True)
print('++++++++++++_AVERAGE_VOTES_++++++++++++\n')
# Print out the sorted data 
for show in sorted_show_data:
    print(f'Name: "{show["name"]}".....Vote average: {show["vote_average"]}\n')
