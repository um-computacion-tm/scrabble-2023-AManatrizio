from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.cell import Cell
from game.board import Board

def main(self):
    print ("Bienvenido")
    player_count = int(input('Ingrese la cantidad de jugadores:'))
    game = ScrabbleGame(player_count = player_count )
    board = Board() 