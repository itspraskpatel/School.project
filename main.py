''' ********************************School project********************** '''
import time
import sys
import mysql.connector as pysq

print('AIRPORTS ARE RUNNING AT LOW CAPACITYL')
print("**********DUE TO COVID-19 OUTBREAK WE ARE FOLLOWING GUIDELINES AS PER ORDERED BY THE GOVERNMENT")
time.sleep(1)
j = ["1. DELHI           AGRA                12HRS                222",
     "2. AGRA           LUCKNOW              13HRS                555",
     '3. LUCKNOW        BANGLORE             23HRS                230',
     '4. DELH           LUCKNOW              33HRS                556',
     '5. BANGLORE       GORAKHPUR             5HRS                565',
     '6. LUCKNOW        DELHI                 6HRS                222',
     '7. AGRA           BHOPAL                6HRS                758',
     '8. DELHI          MUMBAI                7HRS                976']
farel = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]


# '''print("ORIGIN         DESTINATION         TIME(in hours)         DISTANCE")
# for i in j:
#    print(i) '''
def book():
    print("=" * 80)
    print("WELCOME TO BOOKING SECTION")
    print("ORIGIN         DESTINATION         TIME(in hours)         DISTANCE")
    for i in j:
        print(i)
    print("=" * 80)
    try:
        b = int(input("SELECT OPTION BASED ON YOUR JOURNEY:"))
    except:
        print("Enter appropriate option")
    # fare calculation
    fare = 0
    if b == 1:
        fare = farel[0]
    elif b == 2:
        fare = farel[1]
    elif b == 3:
        fare = farel[2]
    elif b == 4:
        fare = farel[3]
    elif b == 5:
        fare = farel[4]
    elif b == 6:
        fare = farel[5]
    elif b == 7:
        fare = farel[6]
    elif b == 8:
        fare = farel[7]
    print("=" * 80)
    print('SELECT CLASS OF YOUR JOURNEY')
    print('1. ECONOMY CLASS')
    print('2. BUSINESS CLASS')
    try:
        c = int(input("What's your Choice?:"))
    except:
        print("Enter appropriate option")
    print("=" * 50)
    print("DO YOU WANT CATERING SERVICE ON YOUR JOURNEY?")
    print('1. YES')
    print('2. NO')
    try:
        d = int(input("What's your Choice?:"))
    except:
        print("Enter appropriate option")
    print("=" * 80)
    try:
        e = int(input("ENTER THE NO. OF TICKETS YOU WANT TO BOOK"))
    except:
        print("Enter appropriate no. of Passengers")
    if e > 5:
        print("WE HAVE LIMITED THE AMOUNT OF PASSENGERS PER BOOKING TO 5 PEOPLE DUE TO COVID-19 OUTBREAK")
        e = 0
    dd = {}
    ll = []
    if str(e).isdigit():
        for k in range(e):
            f = input("Enter name of passenger:")
            try:
                g = int(input("Enter Date of Birth in DDMMYYYY:"))
            except:
                print("Enter appropriate option")
            h = input("Enter Gender of Passenger(M or F):")
            print("=" * 80)
            print("=" * 80)
            if not (h.lower() == 'm' or h.lower() == 'f'):
                print("Enter appropriate option")
            dd = {"name": f, "dob": g, "gender": h}

            ll.append(dd)
    # print(ll)

    for m in range(len(ll)):
        mm = ll[m].values()
        # print(m)
        # print(mm)
        lst = []
        for n in mm:
            lst.append(n)
            if len(lst) == 1:
                print('NAME OF PASSENGER: ', lst[0])
            elif len(lst) == 2:
                print('DATE OF BIRTH: ', lst[1])
            elif len(lst) == 3:
                print('GENDER: ', lst[2].upper())
    print("ABOVE ARE THE DEATILS OF THE PASSENGER")
    if d == 1 and c == 1:
        print("Total fare: ", int(fare + fare / 10) * e)
    elif d == 1 and c == 2:
        print("Total fare: ", int(fare + fare / 10 + fare / 10) * e)
    elif d == 2 and c == 1:
        print("Total fare: ", int(fare) * e)
    elif d == 2 and c == 2:
        print("Total fare: ", int(fare + fare / 10) * e)
    try:
        qq = int(input("ENTER 1 TO CONFIRM"))
    except:
        print("Enter appropriate answer")
    if qq == 1:
        print("YOUR BOOKING HAS BEEN PLACES SUCCESSFULLY")
    # print(lst)


'''                print('NAME OF PASSENGER: ',lst[0])
            elif len(lst)==1:
                print('DATE OF BIRTH: ',lst[1])
            elif len(lst)==2:
                print('GENDER: ',lst[2])'''

# print(ll)
print("=" * 80)
print("WHAT YOU WANT TO DO ?")
print("1.BOOKING")
print('2.CANCELLATION')
print('Press another ke to EXIT')
a = int(input("Choose an Option"))
if a == 1:
    book()
elif a == 2:
    None #cancel()
else:
    print("THANK YOU")
