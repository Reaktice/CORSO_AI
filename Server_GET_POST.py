from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/person', methods=['GET', 'POST'])
def handle_person():
    if request.method == 'GET':
        # Dati fittizi di una persona per la richiesta GET
        person = {
            "nome": "Mario",
            "cognome": "Rossi",
            "indirizzo": "Via Roma 1, Prato, Italia",
            "numero_di_telefono": "+39 055 1234567"
        }
        return jsonify(person)
    
    if request.method == 'POST':
        # Riceve i dati dal client per la richiesta POST
        data = request.json
        person = {
            "nome": data.get("nome", "N/A"),
            "cognome": data.get("cognome", "N/A"),
            "indirizzo": data.get("indirizzo", "N/A"),
            "numero_di_telefono": data.get("numero_di_telefono", "N/A")
        }
        return jsonify(person), 201  # Status code 201 per indicare che è stato creato

if __name__ == '__main__':
    app.run(debug=True)
