import tkinter as tk

def concatena_stringhe():
    # Ottieni il contenuto delle due text box
    stringa1 = text_box1.get("1.0", tk.END).strip()
    stringa2 = text_box2.get("1.0", tk.END).strip()
    
    # Concatenazione delle stringhe
    risultato = stringa1 + " " + stringa2
    
    # Inserisci il risultato nella text box di output
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, risultato)

# Creazione della finestra principale
root = tk.Tk()
root.title("Concatenazione di Stringhe")
root.geometry("800x600")  # Imposta la dimensione della finestra

# Creazione della cornice per il contenuto
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Label e text box di input per la Stringa 1
label1 = tk.Label(frame, text="Stringa 1")
label1.pack(anchor='w')
text_box1 = tk.Text(frame, height=1, width=50)
text_box1.pack(pady=5)

# Label e text box di input per la Stringa 2
label2 = tk.Label(frame, text="Stringa 2")
label2.pack(anchor='w')
text_box2 = tk.Text(frame, height=1, width=50)
text_box2.pack(pady=5)

# Spazio tra le text box di input e la text box di output
spacer = tk.Label(frame, text="")
spacer.pack(pady=10)

# Creazione della text box di output
output_box = tk.Text(frame, height=1, width=50)
output_box.pack(pady=5)

# Creazione del pulsante
btn_concatena = tk.Button(frame, text="Concatenare", command=concatena_stringhe)
btn_concatena.pack(pady=10)

# Avvio del loop principale di tkinter
root.mainloop()
