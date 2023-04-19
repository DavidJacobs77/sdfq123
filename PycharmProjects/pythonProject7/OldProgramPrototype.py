


import random


print("Welcome to the Help Desk Ticketing System Prototype.")
count = 0
TK = 2000
Update = 0
StValue = 0
statOv = 0
statCv = 0
status = 0
(tkv, tc, a, b, c, d, e, f, g, h, trp) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

(TK1, ticketcreator1, firstname1, surname1, staffID1, emailAd1, category1, descript1, priority1, status1, ticketresp1) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
(TK2, ticketcreator2, firstname2, surname2, staffID2, emailAd2, category2, descript2, priority2, status2, ticketresp2) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
(TK3, ticketcreator3, firstname3, surname3, staffID3, emailAd3, category3, descript3, priority3, status3, ticketresp3) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
(TK4, ticketcreator4, firstname4, surname4, staffID4, emailAd4, category4, descript4, priority4, status4, ticketresp4) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
(TK5, ticketcreator5, firstname5, surname5, staffID5, emailAd5, category5, descript5, priority5, status5, ticketresp5) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


def defcategory(v):
    if v == "1":
        slc = "Software"
    if v == "2":
        slc = "Hardware"

    if v == "3":
        slc = "Network"

    if v == "4":
        slc = "Virus Infection"

    if v == "5":
        slc = "Other"

    if v != "1" and v != "2" and v != "3" and v != "4" and v != "5":
        slc = 0

    return slc


def defpriority(v):
    if v == "1":
        slc = "HIGH"
    if v == "2":
        slc = "MEDIUM"
    if v == "3":
        slc = "LOW"
    if v != "1" and v != "2" and v != "3":
        slc = 0

    return slc


def defstatus(v):
    if v == "1":
        slc = 1
    if v == "2":
        slc = 2
    if v != "1" and v != "2":
        slc = 0

    return slc


def defstatus2(v):
    if v == "1":
        slc = 1
    if v == "2":
        slc = 2
    if v != "1" and v != "2":
        slc = 0

    return slc

def menuchoice(v):
    if v == "1":
        slc = 1
    if v == "2":
        slc = 2
    if v == "3":
        slc = 3
    if v != "1" and v != "2" and v != "3":
        slc = 0

    return slc

def ticketchoice(v):
    if v == "1" and count > 1:
        slc = 1
    if v == "2" and count > 2:
        slc = 2
    if v == "2" and count <= 2:
        slc = 0
    if v == "3" and count > 3:
        slc = 3
    if v == "3" and count <= 3:
        slc = 0
    if v == "4" and count > 4:
        slc = 4
    if v == "4" and count <= 4:
        slc = 0
    if v == "5" and count > 5:
        slc = 5
    if v == "5" and count <= 5:
        slc = 0
    if v == "0":
        slc = 100
    if v != "1" and v != "2" and v != "3" and v != "4" and v != "5" and v != "0":
        slc = 0

    return slc


def endchoice(v):
    if v == "1":
        slc = 1
    if v == "2":
        slc = 2
    if v == "3":
        slc = 3
    if v == "4":
        slc = 4
    if v == "5":
        slc = 5
    if v != "1" and v != "2" and v != "3" and v != "4" and v != "5":
        slc = 0

    return slc


def updatepriority(v):
    if v == "1":
        slc = 1
    if v == "2":
        slc = 2
    if v != "1" and v != "2":
        slc = 0

    return slc


def Statistics():
    return


def MainMenu():
    return


def TicketForm():
    return


def ViewTicket():
    return


def ViewUpdate():
    return




"""" This code is the home page of the program. It gives a selection of its functions and displays the number of open and closed tickets """

def MainMenu():
    global count
    global statOv
    global statCv
    global status1, status2, status3, status4, status5
    count = count + 1
    print("\nWhat would you like to do?\n")
    print("1. Create a new ticket")
    print("2. View tickets")

    def TicketStats():
        print("\nThe number of tickets submitted: ", TK - 2000)
        print("The number of tickets open for response: ", statOv)
        print("The number of tickets resolved: ", statCv)
    TicketStats()

    j = menuchoice(input("\nPlease select an item "))
    while j == 0:
        j = menuchoice(input("Please select a valid number "))
    if j == 1 and count >= 6:
        print("\n-------------------------------------------------------")
        print("\nThis action cannot be completed as the ticket folder is full")
        MainMenu()
    if j == 1 and count <= 5:
        print("New Ticket", count)
        TicketForm()
    if j == 2 and count == 1:
        print("\n-------------------------------------------------------")
        print("\nThere are no tickets in the folder to view")
        count = count - 1
        MainMenu()
    if j == 2 and count > 1:
        print("Prompt view tickets\n")
        ViewTicket()


MainMenu()

"""" This code is the input function of all the ticket's fields. It then displays the ticket with the inputed strings or values"""


def TicketForm():
    global count
    global TK
    global statOv
    global statCv
    global TK1, ticketcreator1, firstname1, surname1, staffID1, emailAd1, category1, descript1, priority1, status1, ticketresp1
    global TK2, ticketcreator2, firstname2, surname2, staffID2, emailAd2, category2, descript2, priority2, status2, ticketresp2
    global TK3, ticketcreator3, firstname3, surname3, staffID3, emailAd3, category3, descript3, priority3, status3, ticketresp3
    global TK4, ticketcreator4, firstname4, surname4, staffID4, emailAd4, category4, descript4, priority4, status4, ticketresp4
    global TK5, ticketcreator5, firstname5, surname5, staffID5, emailAd5, category5, descript5, priority5, status5, ticketresp5

    ticketresp = "Not Yet Provided"
    status = "Open"
    ticketcreator = input("Ticket creator's name ")
    firstname = input("Please enter the client's first name ")
    surname = input("Please enter the client's surname ")
    emailAd = input("please enter the client's email address ")
    print("Identify a category that pertains to the enquiry\n")
    print("1. Software")
    print("2. Hardware")
    print("3. Network")
    print("4. Virus Infection")
    print("5. Other")
    staffID = "void"
    x = defcategory(input("\nPlease select "))

    while x == 0:
        x = defcategory(input("Please select a valid number "))

    category = x

    descript = input("\nPlease enter a description of the issue: ")

    substring = 0

    number2 = random.randint(1000, 9999)
    number2 = str(number2)

    if len(firstname) > 0 and len(surname) > 0:
        staffID = firstname[0] + surname[0] + number2

    if len(ticketcreator) > 2 and len(firstname) > 0  and len(surname) > 0:


        password = firstname[0] + surname[0] + ticketcreator[0:3]

        descriptV = str.lower(descript)

        index = descriptV.find("password")

        if index != -1:
           substring = 1

        index2 = descriptV.find("chang")

        if index2 != -1:
           substring = substring + 1

        if substring == 2:

                ticketresp = "Your new password is: ", password
                status = "Closed"
                statOv = statOv - 1
                statCv = statCv + 1


    print("Please choose a priority level for the ticket: \n")

    print("1. High")
    print("2. Medium")
    print("3. Low")

    y = defpriority(input("\nPlease select "))

    while y == 0:
        y = defpriority(input("Please select a valid number "))
    priority = y

    TK = TK + 1
    print("\nTicket Number", TK, "is now open and appears as follows\n")
    print("---------------------------------------------------")
    print("Ticket Number: ",TK)
    print("Ticket Creator: ", ticketcreator)
    print("Client's Name: ", firstname, surname)
    print("Client's Staff ID No: ", staffID)
    print("Client's Email Address: ", emailAd)
    print("Ticket Category: ", category)
    print("Description of the issue: ", descript)
    print("Ticket Priority: ", priority)
    print("Ticket Status: ", status)
    print("Ticket Response: ", ticketresp)
    print("---------------------------------------------------\n")
    statOv = statOv + 1
    if count == 1:
        (TK1, ticketcreator1, firstname1,surname1,staffID1,emailAd1,category1,descript1,priority1,status1, ticketresp1) = (TK, ticketcreator, firstname,surname,staffID,emailAd,category,descript,priority,status, ticketresp)
    if count == 2:
        (TK2, ticketcreator2, firstname2,surname2,staffID2,emailAd2,category2,descript2,priority2,status2, ticketresp2) = (TK, ticketcreator, firstname,surname,staffID,emailAd,category,descript,priority,status, ticketresp)
    if count == 3:
        (TK3, ticketcreator3, firstname3,surname3,staffID3,emailAd3,category3,descript3,priority3,status3, ticketresp3) = (TK, ticketcreator, firstname,surname,staffID,emailAd,category,descript,priority,status, ticketresp)
    if count == 4:
        (TK4, ticketcreator4, firstname4, surname4, staffID4, emailAd4, category4, descript4, priority4, status4, ticketresp4) = (TK, ticketcreator, firstname, surname, staffID, emailAd, category, descript, priority, status, ticketresp)
    if count == 5:
        (TK5, ticketcreator5, firstname5, surname5, staffID5, emailAd5, category5, descript5, priority5, status5, ticketresp5) = (TK, ticketcreator, firstname, surname, staffID, emailAd, category, descript, priority, status, ticketresp)

    input("Press Enter to return to the main menu")
    print("\n-------------------------------------------------------")

    MainMenu()

TicketForm()

""" This code shows a list of all active tickets then displays the selected ticket. The priority and status of the ticket can then be changed"""

def ViewTicket():
    global tkv, tc, a, b, c, d, e, f, g, h, trp
    global count
    global Update
    global StValue
    global statOv
    global statCv
    global status
    StValue = status
    global TK1, ticketcreator1, firstname1, surname1, staffID1, emailAd1, category1, descript1, priority1, status1, ticketresp1
    global TK2, ticketcreator2, firstname2, surname2, staffID2, emailAd2, category2, descript2, priority2, status2, ticketresp2
    global TK3, ticketcreator3, firstname3, surname3, staffID3, emailAd3, category3, descript3, priority3, status3, ticketresp3
    global TK4, ticketcreator4, firstname4, surname4, staffID4, emailAd4, category4, descript4, priority4, status4, ticketresp4
    global TK5, ticketcreator5, firstname5, surname5, staffID5, emailAd5, category5, descript5, priority5, status5, ticketresp5
    print("----------------------------------------------------------")
    if count > 1:
        print("\n1. Ticket Number:",TK1, firstname1, surname1)
    if count > 2:
        print("\n2. Ticket Number:",TK2, firstname2, surname2)
    if count > 3:
        print("\n3. Ticket Number:",TK3, firstname3, surname3)
    if count > 4:
        print("\n4. Ticket Number:",TK4, firstname4, surname4)
    if count > 5:
        print("\n5. Ticket Number:",TK5, firstname5, surname5)
    print("\n--------------------------------------------------------")
    print("\n0. Return to Main Menu")
    j = ticketchoice(input("\nWhich ticket would you like to view. Please select an item "))
    if j == 100:
        count = count - 1
        print("------------------------------------------------------")
        MainMenu()
    while j == 0:
        j = ticketchoice(input("Please select a valid number "))

    if j == 1:
        (tkv, tc, a, b, c, d, e, f, g, h, trp) = (TK1, ticketcreator1, firstname1, surname1, staffID1, emailAd1, category1, descript1, priority1, status1, ticketresp1)

    if j == 2:
        (tkv, tc, a, b, c, d, e, f, g, h, trp) = (TK2, ticketcreator2, firstname2, surname2, staffID2, emailAd2, category2, descript2, priority2, status2, ticketresp2)

    if j == 3:
        (tkv, tc, a, b, c, d, e, f, g, h, trp) = (TK3, ticketcreator3, firstname3, surname3, staffID3, emailAd3, category3, descript3, priority3, status3, ticketresp3)

    if j == 4:
        (tkv, tc, a, b, c, d, e, f, g, h, trp) = (TK4, ticketcreator4, firstname4, surname4, staffID4, emailAd4, category4, descript4, priority4, status4, ticketresp4)

    if j == 5:
        (tkv, tc, a, b, c, d, e, f, g, h, trp) = (TK5, ticketcreator5, firstname5, surname5, staffID5, emailAd5, category5, descript5, priority5, status5, ticketresp5)

    print("\n---------------------------------------------------------")
    print("Ticket Number: ", tkv)
    print("Ticket Creator: ", tc)
    print("Client's Name: ", a, b)
    print("Client's Staff ID No: ", c)
    print("Client's Email Address: ", d)
    print("Ticket Category: ", e)
    print("Description of the issue: ", f)
    print("Ticket Priority: ", g)
    print("Ticket Status: ", h)
    print("Ticket Response: ", trp)
    print("---------------------------------------------------------\n")
    print("What action would you like to take?\n")
    print("1. Change ticket priority")
    print("2. Change ticket status")
    print("3. Update ticket response")
    print("4. View more tickets")
    print("5. Return to main menu")
    w = endchoice(input("\nPlease select an option "))
    while w == 0:
        w = endchoice(input("Please select a valid number "))
    if w == 4:
        ViewTicket()
    if w == 5:
            print("-------------------------------------------------------")
            count = count - 1
            MainMenu()

    if w == 1:
        print("\nThis ticket has a", g, "priority. What would you like to change it to?\n")
        if g == "HIGH":
             print("1. MEDIUM")
             print("2. LOW")
        if g == "MEDIUM":
            print("1. HIGH")
            print("2. LOW")
        if g == "LOW":
            print("1. HIGH")
            print("2 MEDIUM")
        u = updatepriority(input("\nPlease select an option "))
        while u == 0:
              u = updatepriority(input("Please select a valid number "))

        if g == "HIGH" and u == 1:
                PrValue = "MEDIUM"
        if g == "MEDIUM" and u == 1:
                PrValue = "HIGH"
        if g == "LOW" and u == 1:
                PrValue = "HIGH"
        if g == "HIGH" and u == 2:
                PrValue = "LOW"
        if g == "MEDIUM" and u == 2:
                PrValue = "LOW"
        if g == "LOW" and u == 2:
                PrValue = "MEDIUM"

        if j == 1 and (u == 1 or u == 2):
                priority1 = PrValue
                g = PrValue
        if j == 2 and (u == 1 or u == 2):
                priority2 = PrValue
                g = PrValue
        if j == 3 and (u == 1 or u == 2):
                priority3 = PrValue
                g = PrValue
        if j == 4 and (u == 1 or u == 2):
                priority4 = PrValue
                g = PrValue
        if j == 5 and (u == 1 or u == 2):
                priority5 = PrValue
                g = PrValue
        StValue = h
        Update = 1
        ViewUpdate()

    if w == 2 and h == "Open":
        print("\nThis ticket's status is open. Has the ticket been resolved?\n")
        print("1. Yes the ticket has been resolved, close the ticket")
        print("2. Return to ticket folder")

        z = defstatus(input("\nPlease select "))
        while z == 0:
            z = defstatus(input("Please select a valid number \n"))
        if z == 2:
            ViewTicket()
        if h == "Open" and z == 1:
            statOv = statOv - 1
            statCv = statCv + 1
            StValue = "Closed"
        if j == 1 and z == 1:
            status1 = StValue
        if j == 2 and z == 1:
            status2 = StValue
        if j == 3 and z == 1:
            status3 = StValue
        if j == 4 and z == 1:
            status4 = StValue
        if j == 5 and z == 1:
            status5 = StValue
        Update = 2
        ViewUpdate()

    if w == 2 and h == "Closed":
        print("\nThis ticket's status if closed, would you like to reopen the ticket?\n")
        print("1. Reopen ticket")
        print("2. Return to ticket folder")

        x = defstatus2(input("\nPlease select "))
        while x == 0:
          x = defstatus2(input("Please select a valid number \n"))
        if x == 2:
            ViewTicket()
        if h == "Closed" and x == 1:
            statOv = statOv + 1
            statCv = statCv - 1
            StValue = "Open"
        if j == 1 and x == 1:
            status1 = StValue
        if j == 2 and x == 1:
            status2 = StValue
        if j == 3 and x == 1:
            status3 = StValue
        if j == 4 and x == 1:
            status4 = StValue
        if j == 5 and x == 1:
            status5 = StValue
        Update = 3
        ViewUpdate()

    if w == 3:
        StValue = h
        trp = input("Add a response: ")
        if j == 1:
            ticketresp1 = trp
        if j == 2:
            ticketresp2 = trp
        if j == 3:
            ticketresp3 = trp
        if j == 4:
            ticketresp4 = trp
        if j == 5:
            ticketresp5 = trp
        Update = 4
        ViewUpdate()
ViewTicket()

""" this code generates a ticket update when the priority or status or response is changed """

def ViewUpdate():
    global tkv, tc, a, b, c, d, e, f, g, Update, StValue, trp
    print("\nTicket Update")
    print("---------------------------------------------------------")
    print("Ticket Number: ", tkv)
    print("Ticket Creator: ", tc)
    print("Client's Name: ", a, b)
    print("Client's Staff ID No: ", c)
    print("Client's Email Address: ", d)
    print("Ticket Category: ", e)
    print("Description of the issue: ", f)
    print("Ticket Priority: ", g)
    print("Ticket Status: ", StValue)
    print("Ticket Response: ", trp)
    print("---------------------------------------------------------\n")
    if Update == 1:
        print("This ticket's priority level has been updated\n")
    if Update == 2:
        print("This ticket has been closed\n")
    if Update == 3:
        print("This ticket has been reopened\n")
    if Update == 4:
        print("Ticket response has been updated\n")
    Update = 0
    ViewTicket()

ViewUpdate()


