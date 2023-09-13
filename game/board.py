from game.cell import Cell


class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]

    def validate_word_inside_board(self, word, location, orientation):
        row, col = location

        if orientation == "H":
            if col + len(word) <= 15:
                for letter in word:
                    cell = self.grid[row][col]
                    if not cell.is_empty():
                        return False
                    col += 1
                return True
        elif orientation == "V":
            if row + len(word) <= 15:
                for letter in word:
                    cell = self.grid[row][col]
                    if not cell.is_empty():
                        return False
                    row += 1
                return True


