## Author
creator name: Antonella Manatrizio

# maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/501cec3723d1db83d4e8/maintainability)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-AManatrizio/maintainability)

# test coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/501cec3723d1db83d4e8/test_coverage)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-AManatrizio/test_coverage)

# main
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-AManatrizio/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-AManatrizio/tree/main)



# Scrabble with Docker

This repository contains an implementation of the Scrabble game in Python that can be run in Docker containers. You can play Scrabble in test mode to check and test the game's functionality, or you can play it in play mode for an interactive gaming experience using the provided Docker setup.

## Prerequisites

Make sure you have the following requirements installed on your system:

- [Docker](https://www.docker.com/get-started)

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/scrabble-docker.git
   cd scrabble-docker
Build the Docker image:

bash
Copy code
docker build -t scrabble-game .
Test Mode
Test mode allows you to run tests to verify the game's functionality without engaging in real-time gameplay. You can use this mode to check the game's features and rules.

Run the game in test mode:

bash
Copy code
docker run -it --rm scrabble-game python test_game.py
This will execute the tests defined in test_game.py and display the results.

Play Mode
Play mode enables you to enjoy a real-time Scrabble game with either human or virtual opponents. Ensure you have at least two players to enjoy a match.

Run the game in play mode:

bash
Copy code
docker run -it --rm scrabble-game python play_game.py
Follow the on-screen instructions to play Scrabble. Have fun!

