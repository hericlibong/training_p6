import requests
import json


token = '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'


# Définis les données nécessaires pour créer le dépôt

data = {
    "name": "training_p6",
    "description": "Juste un repo d'entraînement",
    "private": False
}


headers = {
    'Authorization':f'token {token}',
    'Accept': 'application/vnd.github.v3+json'

}

url = 'https://api.github.com/user/repos'

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())

if response.status_code == 201:
    print("Repo créé avec succès")
else:
    print("Erreur:", response.status_code)


