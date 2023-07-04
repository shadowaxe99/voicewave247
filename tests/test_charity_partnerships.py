import unittest
from src.charity_partnerships import partnerWithCharities
from src.utils import CharitySchema

class TestCharityPartnerships(unittest.TestCase):

    def setUp(self):
        self.charityData = {
            "name": "Helping Hands",
            "description": "A charity organization focused on providing education to underprivileged children.",
            "fundraisingTarget": 50000,
            "currentAmount": 25000
        }
        self.charitySchema = CharitySchema()

    def test_partnerWithCharities(self):
        result = partnerWithCharities(self.charityData)
        self.assertTrue(result)

    def test_charityData_valid(self):
        errors = self.charitySchema.validate(self.charityData)
        self.assertEqual(errors, {})

    def test_charityData_invalid(self):
        invalid_charityData = self.charityData.copy()
        invalid_charityData.pop('name')
        errors = self.charitySchema.validate(invalid_charityData)
        self.assertNotEqual(errors, {})

if __name__ == '__main__':
    unittest.main()