from openai import OpenAI
import os


# Configura qui la tua chiave API

#API_KEY = "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"
#openai.api_key = API_KEY

client = OpenAI(
    api_key = "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"
)
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
            response = client.chat.completions.create(
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
