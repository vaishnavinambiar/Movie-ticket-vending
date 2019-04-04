""" Movie ticket vending and a platform to manage Keerthi and Mudra theatre"""
import sys
import csv

total_seat_keerthi =50                 #total number of seats in keerthi
total_seat_mudra = 25                  #total number of seats in mudra
movies = ['Captain Marvel', 'Airaa', 'Lucifer', 'Thadam', 'Super delux','Joseph']  #list of movies running all over
movies_in_keerthi = ['Captain Marvel', 'Airaa', 'Lucifer']             #movies running in keerthi
movies_in_mudra = ['Thadam', 'Super delux','Joseph']                   #movies running in mudra
price = ['Rs 250', 'Rs 150', 'Rs 75']
movies_and_show_details = {"Keerthi":('9.30AM: Captain Marvel','1.30PM: Airaa','6.00PM: Lucifer'),"Mudra": ('9.30AM: Thadam', '1.30PM: Super delux','6.00PM: Joseph')}    #movie and showtime list of both theatres

user_option = raw_input("Which theatre do you select? Keerthi/Mudra ")   
seat_select = raw_input("select seat type. I II or III? ")
show_time = raw_input("Enter the show time: 9.30AM 1.30PM 6.00PM ")

def getCount_in_keerthi():
    """ Decrementing from total seat and showing current seat current in keerthi"""
    if user_option == str('keerthi'):
        count_one = total_seat_keerthi -1
        return "Balance seat: ",count_one

def getCount_in_mudra():
    """ Decrementing from total seat and showing current seat current in mudra"""
    if user_option == str('mudra'):
        count_two = total_seat_mudra -1
        return "Balance seat: ",count_two

def getTicket():
    """ Ticket issueing according to user option and seat selected"""
    if user_option == str('keerthi') and seat_select == str('I'):
        return "Price: ",price[0]
    elif user_option == str('keerthi') and seat_select == str('II'):
        return "Price: ",price[1]
    elif user_option == str('keerthi') and seat_select == str('III'):
        return "Price: ",price[2]
    elif user_option == str('mudra') and seat_select == str('I'):
        return "Price: ",price[0]
    elif user_option == str('mudra') and seat_select == str('II'):
        return "Price: ",price[1]
    elif user_option == str('mudra') and seat_select == str('III'):
        return "Price: ",price[2]

def getMovie_booked():
    """ Booking movie according to user option and show time"""
    if user_option == str('keerthi') and show_time == str('9.30AM'):
        return "Movie name: ",movies_in_keerthi[0]
    elif user_option == str('keerthi') and show_time == str('1.30PM'):
        return "Movie name: ",movies_in_keerthi[1]
    elif user_option == str('keerthi') and show_time == str('6.00PM'):
        return "Movie name: ",movies_in_keerthi[2]
    elif user_option == str('mudra') and show_time == str('9.30AM'):
        return "Movie name: ",movies_in_mudra[0]
    elif user_option == str('mudra') and show_time == str('1.30PM'):
        return "Movie name: ",movies_in_mudra[1] 
    elif user_option == str('mudra') and show_time == str('6.00PM'):
        return "Movie name: ",movies_in_mudra[2]

def getOption_to_select():
    """Giving options for users to view movie list"""
    option = raw_input(" 1. Show all running movies\n 2. Show movies in particular theatre\n 3. Show all details of show in all theatres ")
    if option == str('1'):
        return movies
    elif option == str('2'):
        select_theatre = raw_input("Select the theatre Keerthi or Mudra ")
        if select_theatre == str('keerthi'):
            return movies_in_keerthi
        elif select_theatre == str('mudra'):
            return movies_in_mudra
    elif option == str('3'):
        return movies_and_show_details

with open('revenue.csv', mode='w') as revenue_file:        #writing to csv file
    revenue_writer = csv.writer(revenue_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    revenue_writer.writerow(['Theatre', 'Show Timing', 'Total amount sold\n'])
    revenue_writer.writerow(['Keerthi', '9.30AM', 'Rs 2589'])
    revenue_writer.writerow(['Keerthi', '1.30PM', 'Rs 4523'])
    revenue_writer.writerow(['Keerthi', '6.00PM', 'Rs 968\n\n\n'])
    revenue_writer.writerow(['Mudra', '9.30AM', 'Rs 8589'])
    revenue_writer.writerow(['Mudra', '1.30PM', 'Rs 523'])
    revenue_writer.writerow(['Mudra', '6.00PM', 'Rs 568'])
    
       
if __name__ == "__main__":                                 #main function
    print getCount_in_keerthi()
    print getCount_in_mudra()
    print getTicket()
    print getMovie_booked()
    print ("Theatre: ",user_option)
    print ("Seat type: ",seat_select)
    print ("Show time: ",show_time)
    print getOption_to_select()
