import tkinter as tk
import threading
import time

def create_window(width, height, title, bg_color, font_size, font_family):
    # Creare la finestra principale
    root = tk.Tk()
    
    # Impostare le dimensioni della finestra
    root.geometry(f"{width}x{height}")
    
    # Impostare il titolo della finestra
    root.title(title)
    
    # Impostare il colore di sfondo della finestra
    root.configure(bg=bg_color)
    
    # Creare una label con dimensioni e font specificati
    font = (font_family, font_size)
    label = tk.Label(root, text="Questo è un testo colorato!", fg="#FF0000", bg=bg_color, font=font)
    label.pack(pady=20)
    
    # Creare un canvas per disegnare il cerchio
    canvas = tk.Canvas(root, width=100, height=100, bg=bg_color)
    canvas.pack(pady=20)
    
    # Disegnare il cerchio (LED)
    led = canvas.create_oval(25, 25, 75, 75, fill="green")
    
    def blink_led():
        while True:
            current_color = canvas.itemcget(led, "fill")
            new_color = "red" if current_color == "green" else "green"
            canvas.itemconfig(led, fill=new_color)
            time.sleep(0.5)
    
    # Creare e avviare il thread per far lampeggiare il cerchio
    threading.Thread(target=blink_led, daemon=True).start()
    
    # Avviare il ciclo principale della finestra
    root.mainloop()

# Esempio di utilizzo
width = 400
height = 300
title = "Finestra con LED lampeggiante"
bg_color = "lightblue"
font_size = 16
font_family = "Helvetica"

create_window(width, height, title, bg_color, font_size, font_family)
