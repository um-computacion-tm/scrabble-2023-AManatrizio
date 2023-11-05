from game.cell import Cell
from game.models import Tile


"""
    Gestiona el tablero de juego y verifica la validez de la colocación de palabras.
    Métodos:
        - __init__(self): Constructor de la clase que inicializa un tablero 15x15 con celdas vacías.
        - initialize_multipliers(self): Inicializa los multiplicadores de celdas en el tablero de acuerdo con las reglas del juego.
        - validate_word_inside_board(self, word, location, orientation): Verifica si una palabra puede colocarse dentro del tablero en una ubicación y orientación específicas.
        - validate_word_out_of_board(self, word, location, orientation): Verifica si una palabra no puede colocarse fuera del tablero en una ubicación y orientación específicas.
        - is_empty(self): Verifica si el tablero está vacío al comprobar si la celda en la posición [7][7] está vacía.
        - validate_word_place_board(self, word, location, orientation): Verifica si una palabra puede colocarse en el tablero en una ubicación y orientación específicas.
        - show_board(board): Muestra el estado actual del tablero, pero debe llamarse como un método de instancia.
    """

class Board:
    def __init__(self):
        # Crea un tablero de 15x15 inicializado con celdas vacías.
        self.grid = [
            [Cell() for _ in range(15)]
            for _ in range(15)
        ]
        self.initialize_multipliers()

    def initialize_multipliers(self):
        # diccionario que relaciona los tipos de celdas con las coordenadas correspondientes
        cell_types = {
            'Double Letter': [(0, 3), (0, 11), (3, 0), (2, 6), (2, 8), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8,8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)],
            'Triple Letter': [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)],
            'Double Word': [(1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1)],
            'Triple Word': [(0, 0), (7, 0), (14, 0), (0, 7), (0, 14), (7, 14), (14, 14), (14, 7)],
        }

        # Iteramos a través de las filas (15) y columnas (15) del tablero
        for row in range(15):
            for col in range(15):
                # Inicializa los valores por defecto para el multiplicador de celda
                multiplier = 1
                multiplier_type = None

                # Iteramos a través del diccionario de tipos de celdas y sus coordenadas correspondientes
                for cell_type, coordinates in cell_types.items():
                    if (row, col) in coordinates:
                        # Asignamos el tipo y valor del multiplicador basado en el tipo de celda.
                        multiplier_type = 'word' if 'Word' in cell_type else 'letter'
                        multiplier = 3 if 'Triple' in cell_type else 2

                # Asignamos el multiplicador basado en el tipo de celda.
                self.grid[row][col].multiplier = multiplier
                self.grid[row][col].multiplier_type = multiplier_type



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
        return self.grid[7][7].letter is None
        
    def is_cell_empty(self, row, col):
        return self.board.grid[row][col].letter is None
    

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
    def show_board(self,board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(self.grid):
            print(
                str(row_index).rjust(2) +
                '|' +
                ' '.join([repr(cell) for cell in row])
            )