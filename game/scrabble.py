from game import player
from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.scrabble_logic import ScrabbleLogic
from game.exceptions import InvalidWordException, InvalidPlaceWordException
from game.dictionary import validate_word


class ScrabbleGame:

    def __init__(self, players_count):

        # Se crea un tablero (board) utilizando la clase Board
        self.board = Board()
        # Se crea una bolsa de fichas utilizando la clase BagTiles.
        self.bag_tiles = BagTiles()
        # Se crea una lista de jugadores (players) utilizando una comprensión de lista.
        # La comprensión de lista crea jugadores numerados del 1 al 'players_count'.
        self.players = [Player(i) for i in range(1, players_count + 1)]
        # Se establece al jugador actual (current_player) como el primer jugador en la lista de jugadores.
        # Esto asegura que el juego comience con el primer jugador.
        self.current_player = self.players[0]
        


    def next_turn(self):
        # Obtenemos el índice del jugador actual en la lista de jugadores (players).
        current_player_index = self.players.index(self.current_player)
        # Calculamos el índice del próximo jugador tomando el índice actual y sumando 1.
        # Utilizamos el operador '%' (módulo) para asegurarnos de que el índice esté en el rango válido de jugadores.
        next_player_index = (current_player_index + 1) % len(self.players)
        # Actualizamos el jugador actual (current_player) al siguiente jugador en la lista de jugadores.
        self.current_player = self.players[next_player_index]


    # def validate_word(self, word, location, orientation):
    #     '''
    #     1- Validar que usuario tiene esas letras
    #     2- Validar que la palabra entra en el tablero
    #     '''
        
    
    def validate_word(self, word, location, orientation):
        # Comprobar si la palabra no existe en el diccionario
        if not validate_word(word):
            # Si la palabra no existe, lanzar una excepción InvalidWordException
            raise InvalidWordException("Su palabra no existe en el diccionario")

        # Comprobar si la palabra excede los límites del tablero
        if not self.board.validate_word_inside_board(word, location, orientation):
            # Si la palabra excede los límites, lanzar una excepción InvalidPlaceWordException
            raise InvalidPlaceWordException("Su palabra excede el tablero")

        # Comprobar si la palabra está mal puesta en el tablero
        if not self.board.validate_word_place_board(word, location, orientation):
            # Si la palabra está mal puesta, lanzar una excepción InvalidPlaceWordException
            raise InvalidPlaceWordException("Su palabra esta mal puesta en el tablero")


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

        # 3. Calcular el valor de la palabra y aplicar los multiplicadores.
        word_value = ScrabbleLogic.calculate_word_value(placed_word)
        for cell in affected_cells:
            word_value += ScrabbleLogic.apply_cell_multipliers(cell, word_value)
        # 4. Agregar el valor de la palabra al puntaje del jugador actual.
        self.current_player.add_score(word_value)
        # 5. Quitar las fichas utilizadas de la mano del jugador y reponerlas de la bolsa de fichas.
        self.current_player.remove_tiles(word)
        self.current_player.add_tiles(self.bag_tiles.take(len(word)))
        # 6. Actualizar el tablero con la palabra colocada.
        self.board.update_board(placed_word, affected_cells)
        # 7. Cambiar al siguiente jugador para el próximo turno.
        self.next_turn()
        # 8. Devolver el valor de la palabra colocada.
        return word_value    