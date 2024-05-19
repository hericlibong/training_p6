import requests

def fetch_movie_titles_by_year(base_url):
    """Récupérer les films de la liste par année"""
    url = base_url
    #params =  {'years': year}
    movies_titles = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results']:
                movies_titles.append(movie['title'])
            url = data.get('next')
            # params = {}
        else:
            print(f"Erreur: {response.status_code}")
            break
    
    return movies_titles

base_url = 'http://127.0.0.1:8000/api/v1/titles/?year=2020'
#year = 2018
titles = fetch_movie_titles_by_year(base_url)
print(titles)