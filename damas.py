#importamos la biblioteca parte visual
import tkinter as tk

class Tablero(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x600")
        self.title("Damas Game")
        self.tablero = tk.Canvas(self, width=600, height=600)
        self.tablero.pack(fill="both", expand=1)
        self.dibujar_cuadricula()
        self.agregar_fichas()
        self.ficha_seleccionada = None
        self.turno = "negro"  # Comienza el jugador "negro"
        self.tablero.bind("<Button-1>", self.on_click)

    def dibujar_cuadricula(self):
        for i in range(6):
            for j in range(6):
                if (i + j) % 2 == 0:
                    color = "#FFE4C4"
                else:
                    color = "#8c564b"
                self.tablero.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)

    def agregar_fichas(self):
        self.fichas = []
        # add fichas black (player "black)
        for i in range(2):
            for j in range(6):
                if (i + j) % 2 != 0:
                    ficha = self.tablero.create_oval(j * 100 + 10, i * 100 + 10, (j + 1) * 100 - 10, (i + 1) * 100 - 10, fill="black")
                    self.fichas.append((ficha, "negro", i, j))
        
        # add fichas white (player "white)
        for i in range(4, 6):
            for j in range(6):
                if (i + j) % 2 != 0:
                    ficha = self.tablero.create_oval(j * 100 + 10, i * 100 + 10, (j + 1) * 100 - 10, (i + 1) * 100 - 10, fill="white")
                    self.fichas.append((ficha, "blanco", i, j))
    #visual movent of mouse 

    def on_click(self, event):
        x, y = event.x, event.y
        item = self.tablero.find_closest(x, y)
        if item:
            if self.ficha_seleccionada:
                self.tablero.itemconfig(self.ficha_seleccionada[0], outline="")
                self.mover_ficha(event)
            self.ficha_seleccionada = next((ficha for ficha in self.fichas if ficha[0] == item[0]), None)
            if self.ficha_seleccionada and self.ficha_seleccionada[1] == self.turno:
                self.tablero.itemconfig(self.ficha_seleccionada[0], outline="blue")
#movents records
    def mover_ficha(self, event):
        x, y = event.x, event.y
        row = y // 100
        col = x // 100

        if self.ficha_seleccionada:
            ficha, color, current_row, current_col = self.ficha_seleccionada
            # validate if the movement is valid
            if self.validar_movimiento(current_row, current_col, row, col, color):
                # update posicion of the records in the list
                self.fichas.remove(self.ficha_seleccionada)
                self.ficha_seleccionada = (ficha, color, row, col)
                self.fichas.append(self.ficha_seleccionada)
                # move the recorf in the table
                self.tablero.coords(ficha, col * 100 + 10, row * 100 + 10, (col + 1) * 100 - 10, (row + 1) * 100 - 10)
                # capture if posible
                self.realizar_captura(current_row, current_col, row, col, color)
                # change shift
                self.cambiar_turno()

    def cambiar_turno(self):
        # change shift of "black" and "white"
        self.turno = "blanco" if self.turno == "negro" else "negro"

    def validar_movimiento(self, current_row, current_col, new_row, new_col, color):
        # validate that the movenent is whithin the board and the box is free
        if 0 <= new_row < 6 and 0 <= new_col < 6:
            if color == "negro":
                if new_row == current_row + 1 and abs(new_col - current_col) == 1:
                    return self.casilla_libre(new_row, new_col)
                elif new_row == current_row + 2 and abs(new_col - current_col) == 2:
                    return self.casilla_libre(new_row, new_col) and self.casilla_ocupada_por_enemigo((current_row + new_row) // 2, (current_col + new_col) // 2, color)
            elif color == "blanco":
                if new_row == current_row - 1 and abs(new_col - current_col) == 1:
                    return self.casilla_libre(new_row, new_col)
                elif new_row == current_row - 2 and abs(new_col - current_col) == 2:
                    return self.casilla_libre(new_row, new_col) and self.casilla_ocupada_por_enemigo((current_row + new_row) // 2, (current_col + new_col) // 2, color)
        return False

    def casilla_libre(self, row, col):
        return not any(ficha for ficha in self.fichas if ficha[2] == row and ficha[3] == col)

    def casilla_ocupada_por_enemigo(self, row, col, color):
        return any(ficha for ficha in self.fichas if ficha[2] == row and ficha[3] == col and ficha[1] != color)

    def realizar_captura(self, current_row, current_col, new_row, new_col, color):
        # implement logic of  capture
        enemy_row = (current_row + new_row) // 2
        enemy_col = (current_col + new_col) // 2
        for ficha in self.fichas:
            _, enemy_color, row, col = ficha
            if (row, col) == (enemy_row, enemy_col) and enemy_color != color:
                # Realizar captura
                self.tablero.delete(ficha[0])
                self.fichas.remove(ficha)
                break  # Solo se puede capturar una ficha a la vez en un turno

if __name__ == "__main__":
    app = Tablero()
    app.mainloop()
