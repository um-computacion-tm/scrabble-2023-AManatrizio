from game.cell import Cell
from game.models import Tile


class Board:
    def __init__(self):
        # Crea un tablero de 15x15 inicializado con celdas vacías.
        self.grid = [
            [Cell() for _ in range(15)]
            for _ in range(15)
        ]
        


    # def initialize_multipliers(self):
    #     # Definimos las coordenadas de las casillas con diferentes tipos de multiplicadores
    #     double_letter_cells = [(4, 1), (12, 1), (1, 4), (8, 4), (15, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)]
    #     triple_letter_cells = [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)]
    #     double_word_cells = [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)]
    #     triple_word_cells = [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]

    #     # Iteramos a través de las filas (15) y columnas (15) del tablero
    #     for row in range(15):
    #         for col in range(15):
    #             # Verificamos el tipo de multiplicador para la casilla en esta fila y columna
    #             if (row, col) in double_letter_cells:
    #                 # Si las coordenadas están en double_letter_cells, establecemos el multiplicador en 2 y el tipo en 'Double Letter'
    #                 self.grid[row][col].multiplier = 2
    #                 self.grid[row][col].multiplier_type = 'Double Letter'
    #             elif (row, col) in triple_letter_cells:
    #                 # Si las coordenadas están en triple_letter_cells, establecemos el multiplicador en 3 y el tipo en 'Triple Letter'
    #                 self.grid[row][col].multiplier = 3
    #                 self.grid[row][col].multiplier_type = 'Triple Letter'
    #             elif (row, col) in double_word_cells:
    #                 # Si las coordenadas están en double_word_cells, establecemos el multiplicador en 2 y el tipo en 'Double Word'
    #                 self.grid[row][col].multiplier = 2
    #                 self.grid[row][col].multiplier_type = 'Double Word'
    #             elif (row, col) in triple_word_cells:
    #                 # Si las coordenadas están en triple_word_cells, establecemos el multiplicador en 3 y el tipo en 'Triple Word'
    #                 self.grid[row][col].multiplier = 3
    #                 self.grid[row][col].multiplier_type = 'Triple Word'


    def initialize_multipliers(self):
        # diccionario que relaciona los tipos de celdas con las coordenadas correspondientes
        cell_types = {
            'Double Letter': [(4, 1), (12, 1), (1, 4), (8, 4), (14, 4), (3, 7), (7, 7), (9, 7), (13, 7), (4, 10), (12, 10), (0, 12), (7, 12), (14, 12), (3, 15), (11, 15)],
            'Triple Letter': [(6, 2), (10, 2), (2, 6), (6, 6), (10, 6), (14, 6), (1, 8), (5, 8), (9, 8), (13, 8), (2, 10), (6, 10), (10, 10), (14, 10), (6, 14), (10, 14)],
            'Double Word': [(1, 1), (8, 1), (15, 1), (2, 2), (14, 2), (3, 3), (13, 3), (4, 4), (12, 4), (7, 7), (11, 7), (4, 12), (12, 12), (1, 15), (8, 15), (15, 15)],
            'Triple Word': [(0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14)]
        }

        # Iteramos a través de las filas (15) y columnas (15) del tablero
        for row in range(15):
            for col in range(15):
                # Iteramos a través del diccionario de tipos de celdas y sus coordenadas correspondientes
                for cell_type, coordinates in cell_types.items():
                    if (row, col) in coordinates:
                        # Asignamos el multiplicador basado en el tipo de celda.
                        self.grid[row][col].multiplier = 2 if 'Double' in cell_type else 3
                        self.grid[row][col].multiplier_type = cell_type
                        break






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
