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
        colors = ["red", "green", "blue", "yellow"]
        for i in colors:
            button = tk.Canvas(self.master, bg=i, width=100, height=100, highlightthickness=1, relief="raised")
            button.bind("<Button-1>", self.player_input)        # "<Button-1>" es por defecto en tkinter. Bind asocia el botón izquierdo a la función.
            button.pack(side=tk.LEFT, padx=10, pady=10)
            self.buttons.append(button)
        self.score_label = tk.Label(self.master, text=f"Puntaje: {self.score}")
        self.score_label.pack()
        print(*colors[i:i+2])

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

    def check_sequence(self):
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
