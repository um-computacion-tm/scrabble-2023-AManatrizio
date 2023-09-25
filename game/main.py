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

        # Cambiar al siguiente jugador
        game.next_turn()

    # Juego terminado, mostrar puntuaciones finales
    print("\n¡Fin del juego!")
    for player in game.players:
        print(f"{player.name}: {player.score}")




if __name__ == "__main__":
    main()
