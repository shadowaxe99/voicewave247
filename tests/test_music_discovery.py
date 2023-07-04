import unittest
from src import music_discovery

class TestMusicDiscovery(unittest.TestCase):

    def setUp(self):
        self.music_discovery = music_discovery.MusicDiscovery()
        self.userPreferences = {
            'genre': 'rock',
            'artist': 'Nirvana',
            'song': 'Smells Like Teen Spirit'
        }

    def test_discoverMusic(self):
        result = self.music_discovery.discoverMusic(self.userPreferences)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

    def test_updateUserPreferences(self):
        new_preferences = {
            'genre': 'pop',
            'artist': 'Taylor Swift',
            'song': 'Love Story'
        }
        self.music_discovery.updateUserPreferences(new_preferences)
        self.assertEqual(self.music_discovery.userPreferences, new_preferences)

if __name__ == '__main__':
    unittest.main()