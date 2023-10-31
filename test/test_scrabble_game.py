import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.player import Player
from game.dictionary_loader import load_local_dictionary
from game.scrabble import InvalidPlaceWordException


class TestScrabbleGame(unittest.TestCase):
    
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)


    def test_next_turn_when_game_is_starting(self):
        #validar que al comienzo, el turno es del jugador 1
         scrabble_game = ScrabbleGame(players_count=3)

         assert scrabble_game.current_player == scrabble_game.players[0]


    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_player_has_required_letters_and_word_fits_on_board(self):
        game = ScrabbleGame(2)
        game.current_player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]

        try:
            result, message = game.validate_word('CASA', (0, 0), 'horizontal')
            self.assertFalse(result)  # Debería ser False ya que la palabra no cabe en el tablero
            self.assertEqual(message, "Su palabra excede el tablero")
        except InvalidPlaceWordException:
            pass 



    # def test_remaining_tiles_in_bag_when_tiles_left(self):
    #     # Crea una instancia de ScrabbleGame con 2 jugadores
    #     game = ScrabbleGame(2)
            
    #     # Establece algunas fichas en la bolsa
    #     game.bag_tiles.tiles = [Tile('A'), Tile('B'), Tile('C')]
            
    #     # Llama a la función para obtener la cantidad de fichas restantes en la bolsa
    #     remaining_tiles = game.show_remaining_tiles_in_bag()
            
    #     # Verifica si la cantidad de fichas restantes en la bolsa es la misma
    #     # que la cantidad de fichas que habíamos establecido
    #     expected_remaining = len(game.bag_tiles.tiles)
    #     self.assertEqual(remaining_tiles, expected_remaining)


    @patch('builtins.input', return_value='2')  # Simula la entrada de datos
    def test_select_number_of_tiles_to_change(self, mock_input):
        game = ScrabbleGame(2)
        result = game.select_number_of_tiles_to_change()
        self.assertEqual(result, 2)  # Prueba con un valor predeterminado


    @patch('builtins.input', side_effect=['1', '2'])  # Simula entrada de usuario para los tests
    def test_select_tiles_to_change(self, mock_input):
        game = ScrabbleGame(2)
        current_player = game.current_player
        current_player.tiles = [Tile('A', 1), Tile('B', 1), Tile('C', 1), Tile('D', 1)]
        result = game.select_tiles_to_change(current_player, 2)


    @patch('builtins.input', side_effect=['Y'])  # Simula entrada de usuario para los tests
    def test_exchange_tiles(self, mock_input):
        game = ScrabbleGame(2)
        current_player = game.current_player
        
        # Asegúrate de que las fichas en tiles_to_change existan en la mano del jugador
        tiles_to_change = [Tile('B', 1), Tile('C', 1)]
        
        # Establece la mano del jugador con las fichas correctas
        current_player.tiles = tiles_to_change
        
        exchanged_tiles, new_tiles = game.perform_tile_exchange(current_player, tiles_to_change)
        # Asegúrate de verificar que las fichas devueltas coincidan con lo esperado








if __name__ == '__main__':
    unittest.main()