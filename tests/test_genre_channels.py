import unittest
from src import genre_channels

class TestGenreChannels(unittest.TestCase):

    def setUp(self):
        self.genre_channels = genre_channels.curateGenreChannels()

    def test_genre_channels_exist(self):
        self.assertIsNotNone(self.genre_channels)

    def test_genre_channels_type(self):
        self.assertIsInstance(self.genre_channels, dict)

    def test_genre_channels_content(self):
        for genre, channel in self.genre_channels.items():
            self.assertIsInstance(genre, str)
            self.assertIsInstance(channel, list)

    def test_update_genre_channels(self):
        new_genre = "New Genre"
        new_channel = ["Song 1", "Song 2", "Song 3"]
        self.genre_channels.update({new_genre: new_channel})
        self.assertIn(new_genre, self.genre_channels)
        self.assertEqual(self.genre_channels[new_genre], new_channel)

if __name__ == '__main__':
    unittest.main()