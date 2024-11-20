from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/person', methods=['POST'])
def create_person():
    # Riceve i dati dal client
    data = request.json
    
    # Crea una risposta con i dati ricevuti
    person = {
        "nome": data.get("nome", "N/A"),
        "cognome": data.get("cognome", "N/A"),
        "indirizzo": data.get("indirizzo", "N/A"),
        "numero_di_telefono": data.get("numero_di_telefono", "N/A")
    }
    return jsonify(person), 201  # Status code 201 per indicare che è stato creato

if __name__ == '__main__':
    app.run(debug=True)
