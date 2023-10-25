from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.cell import Cell
from game.board import Board
from game.player import Player


def main():

    print("Bienvenido!")
    while True:
        try:
            players_count = int(input("Ingrese cantidad de jugadores: "))
            if players_count <= 1 or players_count > 4:
                raise ValueError
            break
        except ValueError:
            print("Valor invalido")
    scrabble_game = ScrabbleGame(players_count=players_count)
    print("Cantidad de jugadores: ",len(scrabble_game.players))
    scrabble_game.next_turn()
    #TODO while playing: loop por turno de jugador hasta que termine el juego
    print(f"Turno del jugador {scrabble_game.current_player}")
    word = input("Ingrese palabra: ")
    location_x = input("Ingrese posicion X: ")
    location_y = input("Ingrese posicion Y: ")
    location = (location_x, location_y)
    orientation = input("Ingrese orientacion (V/H)")
    scrabble_game.validate_word(word, location, orientation)



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

