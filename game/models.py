import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('A', 1), Tile('A', 1), Tile('A', 1),
            Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('E', 1), Tile('E', 1), Tile('E', 1),
            Tile('I', 1), Tile('I', 1), Tile('I', 1),
            Tile('I', 1), Tile('I', 1), Tile('I', 1),
            Tile('L', 1), Tile('L', 1),
            Tile('L', 1), Tile('L', 1),
            Tile('N', 1), Tile('N', 1), Tile('N', 1),
            Tile('N', 1), Tile('N', 1),
            Tile('O', 1), Tile('O', 1), Tile('O', 1),
            Tile('O', 1), Tile('O', 1), Tile('O', 1),
            Tile('O', 1), Tile('O', 1), Tile('O', 1),
            Tile('R', 1), Tile('R', 1), Tile('R', 1),
            Tile('R', 1), Tile('R', 1),
            Tile('S', 1), Tile('S', 1), Tile('S', 1),
            Tile('S', 1), Tile('S', 1), Tile('S', 1),
            Tile('T', 1), Tile('T', 1),
            Tile('T', 1), Tile('T', 1),
            Tile('U', 1), Tile('U', 1), Tile('U', 1),
            Tile('U', 1), Tile('U', 1),
            Tile('D', 2), Tile('D', 2), Tile('D', 2),
            Tile('D', 2), Tile('D', 2),
            Tile('G', 2), Tile('G', 2),
            Tile('B', 3), Tile('B', 3),
            Tile('C', 3), Tile('C', 3),
            Tile('C', 3), Tile('C', 3),
            Tile('M', 3), Tile('M', 3),
            Tile('P', 3), Tile('P', 3),
            Tile('F', 4), Tile('H', 4), Tile('H', 4),
            Tile('V', 4), Tile('Y', 4),
            Tile('CH', 5), Tile('Q', 5),
            Tile('J', 8), Tile('LL', 8), Tile('Ñ', 8),
            Tile('RR', 8), Tile('X', 8),
            Tile('Z', 10),
            Tile('comodin', 0), Tile('comodin', 0),
    
        ]
        random.shuffle(self.tiles)

    def put(self, tiles):
            # Añadir las fichas a la bolsa
            self.tiles.extend(tiles)
            print("Fichas agregadas a la bolsa:", [tile.letter for tile in tiles])

    def take(self, count):
        # Tomar fichas de la bolsa
        if count <= len(self.tiles):
            selected_tiles = random.sample(self.tiles, count)
            for tile in selected_tiles:
                self.tiles.remove(tile)
            print("Fichas tomadas de la bolsa:", [tile.letter for tile in selected_tiles])
            return selected_tiles
        else:
            raise ValueError("No hay suficientes fichas en la bolsa para tomar.")
        
        
    # def take(self, count):
    #     tiles = []
    #     for _ in range(count):
    #         tiles.append(self.tiles.pop())
    #     return tiles

    # def put(self, tiles):
    #     self.tiles.extend(tiles)

    def shuffle(self):
        random.shuffle(self.tiles)
    
    def is_empty(self):
        # Verificar si la bolsa de fichas está vacía (se agotaron las fichas)
        return not self.tiles
