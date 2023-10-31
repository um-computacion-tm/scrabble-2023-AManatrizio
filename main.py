from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.cell import Cell
from game.board import Board
from game.player import Player
import random

def start_game(players_count):
    # Inicializa el juego
    scrabble_game = ScrabbleGame(players_count=players_count)
    bag_tiles = BagTiles()
    scrabble_game.bag_tiles = bag_tiles  # Asigna la bolsa de fichas al juego
    return scrabble_game, bag_tiles

def main():
    print("Bienvenido!")
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido")
    
    scrabble_game, bag_tiles = start_game(players_count)  # Inicia el juego y obtiene la bolsa de fichas

    board = Board()  # Crea una instancia de la clase Board
    board.initialize_multipliers()  # Establece los multiplicadores del tablero una vez
    board.show_board()  # Llama a la función show_board en la instancia de la clase
    
    # Llamamos a la función para distribuir fichas iniciales solo una vez al inicio del juego
    for player in scrabble_game.players:
        scrabble_game.draw_initial_tiles(player)

    board.initialize_multipliers()  # Establece los multiplicadores del tablero una vez

    while not scrabble_game.is_game_over():
        
        board = Board()  # Crea una instancia de la clase Board
        board.initialize_multipliers() 
        

        # Mostrar las letras en la mano del jugador
        player_tiles = scrabble_game.current_player.tiles
        print(f"Letras en tu mano (Jugador {scrabble_game.current_player.player_number}): {', '.join([tile.letter for tile in player_tiles])}")

        # Realiza las acciones del jugador (ingresar palabra, pasar, cambiar fichas, etc.)
        action = input("¿Qué deseas hacer? (Ingresar palabra (a) / Pasar (b) / Cambiar fichas (c) / Terminar (t) / / Mostrar tablero (m)): ")
        if action == 'a':
            word = input("Ingrese palabra: ")
            location_x = input("Ingrese posicion X: ")
            location_y = input("Ingrese posicion Y: ")
            orientation = input("Ingrese orientación (V/H)")
            scrabble_game.validate_word(word, (location_x, location_y), orientation)

        elif action == 'b':
            scrabble_game.next_turn()

        elif action == 'c':
            exchanged_tiles, new_tiles = scrabble_game.change_player_tiles(scrabble_game.current_player)
            print(f"Fichas cambiadas: {', '.join([tile.letter for tile in exchanged_tiles])}")
            print(f"Nuevas fichas: {', '.join([tile.letter for tile in new_tiles])}")

        elif action == 'm':
            board.show_board()  # Llama a la función show_board en la instancia de la clase

        elif action == 't':
            scrabble_game.request_end_game(player)

    #scrabble_game.next_turn()  # Avanza al siguiente jugador
            

# # Una vez que el bucle de juego haya terminado, se muestra al ganador.
#     winning_player = scrabble_game.get_winner()
#     print(f"¡El ganador es el Jugador {winning_player.player_number} con un puntaje de {winning_player.score}!")



if __name__ == '__main__':
    main()




