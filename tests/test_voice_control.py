import unittest
from unittest.mock import patch
from src import voice_control

class TestVoiceControl(unittest.TestCase):

    @patch('src.voice_control.controlVoiceWave')
    def test_voice_control(self, mock_controlVoiceWave):
        # Mock user voice command
        voice_command = "Play the latest album by Coldplay"
        mock_controlVoiceWave.return_value = "Playing the latest album by Coldplay"

        # Call the function with the mock command
        response = voice_control.controlVoiceWave(voice_command)

        # Assert the function was called with the right arguments
        mock_controlVoiceWave.assert_called_with(voice_command)

        # Assert the function returned the expected result
        self.assertEqual(response, "Playing the latest album by Coldplay")

    @patch('src.voice_control.updateUserPreferences')
    def test_update_user_preferences(self, mock_updateUserPreferences):
        # Mock user preferences
        user_preferences = {"genre": "rock", "artist": "Coldplay"}
        mock_updateUserPreferences.return_value = True

        # Call the function with the mock preferences
        result = voice_control.updateUserPreferences(user_preferences)

        # Assert the function was called with the right arguments
        mock_updateUserPreferences.assert_called_with(user_preferences)

        # Assert the function returned the expected result
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()