__Changelog - Scrabble Project on Python__

October 20, 2023:
- Modifided the is_empty method to properly verify if the cell at position [7][7] is empty, ensuring that it returns True if the cell is empty and False if it contains a letter.
- Updated the __init__ method to initialize the board with empty cells by default. This ensures that the board starts in an empty state.


October 11, 2023:
- Added the method show_board, is used to display the current state of the game board.
- I have been having trouble with writing test for validate_word function, Im using CodiumAI and ChatGPT for help but i still cant get it.
- Im also having troubles with the main.

October 3, 2023:
- Added the 'has letter' function for checking if a player has certain letters in their "tile inventory".

October 1, 2023:
- Added tests for dictionary
- Removed "word_validator" because I renamed it
- Renamed the file 'word_validator' to 'dictionary' for easier identification.

September 26, 2023:
- Added a function attempt to check if the board is empty, but its not working yet it has 4 failures and 1 error. Also, added a menu to the main that was not committed in the previous update.
- I have to ask how can i do to run the main and see a print of the board, type the number of players, etc.

September 25, 2023:
- Added the `WordValidator` class for word validation with the RAE dictionary.
    The `WordValidator` class has been introduced to facilitate word validation using the RAE (Real Academia Española) dictionary. It provides methods to connect to the Pyrae API and validate words against the RAE dictionary.

September 24, 2023:
- Updated the main file to include a menu with multiple options.
    The main file has been enhanced with a user-friendly menu, offering the following options:
    1. Display the Game Board
    2. Show Player Scores
    3. Place a Word on the Board
    4. Exchange Tiles
    5. Pass Turn
    6. End the Game
- Im still strugulling with the funtion that determinates if the board is emtpy or not

September 19, 2023:
- Changes in the calculate_word_value function to work when the multiplier is not active.
    Modifications were made to the calculate_word_value function to ensure it functions correctly when the multiplier is not active.

August 29, 2023:
- Add Code Climate and changelog.
    Code Climate integration and the addition of a changelog were implemented.
- Gitignore changes.
    Modifications were made to the .gitignore file.
- Adding files.
    New files were included in the project.
- Adding test files.
    Test files were added to the project.
- Resolve conflict in .gitignore.
    A conflict in the .gitignore file was resolved.
- Merged branch 'main' with branch 'develop'.
    The 'main' branch was merged with the 'develop' branch.      

August 28, 2023:
- Created README file.
    The README file was created.

August 16, 2023:
- Initial project commit:
    The initial project commit was made.