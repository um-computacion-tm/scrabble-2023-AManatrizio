
# Clase Player
class Player:
    # Constructor de la clase Player
    def __init__(self, player_number, bag_tiles=None):
        # Inicializar una lista de fichas vacía para el jugador
        self.tiles = []
        # Asignar la instancia de BagTiles que se pasa como argumento al jugador
        self.bag_tiles = bag_tiles
        # Inicializa el puntaje del jugador en 0
        self.score = 0 
        # Almacena el número de jugador
        self.player_number = player_number


    # Método has_letters que verifica si el jugador tiene ciertas letras
    def has_letters(self, tiles):
        # Verificar si el jugador tiene una bolsa de fichas (bag_tiles)
        if not self.bag_tiles:
            # Si el jugador no tiene una bolsa de fichas, no puede tener letras, así que devolvemos False
            return False
        
        # Crear una lista de letras que están en la bolsa del jugador
        player_letters = [tile.letter for tile in self.bag_tiles.tiles]
        
        # Iterar sobre las fichas que se pasan como argumento (tiles)
        for tile in tiles:
            # Verificar si la letra de la ficha actual no está en la bolsa del jugador
            if tile.letter not in player_letters:
                # Si una letra no está en la bolsa del jugador, devolvemos False
                return False
        
        # Si todas las letras de las fichas están en la bolsa del jugador, devolvemos True
        return True
    

    # Método para agregar puntos al puntaje del jugador
    def add_score(self, points):
            self.score += points