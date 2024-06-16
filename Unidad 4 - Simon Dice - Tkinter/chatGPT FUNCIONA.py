import tkinter as tk
import random
import json
from tkinter import simpledialog, messagebox

class SimonGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Simon Game")
        self.sequence = []
        self.player_sequence = []
        self.buttons = []
        self.score = 0
        self.player_name = simpledialog.askstring("Nombre", "Ingrese su nombre:")
        self.create_widgets()
        self.start_game()

    def create_widgets(self):
            rows = 2  # Número de filas
            cols = 2  # Número de columnas (ajustado a 2 para una matriz 2x2)
            colors = ["red", "green", "blue", "yellow"]  # Lista de colores

            for i, color in enumerate(colors):
                row = i // cols # Calcula la fila
                col = i % cols  # Calcula la columna
                button = tk.Canvas(self.master, bg=color, width=100, height=100, highlightthickness=3, relief="groove")
                button.bind("<Button-1>", self.player_input)
                button.grid(row=row, column=col, padx=20, pady=20)
                self.buttons.append(button)

            # Ajustamos la fila para la etiqueta de puntuación
            self.score_label = tk.Label(self.master, text="\nMarcador: 0  Mayor puntaje: 0") # Se coloca en 0 porque ya se sabe en qué valor INICIA.
            opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
            self.score_label.place(x=100, anchor=tk.N, width=100, height=50)
            #self.score_label = tk.Label(self.master, text=f"Puntaje: {self.score}")
            #self.score_label.grid(row=rows, column=0, columnspan=cols, pady=10)

        


    def start_game(self):
        self.sequence.clear()
        self.player_sequence.clear()
        self.next_round()

    def next_round(self):
        self.player_sequence.clear()
        self.sequence.append(random.choice(self.buttons))
        self.flash_sequence()

    def flash_sequence(self):
        for i, button in enumerate(self.sequence):
            self.master.after(1000 * i, lambda b=button: self.flash_button(b))

    def flash_button(self, button):
        original_color = button.cget("bg")
        button.config(bg="white")
        self.master.after(500, lambda: button.config(bg=original_color))

    def player_input(self, event):
        clicked_button = event.widget
        self.player_sequence.append(clicked_button)
        self.check_sequence()

    def check_sequence(self):                                                           # fijate esto pacheco pal jeison q hayan mas de 1 coso
        if self.player_sequence != self.sequence[:len(self.player_sequence)]:
            messagebox.showinfo("Game Over", f"Incorrecto! Puntaje: {self.score}")
            self.save_score()
            self.start_game()
        elif len(self.player_sequence) == len(self.sequence):
            self.score += 1
            self.score_label.config(text=f"Puntaje: {self.score}")
            self.master.after(1000, self.next_round)

#jeison
    def save_score(self):
        data = {
            "name": self.player_name,
            "score": self.score
        }
        with open("pysimonpuntajes.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

if __name__ == "__main__":
    root = tk.Tk()
    game = SimonGame(root)
    root.mainloop()
