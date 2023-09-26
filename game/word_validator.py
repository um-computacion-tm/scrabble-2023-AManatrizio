from pyrae import RAE
from pyrae import dle


class WordValidator:

    #constructor
    def __init__(self):
        pass 

    def validate_word(self, palabra):
        # Lógica para validar la palabra utilizando la API pyrae
        try:
            # Realizar una búsqueda en la API
            resultado = dle.search_by_word(word=palabra)
            # Procesar el resultado y determinar si la palabra es válida
            es_valida = self.procesar_resultado(resultado)
            return es_valida
        except Exception as e:
            print(f"Error al validar la palabra: {e}")
            return False

    def procesar_resultado(self, resultado):
        # Aquí puedes analizar el resultado de la búsqueda y determinar si la palabra es válida
        # Por ejemplo, puedes verificar si la palabra tiene una definición en el diccionario
        definiciones = resultado.get_definitions()
        return bool(definiciones)
