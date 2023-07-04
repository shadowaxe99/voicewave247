```python
import unittest
from src import interactive_games

class TestInteractiveGames(unittest.TestCase):

    def setUp(self):
        self.gameData = interactive_games.gameData

    def test_playInteractiveGames(self):
        # Test if the function returns a game based on user voice command
        result = interactive_games.playInteractiveGames("Play trivia")
        self.assertIn("trivia", result)

    def test_updateGameData(self):
        # Test if the function updates game data correctly
        interactive_games.updateGameData("new_game")
        self.assertIn("new_game", self.gameData)

    def test_gameDataStructure(self):
        # Test if game data adheres to the GameSchema
        for game in self.gameData:
            self.assertIn('name', game)
            self.assertIn('description', game)
            self.assertIn('rules', game)

if __name__ == '__main__':
    unittest.main()
```