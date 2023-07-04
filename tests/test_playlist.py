import unittest
from src import playlist

class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = playlist.createPlaylist()
        self.userPreferences = {"genre": "rock", "artist": "Nirvana"}

    def test_create_playlist(self):
        self.playlist.create("My Playlist", self.userPreferences)
        self.assertIn("My Playlist", self.playlistData)

    def test_add_song_to_playlist(self):
        self.playlist.create("My Playlist", self.userPreferences)
        self.playlist.add_song("My Playlist", "Smells Like Teen Spirit")
        self.assertIn("Smells Like Teen Spirit", self.playlistData["My Playlist"])

    def test_remove_song_from_playlist(self):
        self.playlist.create("My Playlist", self.userPreferences)
        self.playlist.add_song("My Playlist", "Smells Like Teen Spirit")
        self.playlist.remove_song("My Playlist", "Smells Like Teen Spirit")
        self.assertNotIn("Smells Like Teen Spirit", self.playlistData["My Playlist"])

    def test_share_playlist(self):
        self.playlist.create("My Playlist", self.userPreferences)
        self.playlist.share("My Playlist", "friend@example.com")
        self.assertIn("friend@example.com", self.playlistData["My Playlist"]["sharedWith"])

    def test_update_playlist(self):
        self.playlist.create("My Playlist", self.userPreferences)
        new_preferences = {"genre": "pop", "artist": "Taylor Swift"}
        self.playlist.update("My Playlist", new_preferences)
        self.assertEqual(new_preferences, self.playlistData["My Playlist"]["preferences"])

if __name__ == '__main__':
    unittest.main()