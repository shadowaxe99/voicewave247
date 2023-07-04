```python
import json
from src.utils import voice_command

gameData = {}

def load_games():
    global gameData
    with open('gameData.json', 'r') as file:
        gameData = json.load(file)

def save_games():
    with open('gameData.json', 'w') as file:
        json.dump(gameData, file)

@voice_command
def play_game(game_name):
    if game_name in gameData:
        game = gameData[game_name]
        print(f"Starting game: {game['name']}")
        # Add code here to start the game
    else:
        print(f"Game {game_name} not found.")

@voice_command
def add_game(game_name, game_info):
    gameData[game_name] = game_info
    save_games()

@voice_command
def remove_game(game_name):
    if game_name in gameData:
        del gameData[game_name]
        save_games()
    else:
        print(f"Game {game_name} not found.")

load_games()
```