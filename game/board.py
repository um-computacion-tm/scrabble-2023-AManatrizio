from game.cell import Cell
from game.models import Tile


class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]

    def validate_word_inside_board(self, word, location: tuple, orientation):
        # Extraer las coordenadas de la ubicación y la longitud de la palabra
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)

        # Convertir la orientación a mayúsculas para que sea insensible a mayúsculas/minúsculas
        orientation = orientation.upper()

        if orientation == "H":  # Si la orientación es horizontal
            if position_x + len_word > 15:  # Verificar si la palabra se desborda en el eje X (columnas)
                return False
            elif position_y + len_word > 1:  # Verificar si la palabra se desborda en el eje Y (filas)
                return True
        elif orientation == "V":  # Si la orientación es vertical
            if position_y + len_word > 15:  # Verificar si la palabra se desborda en el eje Y (filas)
                return False
            elif position_x + len_word > 1:  # Verificar si la palabra se desborda en el eje X (columnas)
                return True

        return False  # Si la orientación no es válida o no se cumple ninguna condición

    def validate_word_out_of_board(self, word, location, orientation):
        # niega el resultado de validate_word_inside_board
        return not self.validate_word_inside_board(word, location, orientation)
    
   

    def is_empty(self):
        # Verifica si todos los elementos en el tablero son espacios en blanco
        for row in self.board:
            for cell in row:
                if cell != ' ':
                    return False
        return True



    def validate_word_place_board(self, word, location: tuple, orientation):
        len_word = len(word)
        row = location[0]
        col = location[1]
        if orientation == "H":
            return len_word +  col <= 14
        if orientation == "H":
            return len_word +  col > 14