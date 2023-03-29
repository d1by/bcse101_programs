import os
import re
import datetime 


cred = input("Enter {username : password}: ")
file1 = open('credentials.txt', 'r')

if(file1.read()!=cred):
    file1.close()
    print("Invalid password")
else:
    file1.close()
    regseats = 12
    tatseats = 3
    print("Main Menu")
    print("------------")
    print("1. Booking\n2. Cancellation\n3. Exit")
    menu = int(input("Enter choice: "))
    if(menu==1):
        totalcost = 0
        destcost = 0
        passengers = []
        print("Booking Menu")
        print("------------")
        print("A. Regular (%d Seats)\nB. Tatkal(%d Seats)"%(regseats, tatseats))
        seat = input("Enter choice: ").upper()
        print("Fare details from Bangalore")
        print("------------")
        print("Regular:")
        print("Hosur Rs75")
        print("Vaniyambadi Rs 250")
        print("Vellore Rs 500")
        print("Walaja Rs600")
        print("Chennai Rs750")
        print(f"*for senior citizen 10% concession (Age 60 and above)")
        print("Tatkal Booking fare - Rs100 addition to the regular fare")
        dest = input("Enter travel destination: ")
        if(dest=="Hosur"):
            destcost+=75
        elif(dest=="Vaniyambadi"):
            destcost+=250
        elif(dest=="Vellore"):
            destcost+=500
        elif(dest=="Walaja"):
            destcost+=600
        elif(dest=="Chennai"):
            destcost+=750
        else:
            print("Incorrect destination. ")
            exit()

        n = int(input("Enter number of passengers: "))
        for i in range(n):
            pname = input("Enter name: ")
            page = int(input("Enter age: "))
            cost = destcost
            if(seat=='B'):
                cost+=100
            if(page>=60):
                cost*=0.9
            passengers.append([pname, page, cost])
            f1 = open('passengerhist.txt', 'a')
            tempstr = str([pname, page, cost])
            f1.writelines(tempstr + "\n")
            f1.close()

        date = input("Enter date of journey: ")
        if(seat=='A'):
            if(regseats-n>=0):
                seatno = regseats
                regseats-=n
            else:
                print("Not enough seats. ")
                exit()
        elif(seat=='B'):
            seatno = tatseats
            if(tatseats-n>=0):
                tatseats-=n
            else:
                print("Not enough seats. ")
                exit()
    
        file1 = open('ticket.txt', 'w')
        file1.writelines("Remaining seats:")
        file1.writelines("\nRegular = " + str(regseats))
        file1.writelines("\nTatkal = " + str(tatseats))
        file1.writelines("\nPassenger Name - Age - Source - Destination - Seat No")
        for i in passengers:
            totalcost += i[2]
            temp = i[0] + " - " + str(i[1]) + " - " + "Bengaluru" + " - " + dest + " - " + str(seatno)
            file1.writelines("\n" + temp)
            seatno-=1
        file1.writelines("\nDate of Journey: " + str(date))
        file1.writelines("\nTotal fare: " + str(totalcost))
        file1.close()
    
    elif(menu==2):
        print("Cancellation Refund Details")
        print("----------------------------")
        print("20 days before the date of journey - full refund")
        print(f"2 weeks before the date of journey - 90% fare refund")
        print(f"1 week before the date of journey - 80% fare refund")
        print(f"4 days before the date of journey - 50% fare refund")
        print("<4 days - No refund")
        name = input("Enter passenger name: ")
        age = int(input("Enter passenger age: "))
        regexsearch = "^" + name + " - " + str(age) + ".*"
        f = open("ticket.txt", 'r')
        lines = f.readlines()
        f.close()
        f = open("ticket.txt", 'w')
        for line in lines:
            if re.findall("^Date of Journey.*", line):
                tdate = line[line.index(": ")+2::].strip()
            if re.findall(regexsearch, line):
                continue
            else:
                f.write(line)
        f.close()

        f = open("passengerhist.txt", 'r')
        lines = f.readlines()
        regexsearch2 = ".*" + name + ".*" + str(age) + ".*"
        tempstr2 = str(age) + ", "
        for line in lines:
            if re.findall(regexsearch2, line):
                cost = line[line.index(tempstr2):line.index(']'):]
                cost = int(float(cost[cost.index(" ")::].strip()))
        f.close()
        today = datetime.datetime.now()
        tripdate = datetime.datetime.strptime(tdate, f'%d-%m-%Y')
        diff = tripdate - today
        if(diff.days>14):
            refund = cost
        elif(diff.days>7 and diff.days<=14):
            refund = 0.9*cost
        elif(diff.days>4 and diff.days<=7):
            refund = 0.8*cost
        elif(diff.days==4):
            refund = 0.5*cost
        else:
            refund = 0

        cancel = cost - refund
        print("\nRefund amount: ", refund)
        print("Cancellation charge: ", cancel)