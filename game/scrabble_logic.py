def calculate_word_value(word):
    # Inicializa una variable para llevar la suma de los valores de las letras en la palabra
    total_value = 0
    
    # Itera a través de cada celda en la palabra
    for cell in word:
        # Obtiene el valor de la letra de la celda y lo suma al total
        total_value += cell.letter.value
    
    return total_value