from game.cell import Cell
from game.models import Tile

class ScrabbleLogic:
    @staticmethod
    def calculate_word_value(word):
        # Inicializar las variables para el valor total y el multiplicador de palabra
        total_value = 0
        word_multiplier = 1

        # Inicializar una bandera para rastrear si hay un multiplicador de letra activo
        letter_multiplier_active = False

        # Recorrer cada celda en la palabra
        for cell in word:
            cell_value = 0

            # Si la celda contiene una letra
            if cell.letter is not None:
                cell_value = cell.letter.value

                # Verificar el tipo de multiplicador (letra o palabra)
                if cell.multiplier_type == 'letter':
                    if cell.multiplier_active:
                        cell_value *= cell.multiplier
                    else:
                        # Si el multiplicador de letra no está activo, indicarlo
                        letter_multiplier_active = True
                elif cell.multiplier_type == 'word':
                    # Aplicar el multiplicador de palabra
                    word_multiplier *= cell.multiplier

            # Agregar el valor de la celda al valor total
            total_value += cell_value

        # Si no hay multiplicador de letra activo, aplicar el multiplicador de palabra al valor total
        if not letter_multiplier_active:
            total_value *= word_multiplier

        # Devolver el valor total de la palabra
        return total_value




