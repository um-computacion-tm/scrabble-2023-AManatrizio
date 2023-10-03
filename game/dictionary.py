#En esta clase se importa el diccionario de la API, para validar las palabras

from pyrae import dle

class DictionaryConnectionError(Exception):
    ...

dle.set_log_level(log_level='CRITICAL')

def validate_word(word):
    search = dle.search_by_word(word=word)
    if search is None:
        raise DictionaryConnectionError()
    return search.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'







# class Validate_word:

#     #constructor
#     def __init__(self):
#         pass 

#     def validate_word(self, palabra):
#         # Lógica para validar la palabra utilizando la API pyrae
#         try:
#             # Realizar una búsqueda en la API
#             resultado = dle.search_by_word(word=palabra)
#             # Procesar el resultado y determinar si la palabra es válida
#             es_valida = self.procesar_resultado(resultado)
#             return es_valida
#         except Exception as e:
#             print(f"Error al validar la palabra: {e}")
#             return False

#     def procesar_resultado(self, resultado):
#         # Aquí puedes analizar el resultado de la búsqueda y determinar si la palabra es válida
#         # Por ejemplo, puedes verificar si la palabra tiene una definición en el diccionario
#         definiciones = resultado.get_definitions()
#         return bool(definiciones)
