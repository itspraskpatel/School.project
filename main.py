''' ****************************************School project***************************************** '''
import datetime
import time
import sys
import mysql.connector as pysq
#setting up sql
conn=pysq.connect(host='localhost',user='root',passwd='')
#print(conn.is_connected()) will be True
crr=conn.cursor()

print('AIRPORTS ARE RUNNING AT LOW CAPACITY DUE TO THE PANDEMIC')
print("**********DUE TO COVID-19 OUTBREAK WE ARE FOLLOWING GUIDELINES AS PER ORDERED BY THE GOVERNMENT")

#delay
time.sleep(1)

#list of places
j = ["1. DELHI           AGRA                12HRS                222",
     "2. AGRA           LUCKNOW              13HRS                555",
     '3. LUCKNOW        BANGALORE            23HRS                230',
     '4. DELHI          LUCKNOW              33HRS                556',
     '5. BANGLORE       GORAKHPUR             5HRS                565',
     '6. LUCKNOW        DELHI                 6HRS                222',
     '7. AGRA           BHOPAL                6HRS                758',
     '8. DELHI          MUMBAI                7HRS                976']

#fare as list
farel = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]

#crating function for booking
def book():
    print("=" * 80)
    print("WELCOME TO BOOKING SECTION")
    print("ORIGIN         DESTINATION         TIME(in hours)         DISTANCE")
    for i in j:
        print(i)
    print("=" * 80)
    try:
        b = int(input("SELECT OPTION BASED ON YOUR JOURNEY:"))
        if b>8:
             print("Enter appropriate option")
             book()
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

#flight class
    print("=" * 80)
    print('SELECT CLASS OF YOUR JOURNEY')
    print('1. ECONOMY CLASS')
    print('2. BUSINESS CLASS')
    try:
        c = int(input("What's your Choice?:"))
        if c>2:
             print("=" * 80)
             print("Enter appropriate option")
             book()
    except:
        print("Enter appropriate option")

#flight meal
    print("=" * 80)
    print("DO YOU WANT IN-FLIGHT MEAL SERVICES ON YOUR JOURNEY?")
    print('1. YES')
    print('2. NO')
    try:
        d = int(input("What's your Choice?:"))
        if d>2:
             print("=" * 80)
             print("Enter appropriate option")
             book()

    except:
        print("=" * 80)
        print("Enter appropriate option")
        book()
    print("=" * 80)

#no. of tickets
    try:
        e = int(input("ENTER THE NO. OF TICKETS YOU WANT TO BOOK"))
    except:
        print("=" * 80)
        print("Enter appropriate no. of Passengers")
        book()
    if e > 5:
        print("WE HAVE LIMITED THE AMOUNT OF PASSENGERS PER BOOKING TO 5 PEOPLE DUE TO COVID-19 OUTBREAK")
        book()
        e = 0

#passenger details
    dd = {}
    ll = []
    if str(e).isdigit():
        for k in range(e):
            f = input("Enter name of passenger:")
            try:
                g = int(input("Enter Date of Birth in DDMMYYYY:"))
            except:
                print("Enter appropriate value")
                book()
            h = input("Enter Gender of Passenger(M or F):")
            print("=" * 80)
            print("=" * 80)
            if not (h.lower() == 'm' or h.lower() == 'f'):
                print("Enter appropriate option")
                book()
            dd = {"name": f, "dob": g, "gender": h}

            ll.append(dd)
    for m in range(len(ll)):
        mm = ll[m].values()
        lst = []
        for n in mm:
            lst.append(n)
            if len(lst) == 1:
                print('NAME OF PASSENGER: ', lst[0])
            elif len(lst) == 2:
                print('DATE OF BIRTH: ', lst[1])
            elif len(lst) == 3:
                print('GENDER: ', lst[2].upper())
    print("=" * 80)
    print("ABOVE ARE THE DEATILS OF THE PASSENGER")

    #fare calculation
    if d == 1 and c == 1:
        print("Total fare: ", int(fare + fare / 10) * e)
        sfare=int(fare + fare / 10) * e
    elif d == 1 and c == 2:
        print("Total fare: ", int(fare + fare / 10 + fare / 10) * e)
        sfare=int(fare + fare / 10 + fare / 10) * e
    elif d == 2 and c == 1:
        print("Total fare: ", int(fare) * e)
        sfare=int(fare) * e
    elif d == 2 and c == 2:
        print("Total fare: ", int(fare + fare / 10) * e)
        sfare=int(fare + fare / 10) * e
    try:
        qq = int(input("ENTER 1 TO CONFIRM"))
    except:
        print("Enter appropriate answer")
        book()
    print("=" * 80)
    if qq == 1:
        print("YOUR BOOKING HAS BEEN PLACED SUCCESSFULLY")
        bid=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bokid=""
        for i in bid:
            if i.isdigit():
                bokid+=i
        print("YOUR BOOKING ID IS: ",bokid)
    else:
        print("Enter appropriate value")
        book()
   # crr.execute("drop database airport")

#sql commands
    crr.execute("create database if not exists airport")
    crr.execute("use airport")
    sql="create table if not exists booking(bookid varchar(15) primary key,jour_no int(1),class int(1),meal int(1),tick_no int(1),fare int(5))"
    crr.execute(sql)
    sql1="insert into booking (bookid,jour_no,class,meal,tick_no,fare)values({},{},{},{},{},{})".format(bokid,b,c,d,e,sfare)
    crr.execute(sql1)
'''crr.execute("select * from booking")
    data=crr.fetchall()
    for i in data:
        print(i)'''

#for another booking
def ask():
        bb=input("do you want another booking(Y/N):")
        if bb.lower()=="y":
            book()
        elif bb.lower()=="n":
            print("THANK YOU")
        else:
            print("Enter appropriate value")
            ask()
        crr.execute("select * from booking")
        data=crr.fetchall()
        for i in data:
            print(i)

#Cancellation
def cancel():
    a=0

#starting
def start():
    print("=" * 80)
    print("WHAT YOU WANT TO DO ?")
    print("1.BOOKING")
    print('2.CANCELLATION')
    print('Press another ke to EXIT')
    a = int(input("Choose an Option: "))
    if a == 1:
        book()
    elif a == 2:
        None #cancel()
    else:
         print("=" * 80)
         print("Enter appropriate option")
         start()
start()
ask()
