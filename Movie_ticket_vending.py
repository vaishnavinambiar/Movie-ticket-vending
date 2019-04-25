""" Movie ticket vending and a platform to manage theatres"""
import sys
import csv

theatres = ["mudra", "keerthi"]
showtimings = ["9.30AM", "1.30PM", "6.00PM"]
movies = ["Captain Marvel", "Airaa", "Lucifer", "Thadam", "Super delux", "Joseph"]
movies_in_particular_theatre = {"mudra":{"movies": "Captain-Marvel  Airaa  Lucifer", "time": "9.30AM  1.30PM  6.00PM"},
                                "keerthi":{"movies": "Thadam  Super-Delux  Joseph", "time": "9.30AM  1.30PM  6.00PM"}}
theatre_showtime_seats = {"Captain Marvel":{"theatre":"mudra", "seats": 50, "time":"9.30AM"},
                          "Airaa":{"theatre":"mudra", "seats": 50, "time":"1.30PM"},
                          "Lucifer":{"theatre":"mudra", "seats": 50, "time":"6.00PM"},
                          "Thadam":{"theatre":"keerthi", "seats": 25, "time":"9.30AM"},
                          "Joseph":{"theatre":"keerthi", "seats": 25, "time":"1.30PM"},
                          "Super delux":{"theatre":"keerthi", "seats": 25, "time":"6.00PM"}}
movie_and_theatre = {"9.30AM":{"theatre1":"mudra:", "movie1":"Captain Marvel", "theatre2":"keerthi:", "movie2":"Thadam"},
                     "1.30PM":{"theatre1":"mudra:", "movie1":"Airaa", "theatre2":"keerthi:", "movie2":"Joseph"},
                     "6.00PM": {"theatre1":"mudra:", "movie1":"Lucifer", "theatre2":"keerthi:", "movie2":"Super delux"}}
balance_seats_after_booking = []
ticket_type= {"I": "Rs 250", "II": "Rs 150", "III": "Rs 75"}


user_option = int(raw_input("Select any from Menu\n1.Theatres\n2.Movies\n3.Showtime "))

def getDetails():
    """Getting details of theatre, show time and seat available when user select from the menu"""
    if user_option == 1:
        return theatres
    elif user_option == 2:
        return movies
    elif user_option == 3:
        return showtimings
    else:
        return "Invalid"


def movies_theatre_and_showtime():
    """Fetching movies, theatres and showtime according to selected menu"""
    if user_option ==1:
        select_theatre=select_theatre = raw_input("Select a theatre: ")
        return movies_in_particular_theatre[select_theatre]["movies"],movies_in_particular_theatre[select_theatre]["time"]
    elif user_option ==2:
        select_movie = raw_input("Select a movie: ")
        return theatre_showtime_seats[select_movie]["theatre"],theatre_showtime_seats[select_movie]["time"]
    elif user_option == 3:
        select_showtime = raw_input("Select a showtime: ")
        print movie_and_theatre[select_showtime]["theatre1"], movie_and_theatre[select_showtime]["movie1"], movie_and_theatre[select_showtime]["theatre2"], movie_and_theatre[select_showtime]["movie2"]
        select_movie = raw_input("Select a movie you want ")
        return "Selected"
    else:
        return "Invalid"


def getSeattype():
    """Getting the seat type and price accordingly"""
    user_wish = raw_input("Do you want to book ticket for this movie? Select Y or N ")
    if user_wish == str("y"):
        seat_type = raw_input("Select seat type I II or III ")
        return ("Ticket price is ",ticket_type[seat_type],"and successfully booked")
    else:
        return "Invalid, Sorry try again!"
    sys.exit()
        


def getBooked():
    """Booking the seats"""
    if user_option == 1:
        fix_theatre = raw_input("Fix this theatre? Y or N ")
        if fix_theatre == str("y"):
            select_one_movie = raw_input("Which movie do you want in this theatre? ")
            print getSeattype()
        else:
            return "Invalid"

    elif user_option == 2:
        fix_movie = raw_input("Fix this movie? Y or N ")
        if fix_movie == str("y"):
            print getSeattype()
        else:
            return "Invalid"

    elif user_option == 3:
        fix_showtime = raw_input("Do you want to book ticket? Y or N ")
        if fix_showtime == str("y"):
            print getSeattype()
        else:
            print "Invalid"
            
            

def getPayed():
    """Payment making through netbanking or card"""
    payment = raw_input("To continue to payment press Y ")
    if payment == str("y"):
        payment_options = raw_input("1.Card payment\n2.Netbanking ")
        if payment_options == str("1"):
            int(input("Enter card no: "))
            int(input("Enter cvv: "))
            return "Yay! payment successfull"
        elif payment_options == str("2"):
            int(input("Enter Customer ID: "))
            raw_input("Enter ur transpassword: ")
            int(input("Enter the OSP number you recieved in registered mobile number: "))
            return "Yay! payment successfull"
    else:
        return "Invalid"



def getContinued():
    """To get continue booking"""
    continue_booking = raw_input("Do you want to rebook Y or N? ")
    if continue_booking == str("y"):
        print user_option
        print getDetails()
        print movies_theatre_and_showtime()
        print getSeattype()
        print getPayed()
    elif continue_booking == str("n"):
        return "Thankyou! Enjoy your movies"
    else:
        return "Invalid"



with open('Movie_vending_machine.csv', mode='w') as moviename_file:        #writing  csv file
    moviename_writer = csv.writer(moviename_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    moviename_writer.writerow(['Theatre', 'Show Timing', 'Movie name'])
    moviename_writer.writerow(['Mudra', '9.30AM', 'Captain Marvel'])
    moviename_writer.writerow(['Mudra', '1.30PM', 'Airaa'])
    moviename_writer.writerow(['Mudra', '6.00PM', 'Lucifer'])
    moviename_writer.writerow(['Keerthi', '9.30AM', 'Thadam'])
    moviename_writer.writerow(['Keerthi', '1.30PM', 'Josseph'])
    moviename_writer.writerow(['Keerthi', '6.00PM', 'Super Delux'])         
            
            


if __name__ == "__main__":
    print getDetails()
    print movies_theatre_and_showtime()
    print getBooked()
    print getPayed()
    print getContinued()
