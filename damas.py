import tkinter as tk

class Tablero(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x600")
        self.title("Damas Game")
        self.Tablero = tk.Canvas(self, width=600, height=600)
        self.Tablero.pack(fill="both", expand=1)
        self.cuadrado()
        self.add_game_tokens()  # Llamar a la función para agregar fichas

    def cuadrado(self):
        for i in range(6):  #6 para filas del tablero de damas
            for j in range(6):  # 6 para columnas del tablero de damas
                if (i + j) % 2 == 0:
                    color = "#FFE4C4"  # Color claro
                else:
                    color = "#8c564b"  # Color oscuro
                self.Tablero.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)

    def add_game_tokens(self):
        # Fichas claras
        for i in range(2):  # Primeras 2 filas
            for j in range(6):  # 6 columnas
                if (i +j) % 2 == 0:  # Casillas oscuras
                    color = "#F0E6C4"  # Color de las fichas claras
                    self.Tablero.create_oval(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)

        # Fichas negras
        for i in range(4, 6):  # Últimas 2 filas
            for j in range(6):  #  6  columnas
                if (i + j) % 2 == 0:  # Casillas oscuras
                    color = "#000000"  # Color de las fichas negras
                    self.Tablero.create_oval(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)

if __name__ == "__main__":
    app = Tablero()
    app.mainloop()
