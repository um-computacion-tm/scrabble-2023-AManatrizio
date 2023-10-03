from game.scrabble import ScrabbleGame
from game.models import Tile, BagTiles
from game.cell import Cell
from game.board import Board

def main():
    print("Bienvenido!")

    # Solicitar la cantidad de jugadores
    player_count = int(input("Ingrese la cantidad de jugadores: "))

    # Inicializar el juego
    game = ScrabbleGame(player_count=player_count)
    board = Board()

    # Ciclo principal del juego
    while not game.is_game_over():
        # Obtener el jugador actual
        current_player = game.get_current_player()

        print(f"\nTurno de {current_player.name}")

        # Mostrar el tablero actual
        print(board)

        # Mostrar el menú de opciones
        print("Menú de opciones:")
        print("1. Ingresar una palabra")
        print("2. Pasar el turno")
        print("3. Terminar el juego")

        # Solicitar la selección de una opción
        choice = input("Selecciona una opción: ")

        if choice == "1":
            # Solicitar palabra y posición al jugador
            word = input("Ingresa una palabra: ")
            position = input("Ingresa la posición (fila, columna): ")

            # Validar la palabra y la posición ingresadas
            if not game.is_valid_word(word):
                print("Palabra inválida. Intenta de nuevo.")
                continue

            if not board.is_valid_position(position):
                print("Posición inválida. Intenta de nuevo.")
                continue

            # Colocar la palabra en el tablero
            success = board.place_word(word, position)

            if not success:
                print("No se pudo colocar la palabra en esa posición. Intenta de nuevo.")
                continue

            # Actualizar la puntuación del jugador
            current_player.update_score(game.calculate_word_value(word, position))

        elif choice == "2":
            # Pasar el turno
            game.next_turn()

        elif choice == "3":
            # Terminar el juego
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

    # Juego terminado, mostrar puntuaciones finales
    print("\n¡Fin del juego!")
    for player in game.players:
        print(f"{player.name}: {player.score}")

if __name__ == "__main__":
    main()


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

