import unittest
from unittest.mock import patch
from src import smart_home_integration

class TestSmartHomeIntegration(unittest.TestCase):

    @patch('src.smart_home_integration.integrateWithSmartHomeDevices')
    def test_integration_with_smart_home_devices(self, mock_integrate):
        test_device = {'deviceName': 'Test Device', 'deviceType': 'Speaker'}
        smart_home_integration.integrateWithSmartHomeDevices(test_device)
        mock_integrate.assert_called_with(test_device)

    @patch('src.smart_home_integration.updateSmartHomeDevices')
    def test_update_smart_home_devices(self, mock_update):
        test_device = {'deviceName': 'Test Device', 'deviceType': 'Speaker'}
        smart_home_integration.updateSmartHomeDevices(test_device)
        mock_update.assert_called_with(test_device)

    @patch('src.smart_home_integration.controlVoiceWave')
    def test_control_voice_wave(self, mock_control):
        test_command = 'Play music'
        smart_home_integration.controlVoiceWave(test_command)
        mock_control.assert_called_with(test_command)

if __name__ == '__main__':
    unittest.main()