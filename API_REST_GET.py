import requests

def get_person_details():
    url = "http://127.0.0.1:5000/person"
    response = requests.get(url)
    data = response.json()
    print("Dati della persona:", data)

# Esempio di utilizzo
get_person_details()
