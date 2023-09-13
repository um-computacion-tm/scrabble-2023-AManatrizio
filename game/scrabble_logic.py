from game.cell import Cell

def calculate_word_value(word):
    total_value = 0
    word_multiplier = 1

    for cell in word:
        cell_value = 0

        if cell.letter is not None:
            cell_value = cell.letter.value

            if cell.multiplier_type == 'letter':
                cell_value *= cell.multiplier
            elif cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier

        total_value += cell_value

    return total_value * word_multiplier


