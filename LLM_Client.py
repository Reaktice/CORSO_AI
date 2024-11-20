import requests

def generate_text(prompt):
    url = "http://127.0.0.1:5000/generate"
    payload = {
        "prompt": prompt
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        data = response.json()
        print("Testo generato:", data["generated_text"])
    except requests.exceptions.JSONDecodeError as e:
        print("Errore decodifica JSON:", e)
        print("Testo di risposta:", response.text)

# Esempio di utilizzo
prompt = "Scrivi una breve poesia sulla natura."
generate_text(prompt)
