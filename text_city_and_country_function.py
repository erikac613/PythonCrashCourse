import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_and_country(self):
        """Do places like 'Toronto, Canada' work?"""
        formatted_city_and_country = city_country('toronto', 'canada')
        self.assertEqual(formatted_city_and_country, 'Toronto, Canada')

unittest.main()        
