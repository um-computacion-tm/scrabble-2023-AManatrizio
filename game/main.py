from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.cell import Cell
from game.board import Board

def main(self):
    player_count = int(input('Cantidad de jugadores:'))
    game = ScrabbleGame(player_count)
    board = Board()