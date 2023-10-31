from pyrae import dle


class DictionaryConnectionError(Exception):
    pass

dle.set_log_level(log_level='CRITICAL')

def validate_word(word: str) -> bool: 
    search = dle.search_by_word(word=word)
    if search is None:
        raise DictionaryConnectionError()
    return search.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'