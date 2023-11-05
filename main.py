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
    print("Bienvenido, vamos a jugar Scrabble!")
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
    board.show_board(board)  # Llama a la función show_board en la instancia de la clase
    
    # Llamamos a la función para distribuir fichas iniciales solo una vez al inicio del juego
    for player in scrabble_game.players:
        scrabble_game.draw_initial_tiles(player)

    
    while not scrabble_game.is_game_over():
        
        #board = Board()  # Crea una instancia de la clase Board
        
        # Mostrar las letras en la mano del jugador
        player_tiles = scrabble_game.current_player.tiles
        print(f"Letras en tu mano (Jugador {scrabble_game.current_player.player_number}): {', '.join([tile.letter for tile in player_tiles])}")

        # Realiza las acciones del jugador (ingresar palabra, pasar, cambiar fichas, etc.)
        action = input("¿Qué deseas hacer? (Ingresar palabra (a) / Pasar (b) / Cambiar fichas (c) / Terminar (t) / / Mostrar tablero (m)): ")
        
        if action == 'a':
            if not scrabble_game.has_made_first_move:  # Verifica si ya se realizó el primer movimiento
                    print("¡Es el primer movimiento y la palabra se colocará en la posición central (7, 7) automáticamente!")
                    word = input("Ingrese palabra: ")
                    orientation = 'H'  # La orientación es fija en el primer movimiento
                    scrabble_game.place_word(word, 7, 7, orientation)
                    scrabble_game.has_made_first_move = True  # Marca que se ha realizado el primer movimiento
            else:
                    word = input("Ingrese palabra: ")
                    location_x = int(input("Ingrese posicion X: "))  # Asegúrate de convertir a int
                    location_y = int(input("Ingrese posicion Y: "))  # Asegúrate de convertir a int
                    orientation = input("Ingrese orientación (V/H): ")
                    scrabble_game.place_word(word, location_x, location_y, orientation)

        elif action == 'b':
            scrabble_game.next_turn()

        elif action == 'c':
            exchanged_tiles, new_tiles = scrabble_game.change_player_tiles(scrabble_game.current_player)
            print(f"Fichas cambiadas: {', '.join([tile.letter for tile in exchanged_tiles])}")
            print(f"Nuevas fichas: {', '.join([tile.letter for tile in new_tiles])}")

        elif action == 'm':
            
            print("tablero de multipicadores")
            board.show_board(Board)  # Llama a la función show_board en la instancia de la clase

        elif action == 't':
            scrabble_game.request_end_game(player)

    #scrabble_game.next_turn()  # Avanza al siguiente jugador
            

# # Una vez que el bucle de juego haya terminado, se muestra al ganador.
#     winning_player = scrabble_game.get_winner()
#     print(f"¡El ganador es el Jugador {winning_player.player_number} con un puntaje de {winning_player.score}!")



if __name__ == '__main__':
    main()