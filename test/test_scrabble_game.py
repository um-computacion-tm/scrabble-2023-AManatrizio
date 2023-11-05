import unittest
from unittest.mock import patch, Mock
from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.player import Player
from game.board import Board
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


    def test_draw_initial_tiles(self):
        self.game = ScrabbleGame(players_count=3)
        # Configuramos un jugador y una bolsa de fichas con fichas iniciales
        player = Player(1)
        initial_tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]

        # Mock de la bolsa de fichas para simular el comportamiento
        self.game.bag_tiles = Mock()
        self.game.bag_tiles.take.return_value = initial_tiles

        # Llamamos a la función que queremos probar
        self.game.draw_initial_tiles(player)

        # Verificamos que el jugador tenga las fichas iniciales
        self.assertEqual(player.tiles, initial_tiles)

    

    @patch('builtins.input', side_effect=['3'])  # Simula la entrada de datos
    def test_select_number_of_tiles_to_change_valid_input(self, mock_input):
        result = ScrabbleGame.select_number_of_tiles_to_change()
        self.assertEqual(result, 3)


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



    def test_validate_word_place_board_horizontal(self):
        board = Board()
        board.initialize_multipliers()
        # Verificar que la palabra "jugar" en (1, 4) con dirección horizontal sea válida
        self.assertTrue(board.validate_word_place_board("jugar", (1, 4), "H"))
    
    def test_validate_word_place_board_vertical(self):
        board = Board()
        board.initialize_multipliers()
        # Verificar que la palabra "jugar" en (4, 1) con dirección vertical sea válida
        self.assertTrue(board.validate_word_place_board("jugar", (4, 1), "V"))
    
    def test_request_end_game(self):
        # Crea una instancia de ScrabbleGame y agrega algunos jugadores
        scrabble_game = ScrabbleGame(players_count=3)
        player1 = Player(1)
        player2 = Player(2)
        player3 = Player(3)
        scrabble_game.players = [player1, player2, player3]

        # Llama a la función request_end_game para el jugador 2
        scrabble_game.request_end_game(player2)

        # Verifica que el jugador 2 haya solicitado el fin del juego
        self.assertTrue(scrabble_game.players_want_to_end_game[1])

    
    def test_is_game_over_bag_empty(self):
    # Crea una instancia de ScrabbleGame y una bolsa de fichas vacía
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles = BagTiles()
        scrabble_game.bag_tiles.tiles = []  # Simula una bolsa de fichas vacía

        # Verifica que el juego esté marcado como terminado
        self.assertTrue(scrabble_game.is_game_over())

    def test_is_game_over_players_want_to_end_game(self):
        # Crea una instancia de ScrabbleGame con jugadores que quieren terminar el juego
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.players_want_to_end_game = [True, False]

        # Verifica que el juego esté marcado como terminado
        self.assertTrue(scrabble_game.is_game_over())

    def test_is_game_over_no_condition_met(self):
        # Crea una instancia de ScrabbleGame con condiciones no cumplidas
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles = BagTiles()
        scrabble_game.bag_tiles.tiles = [Mock()]  # Simula una bolsa de fichas no vacía
        scrabble_game.players_want_to_end_game = [False, False]  # Jugadores no quieren terminar

        # Verifica que el juego no esté marcado como terminado
        self.assertFalse(scrabble_game.is_game_over())


    def test_place_word_first_move(self):
        # Prueba colocar una palabra en el primer movimiento
        scrabble_game = ScrabbleGame(players_count=3)
        word = "HOLA"
        orientation = "H"
        scrabble_game.place_word(word, 7, 7, orientation)

        # Verifica que la palabra se coloque correctamente
        board = scrabble_game.board
        self.assertEqual(board.grid[7][7].letter, "H")
        self.assertEqual(board.grid[7][8].letter, "O")
        self.assertEqual(board.grid[7][9].letter, "L")
        self.assertEqual(board.grid[7][10].letter, "A")




if __name__ == '__main__':
    unittest.main()