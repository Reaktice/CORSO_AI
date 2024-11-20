from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Configura la tua chiave API di OpenAI
openai.api_key = "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"

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    print(f"Ricevuto prompt: {prompt}")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    print("Risposta OpenAI:", response)

    generated_text = response['choices'][0]['message']['content'].strip()
    return jsonify({"generated_text": generated_text})

if __name__ == '__main__':
    app.run(debug=True)
