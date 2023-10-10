import unittest
from game.scrabble import ScrabbleGame


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


    def test_validate_word(self):
        # Crear una instancia de ScrabbleGame con un jugador
        scrabble_game = ScrabbleGame(players_count=1)

        # Configurar el tablero para que la palabra "CASA" encaje horizontalmente en la posición (0, 0)
        scrabble_game.board.place_tile('C', (0, 0))
        scrabble_game.board.place_tile('A', (0, 1))
        scrabble_game.board.place_tile('S', (0, 2))
        scrabble_game.board.place_tile('A', (0, 3))

        # Validar la palabra "CASA" en la ubicación (0, 0) horizontalmente
        word = "CASA"
        location = (0, 0)
        orientation = "horizontal"
        
        # Crear una lista de fichas que representan las letras de la palabra
        word_tiles = [Tile(letter) for letter in word]

        # Configurar la mano del jugador con algunas letras
        player = scrabble_game.current_player
        player.tiles = ['A', 'C', 'S', 'A', 'E', 'F']

        # Validar la palabra con las letras del jugador usando el método has_letters
        result = player.has_letters(word_tiles)

        # Verificar que la palabra sea válida
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
