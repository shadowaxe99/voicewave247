import unittest
from src.artist_interviews import interviewArtists
from src.utils import artistData, UserSchema, ArtistSchema

class TestArtistInterviews(unittest.TestCase):

    def setUp(self):
        self.user = UserSchema(name="Test User", preferences={"genre": "rock"})
        self.artist = ArtistSchema(name="Test Artist", genre="rock")

    def test_interviewArtists(self):
        # Simulate artist data
        artistData.append(self.artist)

        # Call the function to test
        interviewArtists(self.user)

        # Check if the artist interviews are updated in the artist data
        self.assertTrue(any(artist.interviews for artist in artistData if artist.name == self.artist.name))

if __name__ == '__main__':
    unittest.main()