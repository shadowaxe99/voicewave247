import unittest
from src import listener_stats

class TestListenerStats(unittest.TestCase):

    def setUp(self):
        self.listenerStats = listener_stats.ListenerStats()

    def test_update_listener_stats(self):
        new_stats = {
            'total_listeners': 500,
            'active_listeners': 300,
            'listener_feedback': {
                'positive': 200,
                'negative': 50
            }
        }
        self.listenerStats.updateListenerStats(new_stats)
        self.assertEqual(self.listenerStats.listenerStats, new_stats)

    def test_get_listener_stats(self):
        stats = self.listenerStats.getListenerStats()
        self.assertIsInstance(stats, dict)

    def test_get_active_listeners(self):
        active_listeners = self.listenerStats.getActiveListeners()
        self.assertIsInstance(active_listeners, int)

    def test_get_listener_feedback(self):
        feedback = self.listenerStats.getListenerFeedback()
        self.assertIsInstance(feedback, dict)

if __name__ == '__main__':
    unittest.main()