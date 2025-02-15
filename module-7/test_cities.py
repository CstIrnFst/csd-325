# Nathan Maurer
# Advanced Python
# Assignment Module 7.2
# February 12, 2025

import unittest
from city_functions import city_country

print ("Enter 'q' at any time to quit.")
while True:
    city = input("\nProvide a city name: ")
    if city == 'q':
        break
    country = input("Provide that cities country: ")
    if country == 'q':
        break
    population = input("Provide population of the city: ")
    if population == 'q':
        break
    language = input("Provide language used in this city: ")
    if population == 'q':
        break

    full_location = city_country(city, country, population, language)
    print (f"{full_location}")

class LocationTestCase (unittest.TestCase):
    def test_city_country(self):
        full_location = city_country('Detroit', 'united states')
        self.assertEqual(full_location, 'Detroit, United States')

if __name__=='__main__':
    unittest.main()