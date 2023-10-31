from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.models import Tile
from game.dictionary import validate_word
from game.dictionary import DictionaryConnectionError
from game.dictionary_loader import load_local_dictionary
from game.scrabble_logic import ScrabbleLogic

# Ruta al archivo de tu diccionario local
local_dictionary_file = 'dictionary.txt'

# Carga el diccionario local
local_dictionary = load_local_dictionary(local_dictionary_file)

class InvalidWordException(Exception):
    def __init__(self, message="Palabra no válida"):
        self.message = message
        super().__init__(self.message)

class InvalidPlaceWordException(Exception):
    def __init__(self, message="Ubicación de palabra no válida"):
        self.message = message
        super().__init__(self.message)

class ScrabbleGame:

    def __init__(self, players_count):

        # Se crea un tablero (board) utilizando la clase Board
        self.board = Board()
        # Se crea una bolsa de fichas utilizando la clase BagTiles.
        self.bag_tiles = BagTiles()
        # Se crea una lista de jugadores numerados del 1 al 'players_count'.
        self.players = [Player(i) for i in range(1, players_count + 1)]
        # Se establece al jugador actual (current_player) como el primer jugador en la lista de jugadores.
        # Esto asegura que el juego comience con el primer jugador.
        self.current_player = self.players[0]

        self.players_want_to_end_game = [False] * players_count
        

    def draw_initial_tiles(self, player):
        # Cada jugador debe tener un conjunto inicial de fichas al comienzo del juego
        initial_tiles = self.bag_tiles.take(7)
        for tile in initial_tiles:
            player.tiles.append(tile)


    #manejo de turnos
    def next_turn(self):
        # Obtenemos el índice del jugador actual en la lista de jugadores (players).
        current_player_index = self.players.index(self.current_player)
        # Calculamos el índice del próximo jugador tomando el índice actual y sumando 1.
        # Utilizamos el operador '%' (módulo) para asegurarnos de que el índice esté en el rango válido de jugadores.
        next_player_index = (current_player_index + 1) % len(self.players)
        # Actualizamos el jugador actual (current_player) al siguiente jugador en la lista de jugadores.
        self.current_player = self.players[next_player_index]
    
    # Muestra la cantidad de fichas restantes en la bolsa de fichas
    def show_remaining_tiles_in_bag(self):
        return len(self.bag_tiles.tiles)


    @staticmethod
    def select_number_of_tiles_to_change():
        while True:
            try:
                til = int(input("Cuantas fichas quiere cambiar?: "))
                if til <= 0:
                    print("Ingrese un número positivo.")
                else:
                    return til
            except ValueError:
                print("Ingrese un número válido")

    @staticmethod
    def select_tiles_to_change(current_player, til):
        tiles_player = current_player.tiles
        tiles_to_change = []

        for _ in range(til):
            while True:
                print(f"Letras en tu mano (Jugador {current_player.player_number}): {', '.join([tile.letter for tile in tiles_player])}")
                try:
                    tile = int(input("Seleccione el número de la ficha que quiere cambiar: "))
                    if 0 <= tile < len(tiles_player):
                        tiles_to_change.append(tiles_player.pop(tile))
                        break
                    else:
                        print("Número de ficha inválido.")
                except ValueError:
                    print("Ingrese un número válido")

        return tiles_to_change

    def change_player_tiles(self, current_player):
        til = self.select_number_of_tiles_to_change()
        tiles_to_change = self.select_tiles_to_change(current_player, til)
        exchanged_tiles, new_tiles = self.exchange_tiles(current_player, tiles_to_change)
        return exchanged_tiles, new_tiles

    def exchange_tiles(self, player, letters_to_change):
        if not self.bag_tiles:
            raise ValueError("La bolsa de fichas no está disponible.")
        
        tiles_to_change, new_tiles = self.perform_tile_exchange(player, letters_to_change)
        
        return tiles_to_change, new_tiles
    
    def take_tiles_from_bag(self, count):
        if not self.bag_tiles:
            raise ValueError("La bolsa de fichas no está disponible.")
        
        new_tiles = self.bag_tiles.take(count)
        return new_tiles

    def perform_tile_exchange(self, player, letters_to_change):
        # Convierte letras a fichas
        tiles_to_change = [tile for tile in player.tiles if tile.letter in letters_to_change]
        
        # Crea un diccionario que mapea letras a la cantidad de fichas del jugador
        player_letter_counts = {}
        for tile in player.tiles:
            if tile.letter not in player_letter_counts:
                player_letter_counts[tile.letter] = 1
            else:
                player_letter_counts[tile.letter] += 1
        
        # Verifica si el jugador tiene suficientes fichas para cambiar
        for letter, count in player_letter_counts.items():
            if letters_to_change.count(letter) > count:
                raise ValueError(f"No tienes suficientes fichas de la letra '{letter}' para cambiar.")
        
        # Remueve las fichas de la mano del jugador
        for tile in tiles_to_change:
            player.tiles.remove(tile)
        
        # Devuelve las fichas cambiadas a la bolsa
        self.bag_tiles.put(tiles_to_change)
        
        # Toma las fichas nuevas de la bolsa
        new_tiles = self.bag_tiles.take(len(tiles_to_change))
        
        return tiles_to_change, new_tiles


    # Los jugadores pueden usar esta función para expresar su deseo de finalizar el juego.
    # Se llama a esta función cuando un jugador decide terminar la partida.
    def request_end_game(self, player):
            player_index = self.players.index(player)
            self.players_want_to_end_game[player_index] = True

    def is_game_over(self):
        # Condición 1: La bolsa de fichas está vacía
        if self.bag_tiles.is_empty():
            return True
        
        # Condición 2: Verificar si algún jugador desea terminar el juego
        if any(self.players_want_to_end_game):
            return True

        return False

    # def validate_word(self, word, location, orientation):
    #     '''
    #     1- Validar que usuario tiene esas letras
    #     2- Validar que la palabra entra en el tablero
    #     '''
    
    def validate_word(self, word, location, orientation):
        # Verificar si la palabra no existe en el diccionario local
        if word.lower() not in local_dictionary:
            # Si la palabra no existe en el diccionario local, lanzar una excepción InvalidWordException
            raise InvalidWordException("Su palabra no existe en el diccionario local")

        # Comprobar si la palabra no existe en el diccionario en línea
        try:
            if not validate_word(word):
                # Si la palabra no existe en el diccionario en línea, lanzar una excepción InvalidWordException
                raise InvalidWordException("Su palabra no existe en el diccionario en línea")
        except DictionaryConnectionError as e:
            # Manejar la excepción DictionaryConnectionError
            # Por ejemplo, aquí puedes buscar en el diccionario local como lo mencionaste.
            if word.lower() not in local_dictionary:
                raise InvalidWordException("Su palabra no existe en el diccionario local")

        # Comprobar si la palabra excede los límites del tablero
        if not self.board.validate_word_inside_board(word, location, orientation):
            # Si la palabra excede los límites, lanzar una excepción InvalidPlaceWordException
            raise InvalidPlaceWordException("Su palabra excede el tablero")

        # Comprobar si la palabra está mal puesta en el tablero
        if not self.board.validate_word_place_board(word, location, orientation):
            # Si la palabra está mal puesta, lanzar una excepción InvalidPlaceWordException
            raise InvalidPlaceWordException("Su palabra está mal puesta en el tablero")


    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''
    
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''


    # Método para colocar una palabra en el tablero.
    def place_word(self, word, location, orientation):
        # 1. Validar la palabra, su ubicación y orientación.
        self.validate_word(word, location, orientation)

        # 2. Obtener la palabra y las celdas afectadas en el tablero.
        placed_word, affected_cells = self.board.place_word(word, location, orientation)

        # 3. Calcular el valor de la palabra.
        word_value = self.calculate_word_value(placed_word)

        # 4. Agregar el valor de la palabra al puntaje del jugador actual.
        self.current_player.add_score(word_value)

        # 5. Actualizar el tablero con la palabra colocada.
        self.board.update_board(placed_word, affected_cells)

        # 6. Cambiar al siguiente jugador para el próximo turno.
        self.next_turn()

        # 7. Devolver el valor de la palabra colocada.
        return word_value