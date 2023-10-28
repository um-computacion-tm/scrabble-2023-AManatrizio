import unittest
from game.scrabble import ScrabbleGame
from game.models import Tile


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

    # # Player has required letters and word fits on board
    # def test_player_has_required_letters_and_word_fits_on_board(self):
    #     game = ScrabbleGame(2)
    #     game.current_player.letters = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2)]
    #     result, message = game.validate_word('ABCD', (0, 0), 'horizontal')
    #     self.assertTrue(result)
    #     self.assertEqual(message, "The word is valid.")


if __name__ == '__main__':
    unittest.main()