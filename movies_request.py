import requests

# url = "http://127.0.0.1:8000/api/v1/titles/?year=2020"
# #params = {"years": 2018}
# response = requests.get(url)


# if response.status_code == 200:
#     data = response.json()
#     films = data["results"]
#     print(films[0]["title"])
#     print(films[0]['actors'])
    
# else :
#     print(f"Erreur : {response.status_code}")

def fetch_movies(base_url):
    """Récupère tous les films de la liste"""
    url = base_url
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for movie in data['results']:
                titles = movie['title']
                print(titles)
            url = data.get('next')
        else:
            print(f"Erreur : {response.status_code}")
            break

base_url = 'http://127.0.0.1:8000/api/v1/titles/?year=2020'
fetch_movies(base_url)




            


