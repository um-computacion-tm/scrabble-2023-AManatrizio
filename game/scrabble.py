from game.board import Board
from game.player import Player
from game.models import BagTiles


class ScrabbleGame:

    # def __init__(self, players_count: int):
    #     self.board = Board()
    #     self.bag_tiles = BagTiles()
    #     self.players:list[Player] = []
    #     for _ in range(players_count):
    #         self.players.append(Player(bag_tiles=self.bag_tiles))
        
    #     self.current_player = None


    # Se define el constructor (__init__) de la clase ScrabbleGame.
    # Recibe un argumento 'players_count' que representa la cantidad de jugadores en el juego.
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

