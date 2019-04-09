import unittest
from  Movie_ticket_vending import *

class MovieTicketVending(unittest.TestCase):

    def test_user_option_one(self):
        user_option = 'Captain Marvel'
        self.assertEqual(theatre_showtime_movie[user_option]['theatre'],'mudra')

    def test_user_option_two(self):
        user_option = 'Lucifer'
        self.assertEqual(theatre_showtime_movie[user_option]['time'],'6.00PM')

    def test_user_option_three(self):
        user_option = 'Thadam'
        self.assertNotEqual(theatre_showtime_movie[user_option]['seats'], 50)

    def test_user_wish_one(self):
        seat_type = 'I'
        self.assertEqual(ticket_type[seat_type], 'Rs 250')

    def test_user_wish_two(self):
        seat_type = 'II'
        self.assertEqual(ticket_type[seat_type], 'Rs 150')

    def test_user_wish_three(self):
        seat_type = 'III'
        self.assertNotEqual(ticket_type[seat_type], 'Rs 75')

    def test_leftover_seats_one(self):
        leaftover_seats = theatre_showtime_movie[user_option]['seats'] -1
        self.assertNotEqual(theatre_showtime_movie[user_option]['seats'] -1, 49)

    def test_leftover_seats_two(self):
        leaftover_seats = theatre_showtime_movie[user_option]['seats'] -1
        self.assertEqual(theatre_showtime_movie[user_option]['seats'] -1, 24)

    
if __name__== '__main__':
    unittest.main()
