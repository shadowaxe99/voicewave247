```python
import unittest
from src import virtual_meet_and_greets

class TestVirtualMeetAndGreets(unittest.TestCase):

    def setUp(self):
        self.virtual_meet_and_greets = virtual_meet_and_greets.VirtualMeetAndGreets()

    def test_hostVirtualMeetAndGreets(self):
        self.virtual_meet_and_greets.hostVirtualMeetAndGreets()
        self.assertTrue(self.virtual_meet_and_greets.is_live)

    def test_updateUserPreferences(self):
        old_preferences = self.virtual_meet_and_greets.userPreferences
        self.virtual_meet_and_greets.updateUserPreferences({"genre": "rock"})
        self.assertNotEqual(old_preferences, self.virtual_meet_and_greets.userPreferences)

    def test_updateArtistData(self):
        old_data = self.virtual_meet_and_greets.artistData
        self.virtual_meet_and_greets.updateArtistData({"artist": "New Artist"})
        self.assertNotEqual(old_data, self.virtual_meet_and_greets.artistData)

    def tearDown(self):
        self.virtual_meet_and_greets = None

if __name__ == '__main__':
    unittest.main()
```