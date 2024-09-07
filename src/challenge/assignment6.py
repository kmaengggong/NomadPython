# BLUEPRINT | DONT EDIT

import requests

movie_ids = [
    238, 680, 550, 185, 641, 515042, 152532, 120467, 872585, 906126, 840430
]

# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:

uri = "https://nomad-movies.nomadcoders.workers.dev/movies"

for id in movie_ids:
    response = requests.get(f"{uri}/{id}")
    data = response.json()
    print(f"title: {data['title']}")
    print(f"overview: {data['overview']}")
    print(f"vote_average: {data['vote_average']}")
    print()

# /YOUR CODE
