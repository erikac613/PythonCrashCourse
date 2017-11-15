import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_and_country(self):
        """Do places like 'Toronto, Canada' work?"""
        formatted_city_and_country = city_country('toronto', 'canada')
        self.assertEqual(formatted_city_and_country, 'Toronto, Canada.')

    def test_city_country_pop(self):
        """Do locations with a given popuation work?"""
        formatted_city_and_country = city_country('moscow', 'russia', '12.19 million')
        self.assertEqual(formatted_city_and_country, 'Moscow, Russia: Population 12.19 Million.')

unittest.main()
