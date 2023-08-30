import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1), Tile('A', 1),
            
            Tile('B', 3), Tile('B', 3),
            
            Tile('C', 3), Tile('C', 3),
            
            Tile('D', 2), Tile('D', 2), Tile('D', 2), Tile('D', 2),
            
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('E', 1), Tile('E', 1),
            
            Tile('F', 4), Tile('F', 4),
            
            Tile('G', 2), Tile('G', 2), Tile('G', 2),
            
            Tile('H', 4), Tile('H', 4),
            
            Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1), Tile('I', 1),
            Tile('I', 1), Tile('I', 1), Tile('I', 1),
            
            Tile('J', 8),
            
            Tile('K', 5),
            
            Tile('L', 1), Tile('L', 1), Tile('L', 1), Tile('L', 1),
            
            Tile('M', 3), Tile('M', 3),
            
            Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1), Tile('N', 1),
            Tile('N', 1),
            
            Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1), Tile('O', 1),
            Tile('O', 1), Tile('O', 1), Tile('O', 1),
            
            Tile('P', 3), Tile('P', 3),
            
            Tile('Q', 10),
            
            Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1), Tile('R', 1),
            Tile('R', 1),
            
            Tile('S', 1), Tile('S', 1), Tile('S', 1), Tile('S', 1),
            
            Tile('T', 1), Tile('T', 1), Tile('T', 1), Tile('T', 1), Tile('T', 1),
            Tile('T', 1),
            
            Tile('U', 1), Tile('U', 1), Tile('U', 1), Tile('U', 1),
            
            Tile('V', 4), Tile('V', 4),
            
            Tile('W', 4), Tile('W', 4),
            
            Tile('X', 8),
            
            Tile('Y', 4), Tile('Y', 4),
            
            Tile('Z', 10)
    
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
