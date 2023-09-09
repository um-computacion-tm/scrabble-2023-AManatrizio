
#para el primer test
# def calculate_word_value(word):
#     # Inicializa una variable para llevar la suma de los valores de las letras en la palabra
#     total_value = 0
    
#     # Itera a través de cada celda en la palabra
#     for cell in word:
#         # Obtiene el valor de la letra de la celda y lo suma al total
#         total_value += cell.letter.value
        
    
#     return total_value

#primer y segundo test
# def calculate_word_value(word):
#     total_value = 0

#     for cell in word:
#         letter_value = cell.letter.value

#         # Verifica si hay un multiplicador de letra
#         if cell.multiplier_type == 'letter':
#             letter_value *= cell.multiplier

#         total_value += letter_value

#     return total_value


# def calculate_word_value(word):
#     total_value = 0
#     word_multiplier = 1  # Inicializamos el multiplicador de palabra en 1

#     for cell in word:
#         letter_value = cell.letter.value

#         # Verificamos si hay un multiplicador de letra
#         if cell.multiplier_type == 'letter':
#             letter_value *= cell.multiplier

#         # Verificamos si hay un multiplicador de palabra
#         if cell.multiplier_type == 'word':
#             word_multiplier *= cell.multiplier

#         total_value += letter_value

#     return total_value * word_multiplier  # Aplicamos el multiplicador de palabra al valor total



def calculate_word_value(word):
    total_value = 0
    word_multiplier = 1

    for cell in word:
        letter_value = cell.letter.value

        if cell.multiplier_type == 'letter':
            letter_value *= cell.multiplier

        total_value += letter_value

        if cell.multiplier_type == 'word':
            word_multiplier *= cell.multiplier

    return total_value * word_multiplier

