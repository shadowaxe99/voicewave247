```python
import unittest
from src import interaction

class TestInteraction(unittest.TestCase):

    def setUp(self):
        self.interaction = interaction.engageWithListeners()

    def test_updateUserPreferences(self):
        self.interaction.updateUserPreferences({"genre": "rock", "artist": "Nirvana"})
        self.assertEqual(self.interaction.userPreferences, {"genre": "rock", "artist": "Nirvana"})

    def test_handleCallIns(self):
        result = self.interaction.handleCallIns("1234567890")
        self.assertTrue(result)

    def test_handleTextMessages(self):
        result = self.interaction.handleTextMessages("Hello VoiceWave 24/7")
        self.assertTrue(result)

    def test_handleSocialMediaInteraction(self):
        result = self.interaction.handleSocialMediaInteraction("@VoiceWave247", "Loving the music!")
        self.assertTrue(result)

    def test_directInteractionWithHosts(self):
        result = self.interaction.directInteractionWithHosts("Host1", "Great show!")
        self.assertTrue(result)

    def test_directInteractionWithCelebrities(self):
        result = self.interaction.directInteractionWithCelebrities("Celebrity1", "Big fan!")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```