import unittest
from Movie_ticket_vending import *

class MovieTicketVending(unittest.TestCase):

    def test_user_menu_theatres(self):
         user_option = 'Theatres'
         self.assertEqual(theatres,["mudra", "keerthi"])

    def test_user_menu_movies(self):
         user_option = 'Theatres'
         self.assertEqual(movies, ["Captain Marvel", "Airaa", "Lucifer", "Thadam", "Super delux", "Joseph"])

    def test_user_menu_showtime(self):
         user_option = 'Theatres'
         self.assertEqual(showtimings, ["9.30AM", "1.30PM", "6.00PM"])

    def test_user_wish_one(self):
        seat_type = 'I'
        self.assertEqual(ticket_type[seat_type], 'Rs 250')

    def test_user_wish_two(self):
        seat_type = 'II'
        self.assertFalse(ticket_type[seat_type], 'Rs 150')

    def test_user_wish_three(self):
        seat_type = 'III'
        self.assertEqual(ticket_type[seat_type], 'Rs 75')

    def test_cardpayment(self):
        payment_options = 'Card payment'
        card_number = 4563456987556
        cvv = 985
        self.assertNotEqual((card_number,cvv), (4563456987556,985))

    def test_netbanking(self):
        payment_options = 'Netbanking'
        customer_id = 445522663
        transaction_password= 'vaishnavi1996'
        osp_number = 852369
        self.assertTrue((customer_id,transaction_password,osp_number), (445522663,'vaishnavi1996',852369))
        
        
if __name__== '__main__':
    unittest.main()
