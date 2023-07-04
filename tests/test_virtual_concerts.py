import unittest
from src import virtual_concerts

class TestVirtualConcerts(unittest.TestCase):

    def setUp(self):
        self.virtual_concerts = virtual_concerts.VirtualConcerts()
        self.userPreferences = {"genre": "rock", "artist": "Nirvana"}
        self.liveEvents = [{"event": "Nirvana Live", "date": "2022-12-31", "time": "20:00"}]

    def test_hostVirtualConcerts(self):
        result = self.virtual_concerts.hostVirtualConcerts(self.userPreferences, self.liveEvents)
        self.assertEqual(result, "Nirvana Live concert is scheduled on 2022-12-31 at 20:00")

    def test_updateLiveEvents(self):
        new_event = {"event": "Foo Fighters Live", "date": "2023-01-01", "time": "20:00"}
        self.liveEvents.append(new_event)
        self.virtual_concerts.updateLiveEvents(self.liveEvents)
        self.assertIn(new_event, self.virtual_concerts.liveEvents)

    def test_getLiveEvents(self):
        self.virtual_concerts.updateLiveEvents(self.liveEvents)
        result = self.virtual_concerts.getLiveEvents()
        self.assertEqual(result, self.liveEvents)

if __name__ == '__main__':
    unittest.main()