#en esta clase se carga el diccionario local
def load_local_dictionary(dictionary_file):
    local_dictionary = set()

    with open(dictionary_file, 'r') as file:
        for line in file:
            # Agregar cada palabra del archivo a un conjunto
            word = line.strip().lower()
            local_dictionary.add(word)

    return local_dictionary