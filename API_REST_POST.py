import requests

import requests

def post_person_details():
    url = "http://127.0.0.1:5000/person"
    payload = {
        "nome": "Mario",
        "cognome": "Rossi",
        "indirizzo": "Via Roma 1, Prato, Italia",
        "numero_di_telefono": "+39 055 1234567"
    }
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    print("Risposta POST:", data)

# Esempio di utilizzo
post_person_details()
