from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.cell import Cell
from game.board import Board
from game.player import Player
import random

def start_game(players_count):
    # Inicializa el juego
    scrabble_game = ScrabbleGame(players_count=players_count)
    # Inicializa la bolsa de fichas
    bag_tiles = BagTiles()
    scrabble_game.bag_tiles = bag_tiles  # Asigna la bolsa de fichas al juego
    return scrabble_game


def main():
    print("Bienvenido!")
    # Inicializa la bolsa de fichas
    bag_tiles = BagTiles()
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor inválido")
    
    scrabble_game = start_game(players_count)  # Inicia el juego
    board = Board()  # Crea una instancia de la clase Board
    
    # Llamamos a la función para distribuir fichas iniciales solo una vez al inicio del juego
    for player in scrabble_game.players:
        scrabble_game.draw_initial_tiles(player)

    board.initialize_multipliers()  # Establece los multiplicadores del tablero una vez

    while not scrabble_game.is_game_over():
        
        board = Board()  # Crea una instancia de la clase Board
        board.initialize_multipliers() 
        board.show_board()  # Llama a la función show_board en la instancia de la clase

        # Mostrar las letras en la mano del jugador
        player_tiles = scrabble_game.current_player.tiles
        print(f"Letras en tu mano (Jugador {scrabble_game.current_player.player_number}): {', '.join([tile.letter for tile in player_tiles])}")

        # Realiza las acciones del jugador (ingresar palabra, pasar, cambiar fichas, etc.)
        action = input("¿Qué deseas hacer? (Ingresar palabra (a) / Pasar (b) / Cambiar fichas (c) / Terminar (t)): ")
        if action == 'a':
            # Aquí deberías tener la lógica para ingresar una palabra válida.
            word = input("Ingrese palabra: ")
            location_x = input("Ingrese posicion X: ")
            location_y = input("Ingrese posicion Y: ")
            orientation = input("Ingrese orientación (V/H)")
            scrabble_game.validate_word(word, (location_x, location_y), orientation)


        elif action == 'b':
            scrabble_game.next_turn()

        elif action == 'c':
            exchanged_tiles, new_tiles = scrabble_game.change_player_tiles(scrabble_game.current_player)
            if exchanged_tiles:
                print(f"Fichas cambiadas: {', '.join([tile.letter for tile in exchanged_tiles])}")
                print(f"Nuevas fichas: {', '.join([tile.letter for tile in new_tiles])}")
            else:
                print("No se pudieron cambiar las fichas. Verifica que tienes suficientes letras.")

        #scrabble_game.next_turn()  # Avanza al siguiente jugador
            

# Una vez que el bucle de juego haya terminado, se muestra al ganador.
    winning_player = scrabble_game.get_winner()
    print(f"¡El ganador es el Jugador {winning_player.player_number} con un puntaje de {winning_player.score}!")



if __name__ == '__main__':
    main()



# def main(): 
#     print("Bienvenido!")

#     while True:
#         try:
#             player_count = int(input("Ingrese la cantidad de jugadores: "))
#             if player_count <= 0:
#                 print("La cantidad de jugadores debe ser un entero positivo.")
#             else:
#                 break
#         except ValueError:
#             print("La cantidad de jugadores debe ser un entero positivo.")

#     game = ScrabbleGame(player_count)
#     board = Board()

#     while not game.is_game_over():
#         current_player = game.get_current_player()

#         print(f"\nTurno de {current_player.name}")

#         print(board)

#         print("Menú de opciones:")
#         print("1. Ingresar una palabra")
#         print("2. Pasar el turno")
#         print("3. Terminar el juego")

#         choice = input("Selecciona una opción: ")

#         if choice == "1":
#             word = input("Ingresa una palabra: ")
#             position = input("Ingresa la posición (fila, columna): ")

#             if not game.is_valid_word(word):
#                 print("Palabra inválida. Intenta de nuevo.")
#                 continue

#             if not board.is_valid_position(position):
#                 print("Posición inválida. Intenta de nuevo.")
#                 continue

#             success = board.place_word(word, position)

#             if not success:
#                 print("No se pudo colocar la palabra en esa posición. Intenta de nuevo.")
#                 continue

#             current_player.update_score(game.calculate_word_value(word, position))

#         elif choice == "2":
#             game.next_turn()

#         elif choice == "3":
#             break

#         else:
#             print("Opción inválida. Intenta de nuevo.")

#     print("\n¡Fin del juego!")
#     for player in game.players:
#         print(f"{player.name}: {player.score}")

# if __name__ == "__main__":
#     main()






















# intento de tablero
# def print_scrabble_board():
#     board_size = 15  # Tamaño del tablero de Scrabble (15x15)

#     # Imprimir el encabezado de las columnas
#     header = "    " + "   ".join(f"{i + 1:2}" for i in range(board_size))
#     separator = "  +" + "+".join(["---"] * board_size) + "+"

#     print(header)
#     print(separator)

#     # Imprimir las filas del tablero
#     for i in range(board_size):
#         row_str = f"{i + 1:2} | " + " | ".join("   " for _ in range(board_size)) + " |"
#         print(row_str)
#         print(separator)