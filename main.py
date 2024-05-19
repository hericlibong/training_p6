import requests


def fetch_movie_by_directors(base_url, director_name):
    url = base_url
    filtered_movies = []
    while url :
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            movies = data['results']
            filtered_movies.extend([movie['title'] for movie in movies if director_name in movie["directors"]])
            
            
            url = data.get('next')
        else:
            print(f"Erreur : {response.status_code}")
            break

    return filtered_movies

base_url = 'http://127.0.0.1:8000/api/v1/titles/'
results_movies = fetch_movie_by_directors(base_url, 'Steven Spielberg')
print(results_movies)







# url = "http://127.0.0.1:8000/api/v1/titles/"
# response = requests.get(url)
# movies = response.json()["results"]

# filtered_movies = [movie for movie in movies if "Alexander Black" in movie["directors"]]
# print(filtered_movies)


