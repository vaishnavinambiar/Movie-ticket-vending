import unittest
import sys
from movie4 import *

class MyTest(unittest.TestCase):
    def test_one(self):
        movies = ['Captain Marvel', 'Airaa', 'Lucifer', 'Thadam', 'Super delux','Joseph']
        self.assertEqual(movies[0], 'Captain Marvel')

    def test_two(self):
        movies_in_keerthi = ['Captain Marvel', 'Airaa', 'Lucifer']
        self.assertTrue(True)

    def test_three(self):
        movies_in_mudra = ['Thadam', 'Super delux','Joseph']
        self.assertNotEqual(movies_in_mudra[0], 'Captain Marvel')

    def test_four(self):
        theatres_and_seats =  { 'keerthi' : 50, 'mudra' : 25}
        self.assertEqual(theatres_and_seats.get('keerthi'), 50)

    def test_five(self):
        leaftoverseats_mudra = (theatre_and_seats.get('mudra')) -1
        self.assertNotEqual(leaftoverseats_mudra, 24)
        
        


if __name__== '__main__':
    unittest.main()
