print('Welcome to Book My Show')
ch=input('enter the theatre(PVR or INOX):')
l=['PVR','INOX']
if ch in l:
    if ch ==l[0]:
        print("Movies available in PVR:\n1. Avatar\n2. Batman")
        a=int(input('Select the number (1 or 2):'))
        if a==1:
            print('You have selected Avatar Movie\nThe ticktet price of the movie is - Rs.60')
            b=input('Confirm your ticket booking(yes or no):')
            if b=='yes':
                print('Booking succesfully completed\nYour show time is 7:00 pm\nYour Booking Id: 123')
            elif b=='no':
                print('Your booking is cancelled\nPlease Try Again')
            else:
                print('Wrong Input')
        if a==2:
            print('You have selected Batman Movie\nThe ticket price of the movie is - Rs.100')
            c=input('Confirm your booking(yes or no):')
            if c=='yes':
                print('Booking succesfully completed\nYour show time is 3:00 pm\nYour Booking Id: 555')
            elif c=='no':
                print('Your Booking is Cancelled\nPlease Try Again')
    if ch==l[1]:
        print('Movies available in INOX\n1.SALAAR\n2.PUSHPA 3')
        d=int(input('select the movie number(1 or 2):'))
        if d==1:
            print('You have selected SALAAR movie\nThe ticket price of the movie is - Rs.4000')
            g=input('Confirm your ticket booking(yes or no):')
            if g=='yes':
                print('Booking Sucessfully completed\nYour show time is 3:00 pm\nYour Booking Id: 222')
            elif g=='no':
                print('Your Booking is cancelled \nPlease Try Again')
            else:
                print('wrong input')
        if d==2:
            print('You have selected PUSHPA 3\nThe ticket price of the movie is - Rs.6000')
            e=input('Confirm your ticket booking(yes or no):')
            if e=='yes':
                print('Booking sucesfully completed\nYour show time is 5:00 pm\nYour Booking Id: 666')
            elif e=='no':
                print('Your booking is cancelled sucessfully\nPlease Try Again')
else:
    print('Theatre name is not Available')
