from game.models import Tile

class Cell:
    def __init__(self, letter=None, multiplier=1, multiplier_type=None, multiplier_active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.multiplier_active = multiplier_active
        self.letter = letter

    def is_empty(self) -> bool:
        return self.letter is None

    def add_letter(self, letter: Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_active:
            if self.multiplier_type == 'letter':
                return self.letter.value * self.multiplier
            else:
                return self.letter.value
        else:
            return self.letter.value  # No aplicar el multiplicador cuando no está activo
