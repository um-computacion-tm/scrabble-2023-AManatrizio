from game.cell import Cell
from game.models import Tile


class Board:
    def __init__(self):
        # Crea un tablero de 15x15 inicializado con celdas vacías.
        self.grid = [
            [Cell() for _ in range(15)]
            for _ in range(15)
        ]
        self.initialize_multipliers()  # Llama a la función para inicializar los multiplicadores


    def initialize_multipliers(self):
        # Creamos un diccionario que mapea las coordenadas de las casillas con los tipos y valores de multiplicadores.
        multipliers = {
            (4, 1): ('Double Letter', 2),  # Casilla de Doble Letra con valor 2
            (12, 1): ('Double Letter', 2),  
            (1, 4): ('Double Letter', 2),
            (8, 4): ('Double Letter', 2),
            (15, 4): ('Double Letter', 2),
            (3, 7): ('Double Letter', 2),
            (7, 7): ('Double Letter', 2),
            (9, 7): ('Double Letter', 2),
            (13, 7): ('Double Letter', 2),
            (4, 10): ('Double Letter', 2),
            (12, 10): ('Double Letter', 2),
            (0, 12): ('Double Letter', 2),
            (7, 12): ('Double Letter', 2),
            (14, 12): ('Double Letter', 2),
            (3, 15): ('Double Letter', 2),
            (11, 15): ('Double Letter', 2),
            (6, 2): ('Triple Letter', 3),  # Casilla de Triple Letra con valor 3
            (10, 2): ('Triple Letter', 3),  
            (2, 6): ('Triple Letter', 3),
            (6, 6): ('Triple Letter', 3),
            (10, 6): ('Triple Letter', 3),
            (14, 6): ('Triple Letter', 3),
            (1, 8): ('Triple Letter', 3),
            (5, 8): ('Triple Letter', 3),
            (9, 8): ('Triple Letter', 3),
            (13, 8): ('Triple Letter', 3),
            (2, 10): ('Triple Letter', 3),
            (6, 10): ('Triple Letter', 3),
            (10, 10): ('Triple Letter', 3),
            (14, 10): ('Triple Letter', 3),
            (6, 14): ('Triple Letter', 3),
            (10, 14): ('Triple Letter', 3),
            (1, 1): ('Double Word', 2),  # Casilla de Doble Palabra con valor 2
            (8, 1): ('Double Word', 2),  
            (15, 1): ('Double Word', 2),
            (2, 2): ('Double Word', 2),
            (14, 2): ('Double Word', 2),
            (3, 3): ('Double Word', 2),
            (13, 3): ('Double Word', 2),
            (4, 4): ('Double Word', 2),
            (12, 4): ('Double Word', 2),
            (7, 7): ('Double Word', 2),
            (11, 7): ('Double Word', 2),
            (4, 12): ('Double Word', 2),
            (12, 12): ('Double Word', 2),
            (1, 15): ('Double Word', 2),
            (8, 15): ('Double Word', 2),
            (15, 15): ('Double Word', 2),
            (0, 0): ('Triple Word', 3),  # Casilla de Triple Palabra con valor 3
            (7, 0): ('Triple Word', 3),  
            (14, 0): ('Triple Word', 3),
            (0, 7): ('Triple Word', 3),
            (14, 7): ('Triple Word', 3),
            (0, 14): ('Triple Word', 3),
            (7, 14): ('Triple Word', 3),
            (14, 14): ('Triple Word', 3),
        }

        # Iteramos a través del diccionario y asignamos los valores de los multiplicadores a las casillas del tablero.
        for (row, col), (multiplier_type, multiplier) in multipliers.items():
            self.grid[row][col].multiplier_type = multiplier_type
            self.grid[row][col].multiplier = multiplier



    def validate_word_inside_board(self, word, location: tuple, orientation):
        # Extraer las coordenadas de la ubicación y la longitud de la palabra
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)

        # Convertir la orientación a mayúsculas para que sea insensible a mayúsculas/minúsculas
        orientation = orientation.upper()

        if orientation == "H":  # Si la orientación es horizontal
            if position_x + len_word <= 15 and position_y <= 15:  # Verificar si la palabra cabe en el eje X (columnas)
                return True
        elif orientation == "V":  # Si la orientación es vertical
            if position_y + len_word <= 15 and position_x <= 15:  # Verificar si la palabra cabe en el eje Y (filas)
                return True

        return False  # Si no se cumple ninguna de las condiciones, la palabra no cabe en el tablero


    def validate_word_out_of_board(self, word, location, orientation):
        # niega el resultado de validate_word_inside_board
        return not self.validate_word_inside_board(word, location, orientation)
    
   
# metodo para verificar si la celda en la posición [7][7] está vacía, entonces el tablero esta vacio.
    def is_empty(self):
        if self.grid[7][7].letter is None:
            return True
        else:
            return False
        
    def validate_word_place_board(self, word, location: tuple, orientation):
        len_word = len(word)
        row = location[0]
        col = location[1]

        if orientation == "H":
            if len_word + col <= 15:
                return True  # La palabra cabe horizontalmente en el tablero
        elif orientation == "V":
            if len_word + row <= 15:
                return True  # La palabra cabe verticalmente en el tablero

        return False  # La palabra no cabe en el tablero

            

#metodo que muestra el tablero
    def show_board(board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )
