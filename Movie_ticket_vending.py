""" Movie ticket vending and a platform to manage theatres"""
import sys
import csv

movies = ['Captain Marvel', 'Airaa', 'Lucifer', 'Thadam', 'Super delux','Joseph']
theatre_showtime_movie = {'Captain Marvel':{'theatre':'mudra', 'seats': 50, 'time':'9.30AM'},
                          'Airaa':{'theatre':'mudra', 'seats': 50, 'time':'1.30PM'},
                          'Lucifer':{'theatre':'mudra', 'seats': 50, 'time':'6.00PM'},
                          'Thadam':{'theatre':'keerthi', 'seats': 25, 'time':'9.30AM'},
                          'Joseph':{'theatre':'keerthi', 'seats': 25, 'time':'1.30PM'},
                          'Super delux':{'theatre':'keerthi', 'seats': 25, 'time':'6.00PM'}}
balance_seats_after_booking = []
ticket_type= {'I': 'Rs 250', 'II': 'Rs 150', 'III': 'Rs 75'}

user_option= raw_input("select a movie: ")

def getDetails(user_option):
    
    """Getting details of theatre, show time and seat available when user selects a movie"""
    return "theatre, seats and show time are:",theatre_showtime_movie[user_option]['theatre'],theatre_showtime_movie[user_option]['seats'],theatre_showtime_movie[user_option]['time']


def getSeattype():
    """Getting the seat type and price accordingly"""
    user_wish = raw_input("Do you want to book ticket for this movie? Select Y or N ")
    if user_wish == str('y'):
        seat_type = raw_input("Select seat type I II or III ")
        return "Ticket price: ",ticket_type[seat_type]


def getBooked():
    """Booking the seats"""
    booking = raw_input("To continue booking press Y ")
    if booking == str('y'):
        leftover_seats = theatre_showtime_movie[user_option]['seats'] -1
        balance_seats_after_booking.append(leftover_seats)
        return "left seats are: ",balance_seats_after_booking


def getPayed():
    """Payment making through netbanking or card"""
    payment = raw_input("To continue to payment press Y ")
    if payment == str('y'):
        payment_options = raw_input("1. Card payment\n 2. Netbanking ")
        if payment_options == str('1'):
            raw_input("Enter card no & cvv")
            return "Yay! payment successfull"
        elif payment_options == str('2'):
            raw_input ("Enter Customer ID & password")
            return "Yay! payment successfull"

def rebooking():
  """To rebook or not"""
    rebook = raw_input("Do you want to rebook Y or N? ")
    if rebook == str('y'):
        print getSeattype()
        leftover_seats = balance_seats_after_booking[0] -1
        balance_seats_after_booking.append(leftover_seats)
        return leftover_seats 
        print getPayed()
        
    elif rebook == str('n'):
        return "Thankyou! Enjoy your movies"
        sys.exit()
        
        
def getAllmovies():
  """ To list out all movies"""
    raw_input("To see all trending movies press Enter")
    return movies

  
def Movies_particular_theatre():
  """To see movies in particular theatre"""
    user_need_theatre = raw_input("Which theatre movies you want to see?")
    return movies_in_particular_theatre[user_need_theatre]['movies']   
    
                               

with open('Movie_vending_machine.csv', mode='w') as moviename_file:        #writing  csv file
    moviename_writer = csv.writer(moviename_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    moviename_writer.writerow(['Theatre', 'Show Timing', 'Movie name'])
    moviename_writer.writerow(['Mudra', '9.30AM', 'Captain Marvel'])
    moviename_writer.writerow(['Mudra', '1.30PM', 'Airaa'])
    moviename_writer.writerow(['Mudra', '6.00PM', 'Lucifer'])
    moviename_writer.writerow(['Keerthi', '9.30AM', 'Thadam'])
    moviename_writer.writerow(['Keerthi', '1.30PM', 'Josseph'])
    moviename_writer.writerow(['Keerthi', '6.00PM', 'Super Delux'])   



if __name__ == "__main__":                   #main program
    print getDetails(user_option)
    print getSeattype()
    print getBooked()
    print getPayed()
    print rebooking()
    print getAllmovies()
    print Movies_particular_theatre()
