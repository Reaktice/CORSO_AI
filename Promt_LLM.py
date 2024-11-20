import openai
import os

# Configura qui la tua chiave API
API_KEY = "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"
openai.api_key = API_KEY

def test_llm():
    print("Test LLM con API (Nuova versione)")
    print("Inserisci 'exit' per uscire.")
    
    while True:
        # Prendi il prompt dall'utente
        prompt = input("\nInserisci il tuo prompt: ")
        if prompt.lower() == 'exit':
            print("Chiusura del programma.")
            break

        try:
            # Chiamata API al modello Chat
            response = openai.ChatCompletion.create(
                model="davinci-002",  # Cambia con il modello desiderato
                messages=[
                    {"role": "system", "content": "Sei un assistente AI utile."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=50,  # Numero massimo di token nella risposta
                temperature=0.5,  # Controlla la creatività
            )
            
            # Mostra la risposta
            print("\nRisposta del modello:")
            print(response['choices'][0]['message']['content'].strip())
        
        except Exception as e:
            print(f"Errore durante la chiamata API: {e}")

if __name__ == "__main__":
    test_llm()
