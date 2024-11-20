import tkinter as tk

def calcola_somma():
    # Ottieni il contenuto delle due text box e convertilo in numeri
    numero1 = float(text_box1.get("1.0", tk.END).strip())
    numero2 = float(text_box2.get("1.0", tk.END).strip())
    
    # Calcola la somma dei due numeri
    somma = round(numero1,2) + round(numero2,2)
    
    # Inserisci il risultato nella text box di output
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, str(somma))

# Creazione della finestra principale
root = tk.Tk()
root.title("Calcolo della Somma di Due Numeri")
root.geometry("800x600")  # Imposta la dimensione della finestra

# Creazione della cornice per il contenuto
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

# Label e text box di input per il Numero 1
label1 = tk.Label(frame, text="Numero 1")
label1.pack(anchor='w')
text_box1 = tk.Text(frame, height=1, width=50)
text_box1.pack(pady=5)

# Label e text box di input per il Numero 2
label2 = tk.Label(frame, text="Numero 2")
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
btn_calcola = tk.Button(frame, text="Calcola Somma", command=calcola_somma)
btn_calcola.pack(pady=10)

# Avvio del loop principale di tkinter
root.mainloop()


""""

# Tipi di Dati Numerici

# int: Intero
numero_intero = int(3.14)  # Converte un numero in un intero (troncando i decimali)

# float: Numero a virgola mobile
numero_virgola_mobile = float(3)  # Converte un numero in un float

# complex: Numero complesso
numero_complesso = complex(1, 2)  # Crea un numero complesso (1 + 2j)

# Funzioni e Metodi Utili per Numeri

# round(): Arrotonda un numero al numero di decimali specificato
arrotondato = round(3.14159, 2)  # Output: 3.14

# abs(): Valore assoluto di un numero
valore_assoluto = abs(-5)  # Output: 5

# divmod(): Restituisce una tupla con il quoziente e il resto
quoziente, resto = divmod(10, 3)  # Output: (3, 1)

# pow(): Eleva un numero alla potenza di un altro numero
potenza = pow(2, 3)  # Output: 8

# sum(): Somma di tutti gli elementi in un iterabile
somma = sum([1, 2, 3, 4])  # Output: 10

# max(): Massimo tra tutti gli elementi in un iterabile
massimo = max(1, 5, 3)  # Output: 5

# min(): Minimo tra tutti gli elementi in un iterabile
minimo = min(1, 5, 3)  # Output: 1

# Conversioni di Tipo

# str(): Converte un numero in una stringa
stringa = str(123)  # Output: "123"

# hex(): Converte un numero intero in una stringa esadecimale
esadecimale = hex(255)  # Output: "0xff"

# oct(): Converte un numero intero in una stringa ottale
ottale = oct(8)  # Output: "0o10"

# bin(): Converte un numero intero in una stringa binaria
binario = bin(3)  # Output: "0b11"

# Operazioni Matematiche Avanzate (Modulo math)

import math

# math.sqrt(): Radice quadrata
radice_quadrata = math.sqrt(16)  # Output: 4.0

# math.log(): Logaritmo naturale (base e)
logaritmo_naturale = math.log(10)  # Output: 2.302585092994046

# math.sin(), math.cos(), math.tan(): Funzioni trigonometriche
seno = math.sin(math.pi / 2)  # Output: 1.0

# math.ceil(): Arrotonda un numero verso l'alto
arrotondato_su = math.ceil(4.2)  # Output: 5

# math.floor(): Arrotonda un numero verso il basso
arrotondato_giu = math.floor(4.8)  # Output: 4

"""