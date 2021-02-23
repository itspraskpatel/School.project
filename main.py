import datetime
import time
import sys
import mysql.connector as pysq
import smtplib, ssl

print('**********AIRPORTS ARE RUNNING AT LOW CAPACITY DUE TO THE PANDEMIC**********')
print("**********DUE TO COVID-19 OUTBREAK WE ARE FOLLOWING GUIDELINES AS PER ORDERED BY THE GOVERNMENT**********")

# delay
time.sleep(1)

# list of places
j = ["1. DELHI           AGRA                12HRS                222",
     "2. AGRA           LUCKNOW              13HRS                555",
     '3. LUCKNOW        BANGALORE            23HRS                230',
     '4. DELHI          LUCKNOW              33HRS                556',
     '5. BANGLORE       GORAKHPUR             5HRS                565',
     '6. LUCKNOW        DELHI                 6HRS                222',
     '7. AGRA           BHOPAL                6HRS                758',
     '8. DELHI          MUMBAI                7HRS                976']

# fare as list
farel = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888]


# creating function for booking
def book():
    # setting up sql
    conn = pysq.connect(host='localhost', user='root', passwd='')
    # print(conn.is_connected()) will be True
    crr = conn.cursor()

    # code
    print("=" * 80)
    print("WELCOME TO BOOKING SECTION")
    print("=" * 80)
    print("ORIGIN         DESTINATION         TIME(in hours)         DISTANCE")
    for i in j:
        print(i)
    print("=" * 80)
    try:
        b = int(input("ENTER NUMBER RESPECTIVE TO YOUR JOURNEY: "))
        if b > 8:
            print("=" * 80)
            print("ENTER APPROPRIATE OPTION")
            book()
    except:
        print("=" * 80)
        print("ENTER APPROPRIATE OPTION")
        book()

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

    # flight class
    print("=" * 80)
    mail = input("ENTER YOUR E-MAIL ID: ")
    print("=" * 80)
    print('SELECT CLASS OF YOUR JOURNEY')
    print('1. ECONOMY CLASS')
    print('2. BUSINESS CLASS')
    print("*EXTRA CHARGES WILL BE APPLIED")
    print("")
    try:
        c = int(input("WHAT'S YOUR CHOICE?: "))
        if c > 2:
            print("=" * 80)
            print("ENTER APPROPRIATE OPTION")
            book()
    except:
        print("=" * 80)
        print("ENTER APPROPRIATE OPTION")
        book()

    # flight meal
    print("=" * 80)
    print("DO YOU WANT IN-FLIGHT MEAL SERVICES ON YOUR JOURNEY?")
    print("*EXTRA CHARGES WILL BE APPLIED")
    print("")
    print('1. YES, I WANT')
    print("2. NO, I DON'T WANT")
    try:
        d = int(input("WHAT'S YOUR CHOICE?: "))
        if d > 2:
            print("=" * 80)
            print("ENTER APPROPRIATE OPTION")
            book()

    except:
        print("=" * 80)
        print("ENTER APPROPRIATE OPTION")
        book()
    print("=" * 80)

    # no. of tickets
    try:
        e = int(input("ENTER THE NO. OF TICKETS YOU WANT TO BOOK: "))
        print("=" * 80)
    except:
        print("=" * 80)
        print("ENTER APPROPRIATE NUMBER OF PASSENGERS")
        book()
    if e > 5:
        print("WE HAVE LIMITED THE AMOUNT OF PASSENGERS PER BOOKING TO 5 PEOPLE DUE TO COVID-19 OUTBREAK")
        book()
        e = 0

    # passenger details
    dd = {}
    ll = []
    if str(e).isdigit():
        for k in range(e):
            f = input("ENTER NAME OF PASSENGER: ")
            try:
                g1 = input("ENTER DATE OF BIRTH IN DD/MM/YYYY (use /): ")
                g2 = g1.split('/')
                g = ''
                for gg in g2:
                    g += gg
                leng = len(g1)
                if leng > 10:
                    print("ENTER APPROPRIATE DATE")
                    book()
                elif leng < 10:
                    print("ENTER APPROPRIATE DATE")
                    book()
                day, month, year = g1.split('/')
                isValidDate = True
                try:
                    datetime.datetime(int(year), int(month), int(day))
                except ValueError:
                    isValidDate = False
                if (isValidDate):
                    None
                else:
                    print("ENTER APPROPRIATE DATE")
                    book()
            except:
                print("ENTER APPROPRIATE VALUE")
                book()
            h = input("Enter Gender of Passenger(M or F):")
            print("=" * 80)
            print("=" * 80)
            if not (h.lower() == 'm' or h.lower() == 'f'):
                print("ENTER APPROPRIATE VALUE")
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

    # fare calculation
    if d == 1 and c == 1:
        print("Total fare: ", int(fare + fare / 10) * e)
        sfare = int(fare + fare / 10) * e
    elif d == 1 and c == 2:
        print("Total fare: ", int(fare + fare / 10 + fare / 10) * e)
        sfare = int(fare + fare / 10 + fare / 10) * e
    elif d == 2 and c == 1:
        print("Total fare: ", int(fare) * e)
        sfare = int(fare) * e
    elif d == 2 and c == 2:
        print("Total fare: ", int(fare + fare / 10) * e)
        sfare = int(fare + fare / 10) * e
    try:
        qq = input("ENTER 'Y' TO CONFIRM: ")
    except:
        print("ENTER APPROPRIATE OPTION")
        book()
    print("=" * 80)
    if qq.lower() == 'y':
        print("YOUR BOOKING HAS BEEN PLACED SUCCESSFULLY")
        bid = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        bokid = ""
        for i in bid:
            if i.isdigit():
                bokid += i
        print("YOUR BOOKING ID IS: ", bokid)
    else:
        print("ENTER APPROPRIATE VALUE")
        book()

    # sql commands
    crr.execute("create database if not exists airport")
    crr.execute("use airport")
    sql = "create table if not exists booking(bookid varchar(15) primary key,jour_no int(1),class int(1),meal int(1),tick_no int(1),fare int(5))"
    crr.execute(sql)
    sql1 = "insert into booking (bookid,jour_no,class,meal,tick_no,fare)values({},{},{},{},{},{})"
    sql1_ = sql1.format(bokid, b, c, d, e, sfare)
    crr.execute(sql1_)
    conn.commit()
    sql2 = "create table if not exists details(sn_no int(5) primary key,name varchar(20),dob varchar(15),gender char(1),bookid varchar(15) REFERENCES booking(bookid))"
    crr.execute(sql2)

    # calculate max serial no.
    sql3 = "select max(sn_no) from details"
    crr.execute(sql3)
    maxx = crr.fetchone()
    fmax = 0
    if maxx == (None,):
        fmax = 1
    else:
        for i in maxx:
            fmax += i
    fmax = int(fmax + 1)
    for m in range(len(ll)):
        mm = ll[m].values()
        lst = []
        for n in mm:
            lst.append(n)
            if len(lst) == 1:
                sqname = lst[0]
            elif len(lst) == 2:
                sqdob = lst[1]
            elif len(lst) == 3:
                sqgender = lst[2].upper()
        sql3 = "select max(sn_no) from details"
        crr.execute(sql3)
        maxx = crr.fetchone()
        fmax = 0
        if maxx == (None,):
            fmax = 1
        else:
            for i in maxx:
                fmax += i
        fmax = int(fmax + 1)
        sql4 = "insert into details (sn_no,name,dob,gender,bookid)values({},'{}',{},'{}',{})"
        sql5 = sql4.format(fmax, sqname, sqdob, sqgender, bokid)
        crr.execute(sql5)
        conn.commit()

        """crr.execute("select * from booking")
        data=crr.fetchall()
        for i in data:
        print(i,"____booking")

        crr.execute("select * from details")
        data=crr.fetchall()
        for i in data:
            print(i,"_____detail")"""

        # mailing
        try:
            data1 = 'YOUR BOOKING HAS BEEN PLACED SUCCESSFULLY\n'
            data2 = 'YOUR BOOOKING ID IS:\n'
            data3 = bokid
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "progpurpose@gmail.com"  # Enter your address
            receiver_email = "{}".format(mail)  # Enter receiver address
            password = "programpurpose"
            message = """\
            Subject: Flight Booking

            {}{}{}""".format(data1, data2, data3)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        except:
            print('=' * 80)
        crr.close()
        conn.close()


# for another booking
def ask():
    bb = input("do you want another booking(Y/N):")
    if bb.lower() == "y":
        book()
    elif bb.lower() == "n":
        print("THANK YOU")
    else:
        print("Enter appropriate value")
        ask()


# Cancellation
def cancel():
    # setting up sql
    conn = pysq.connect(host='localhost', user='root', passwd='')
    # print(conn.is_connected()) will be True
    crr = conn.cursor()

    print("************************************CANCELLATION*************************************")
    cc = "Enter your booking ID to cancel"
    r = input(cc)
    print("=" * 80)
    mail = input("Enter your e-mail ID")
    print("=" * 80)
    sql8 = "use airport"
    crr.execute(sql8)

    sql9 = "select count(*) from booking where bookid={}"
    sql10 = sql9.format(r)
    crr.execute(sql10)
    am = crr.fetchone()

    sql6 = "select * from booking where bookid={}"
    sql7 = sql6.format(r)
    crr.execute(sql7)
    ab = crr.fetchone()
    print("Following are the details of the booking:")
    print("=" * 80)

    # journey destinations
    j = ["DELHI           AGRA                12HRS                222",
         "AGRA           LUCKNOW              13HRS                555",
         'LUCKNOW        BANGALORE            23HRS                230',
         'DELHI          LUCKNOW              33HRS                556',
         'BANGLORE       GORAKHPUR             5HRS                565',
         'LUCKNOW        DELHI                 6HRS                222',
         'AGRA           BHOPAL                6HRS                758',
         'DELHI          MUMBAI                7HRS                976']
    try:
        ac = ab[0]  # bookid
        ad = ab[1]  # journo
        ae = ab[2]  # class
        af = ab[3]  # meal
        ag = ab[4]  # no. of tickets
        ah = ab[5]  # fare
        # ai=j[ad]#desination
        print("BOOKING ID:", ac)
        print("=" * 80)
        print("ORIGIN         DESTINATION         TIME(in hours)         DISTANCE")
        if ad == 1:
            print(j[0])
            print("=" * 80)
        elif ad == 2:
            print(j[1])
            print("=" * 80)
        elif ad == 3:
            print(j[2])
            print("=" * 80)
        elif ad == 4:
            print(j[3])
            print("=" * 80)
        elif ad == 5:
            print(j[4])
            print("=" * 80)
        elif ad == 6:
            print(j[5])
            print("=" * 80)
        elif ad == 7:
            print(j[6])
            print("=" * 80)
        elif ad == 8:
            print(j[7])
            print("=" * 80)
        if ae == 1:
            clss = "ECONOMY CLASS"
        else:
            clss = "BUSINESS CLASS"
        print("CLASS: ", clss)
        print("=" * 80)
        if af == 1:
            meal = "YES"
        else:
            meal = "NO"
        print("IN-FLIGHT MEAL: ", meal)
        print("=" * 80)
        print("NUMBER OF TICKETS: ", ag)
        print("=" * 80)
        print("TOTAL FARE: ", ah)
        print("=" * 80)
        print("DO YOU REALLY WANT TO CANCEL YOUR BOOKING?")
        print("TYPE YES TO CONFIRM OR NO TO CANCEL")
        aj = input("ENTER YOUR CHOICE: ")
        if aj.lower() == "yes":
            sql9 = "delete  from details where bookid={}"
            sql10 = sql9.format(r)
            crr.execute(sql10)
            sql11 = "delete from booking where bookid={}"
            sql12 = sql11.format(r)
            crr.execute(sql12)
            print("YOUR BOOKING HAS BEEN CANCELLED SUCCESSFULLY")
            bid = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            canid = ""
            for i in bid:
                if i.isdigit():
                    canid += i
            # mail
            try:
                data1 = '\nYOUR BOOKING HAS BEEN CANCELLED SUCCESSFULLY\n'
                data2 = 'YOUR CANCELLATION ID IS:\n'
                data3 = canid

                port = 465  # For SSL
                smtp_server = "smtp.gmail.com"
                sender_email = "progpurpose@gmail.com"  # Enter your address
                receiver_email = "{}".format(mail)  # Enter receiver address
                password = "programpurpose"
                message = """\
                Subject: Flight Booking

                {}{}{}""".format(data1, data2, data3)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)
            except:
                print('*' * 80)
            """crr.execute("select * from details")
            data=crr.fetchall()
            for i in data:
            print(i,"_____detail")#just to check"""
            print("=" * 80)
        elif aj.lower() == "no":
            print("THANK YOU")
            print("=" * 80)
            sys.exit()
        else:
            ("ENTER APPROPRIATE VALUE")
            cancel()
        print("DO YOU WANT ANY OTHER BOOKING/CANCELLATION?")
        print("Enter Y/N")
        al = input("ENTER YOUR CHOICE: ")
        if al == "y" or al == "Y":
            start()
        elif al == "n" or al == 'N':
            print("THANK YOU")
            sys.exit()
        else:
            print("ENTER CORRECT CHOICE")
    except TypeError:
        print("NO BOOKING FOUND ON THIS BOOKING ID")
        print("=" * 80)
        print("=" * 80)
        cancel()
    crr.close()
    conn.close()


# starting
def start():
    print("=" * 80)
    print("WHAT YOU WANT TO DO ?")
    print("1.BOOKING")
    print('2.CANCELLATION')
    print('ENTER ANY OTHER VALUE TO EXIT')
    a = input("CHOOSE AN OPTION: ")
    if a == "1":
        book()
        ask()
    elif a == "2":
        cancel()
    else:
        print("=" * 80)
        sys.exit()
        start()
start()
# install this via cmd:
# python -m smtpd -c DebuggingServer -n localhost:1025
