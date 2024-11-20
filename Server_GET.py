from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/person', methods=['GET'])
def get_person():
    # Dati fittizi di una persona
    person = {
        "nome": "Mario",
        "cognome": "Rossi",
        "indirizzo": "Via Roma 1, Prato, Italia",
        "numero_di_telefono": "+39 055 1234567"
    }
    return jsonify(person)

if __name__ == '__main__':
    app.run(debug=True)
