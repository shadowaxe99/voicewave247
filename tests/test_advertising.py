```python
import unittest
from src import advertising

class TestAdvertising(unittest.TestCase):

    def setUp(self):
        self.advertising = advertising.DynamicAdvertising()

    def test_display_ads(self):
        userPreferences = {"genre": "rock", "artist": "Nirvana"}
        self.advertising.displayAds(userPreferences)
        self.assertIsNotNone(self.advertising.ads)

    def test_update_user_preferences(self):
        userPreferences = {"genre": "pop", "artist": "Taylor Swift"}
        self.advertising.updateUserPreferences(userPreferences)
        self.assertEqual(self.advertising.userPreferences, userPreferences)

    def test_ad_targeting(self):
        userPreferences = {"genre": "jazz", "artist": "Miles Davis"}
        self.advertising.updateUserPreferences(userPreferences)
        self.advertising.displayAds(userPreferences)
        for ad in self.advertising.ads:
            self.assertIn(userPreferences["genre"], ad["targetGenres"])

if __name__ == '__main__':
    unittest.main()
```