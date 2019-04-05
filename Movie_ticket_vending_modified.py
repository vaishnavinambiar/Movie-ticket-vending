""" Movie ticket vending and a platform to manage Keerthi and Mudra theatre"""
import sys
import csv

theatre_and_seats = { 'keerthi' : 50, 'mudra' : 25}              #total number of seats in keerthi and mudra
leftover_seats = []
movies = ['Captain Marvel', 'Airaa', 'Lucifer', 'Thadam', 'Super delux','Joseph']  #list of movies running all over
movies_in_keerthi = ['Captain Marvel', 'Airaa', 'Lucifer']             #movies running in keerthi
movies_in_mudra = ['Thadam', 'Super delux','Joseph']                   #movies running in mudra
price = ['Rs 250', 'Rs 150', 'Rs 75']
movies_and_show_details = {"Keerthi":('9.30AM: Captain Marvel','1.30PM: Airaa','6.00PM: Lucifer'),"Mudra": ('9.30AM: Thadam', '1.30PM: Super delux','6.00PM: Joseph')}    #movie and showtime list of both theatres

user_option = raw_input("Which theatre do you select?\n 1.Keerthi\n 2.Mudra  ")   
seat_select = raw_input("select seat type. I II or III? ")
show_time = raw_input("Enter the show time: 9.30AM 1.30PM 6.00PM ")

def getLeftoverseats():
    """ Decrementing from total seat and showing current seat current in keerthi and mudra theatres"""
    if user_option == str('1'):
        leaftoverseats_keerthi = (theatre_and_seats.get('keerthi')) -1
        leftover_seats.append(leaftoverseats_keerthi)
        return leftover_seats 
    elif user_option == str('2'):
        leaftoverseats_mudra = (theatre_and_seats.get('mudra')) -1
        leftover_seats.append(leaftoverseats_mudra)
        return leftover_seats


def getTicket():
    """ Ticket issueing according to user option and seat selected"""
    if user_option == str('1') and seat_select == str('I'):
        return "Price: ",price[0]
    elif user_option == str('1') and seat_select == str('II'):
        return "Price: ",price[1]
    elif user_option == str('1') and seat_select == str('III'):
        return "Price: ",price[2]
    elif user_option == str('2') and seat_select == str('I'):
        return "Price: ",price[0]
    elif user_option == str('2') and seat_select == str('II'):
        return "Price: ",price[1]
    elif user_option == str('2') and seat_select == str('III'):
        return "Price: ",price[2]

def getBooked():
    """ Booking movie according to user option and show time"""
    if user_option == str('1') and show_time == str('9.30AM'):
        return "Movie name: ",movies_in_keerthi[0]
    elif user_option == str('1') and show_time == str('1.30PM'):
        return "Movie name: ",movies_in_keerthi[1]
    elif user_option == str('1') and show_time == str('6.00PM'):
        return "Movie name: ",movies_in_keerthi[2]
    elif user_option == str('2') and show_time == str('9.30AM'):
        return "Movie name: ",movies_in_mudra[0]
    elif user_option == str('2') and show_time == str('1.30PM'):
        return "Movie name: ",movies_in_mudra[1] 
    elif user_option == str('2') and show_time == str('6.00PM'):
        return "Movie name: ",movies_in_mudra[2]

def Option_to_select():
    """Giving options for users to view movie list"""
    more_option = raw_input("For more options:\n a. Show all running movies\n b. Show movies in particular theatre\n c. Show all details of show in all theatres ")
    if more_option == str('a'):
        return movies
    elif more_option == str('b'):
        select_theatre = raw_input("Select the theatre Keerthi or Mudra ie, enter 1 or 2 respectively ")
        if select_theatre == str('1'):
            return movies_in_keerthi
        elif select_theatre == str('2'):
            return movies_in_mudra
    elif more_option == str('c'):
        return movies_and_show_details

with open('moviename.csv', mode='w') as moviename_file:        #writing  csv file
    moviename_writer = csv.writer(moviename_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    moviename_writer.writerow(['Theatre', 'Show Timing', 'Movie name\n'])
    moviename_writer.writerow(['Keerthi', '9.30AM', movies_in_keerthi[0]])
    moviename_writer.writerow(['Keerthi', '1.30PM', movies_in_keerthi[1]])
    moviename_writer.writerow(['Keerthi', '6.00PM', movies_in_keerthi[2]])
    moviename_writer.writerow(['Mudra', '9.30AM', movies_in_mudra[0]])
    moviename_writer.writerow(['Mudra', '1.30PM',  movies_in_mudra[1]])
    moviename_writer.writerow(['Mudra', '6.00PM',  movies_in_mudra[2]])
    
       
if __name__ == "__main__":                                 #main function
    print getLeftoverseats()
    print getTicket()
    print getBooked()
    print ("Theatre: ",user_option)
    print ("Seat type: ",seat_select)
    print ("Show time: ",show_time)
    print Option_to_select()
