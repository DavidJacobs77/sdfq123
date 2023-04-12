import random

class Ticket:
     TicketFields = []

     def __init__(self, TK, ticketcreator, firstname, surname, staffID, emailAd, category, descript, priority, status, ticketresp):
        self.TK = TK
        self.ticketcreator = ticketcreator
        self.firstname = firstname
        self.surname = surname
        self.staffID = staffID
        self.emailed = emailAd
        self.category = category
        self.descript = descript
        self.priority = priority
        self.status = status
        self.ticketresp = ticketresp
        Ticket.TicketFields.append(self)


print("Welcome to the Help Desk Ticketing System Prototype.")
count = 0
TK = 2000
Update = 0
StValue = 0
statOv = 0
statCv = 0
status = 0
(tkv, tc, a, b, c, d, e, f, g, h, trp) = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

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

def MainMenu(self):
    global count
    global statOv
    global statCv
    count = count + 1

    print("\nWhat would you like to do?\n")
    print("1. Create a new ticket")
    print("2. View tickets")

    print("\nThe number of tickets submitted: ", TK - 2000)
    print("The number of tickets open for response: ", statOv)
    print("The number of tickets resolved: ", statCv)

    j = menuchoice(input("\nPlease select an item "))
    while j == 0:
        j = menuchoice(input("Please select a valid number "))
    if j == 1 and count >= 6:
        print("\n-------------------------------------------------------")
        print("\nThis action cannot be completed as the ticket folder is full")
        MainMenu(Ticket)
    if j == 1 and count <= 5:
        print("New Ticket", count)
        TicketForm()
    if j == 2 and count == 1:
        print("\n-------------------------------------------------------")
        print("\nThere are no tickets in the folder to view")
        count = count - 1
        MainMenu(Ticket)
    if j == 2 and count > 1:
        print("Prompt view tickets\n")
        ViewTicket(Ticket)


MainMenu(Ticket)

"""" This code is the input function of all the ticket's fields. It then displays the ticket with the inputed strings or values"""

def TicketForm(self):
    global count
    global TK
    global statOv
    global statCv
    TK = TK + 1
    self.TK = TK
    self.ticketresp = "Not Yet Provided"
    self.status = "Open"
    self.ticketcreator = input("Ticket creator's name ")
    self.firstname = input("Please enter the client's first name ")
    self.surname = input("Please enter the client's surname ")
    self.emailAd = input("please enter the client's email address ")
    print("Identify a category that pertains to the enquiry\n")
    print("1. Software")
    print("2. Hardware")
    print("3. Network")
    print("4. Virus Infection")
    print("5. Other")
    self.staffID = "void"
    x = defcategory(input("\nPlease select "))

    while x == 0:
        x = defcategory(input("Please select a valid number "))

    self.category = x

    self.descript = input("\nPlease enter a description of the issue: ")

    substring = 0

    number2 = random.randint(1000, 9999)
    number2 = str(number2)

    if len(self.firstname) > 0 and len(self.surname) > 0:
        self.staffID = self.firstname[0] + self.surname[0] + number2

    if len(self.ticketcreator) > 2 and len(self.firstname) > 0 and len(self.surname) > 0:


        password = self.firstname[0] + self.surname[0] + self.ticketcreator[0:3]

        descriptV = str.lower(self.descript)

        index = descriptV.find("password")

        if index != -1:
           substring = 1

        index2 = descriptV.find("chang")

        if index2 != -1:
           substring = substring + 1

        if substring == 2:

                self.ticketresp = "Your new password is: ", password
                Ticket.status = "Closed"
                statOv = statOv - 1
                statCv = statCv + 1

    print("Please choose a priority level for the ticket: \n")

    print("1. High")
    print("2. Medium")
    print("3. Low")

    y = defpriority(input("\nPlease select "))

    while y == 0:
        y = defpriority(input("Please select a valid number "))
    self.priority = y

    if TK == 2001:
        self.ticket1 = [self.TK, self.ticketcreator, self.firstname, self.surname, self.staffID, self.emailAd, self.category, self.descript, self.priority, self.status, self.ticketresp]
    if TK == 2002:
        self.ticket2 = [self.TK, self.ticketcreator, self.firstname, self.surname, self.staffID, self.emailAd, self.category, self.descript, self.priority, self.status, self.ticketresp]
    if TK == 2003:
        self.ticket3 = [self.TK, self.ticketcreator, self.firstname, self.surname, self.staffID, self.emailAd, self.category, self.descript, self.priority, self.status, self.ticketresp]
    if TK == 2004:
        self.ticket4 = [self.TK, self.ticketcreator, self.firstname, self.surname, self.staffID, self.emailAd, self.category, self.descript, self.priority, self.status, self.ticketresp]
    if TK == 2005:
        self.ticket5 = [self.TK, self.ticketcreator, self.firstname, self.surname, self.staffID, self.emailAd, self.category, self.descript, self.priority, self.status, self.ticketresp]

    print("\nTicket Number", self.TK, "is now open and appears as follows\n")
    print("---------------------------------------------------")
    print("Ticket Number: ", self.TK)
    print("Ticket Creator: ", self.ticketcreator)
    print("Client's Name: ", self.firstname, self.surname)
    print("Client's Staff ID No: ", self.staffID)
    print("Client's Email Address: ", self.emailAd)
    print("Ticket Category: ", self.category)
    print("Description of the issue: ", self.descript)
    print("Ticket Priority: ", self.priority)
    print("Ticket Status: ", self.status)
    print("Ticket Response: ", self.ticketresp)
    print("---------------------------------------------------\n")
    statOv = statOv + 1
    input("\nPress Enter to return to the main menu")
    print("-------------------------------------------------------")

    MainMenu(Ticket)

TicketForm(Ticket)

""" This code shows a list of all active tickets then displays the selected ticket. The priority and status of the ticket can then be changed"""

def ViewTicket(self):
    global tkv, tc, a, b, c, d, e, f, g, h, trp
    global count
    global Update
    global StValue
    global statOv
    global statCv
    StValue = status

    print("---------------------------------------------------------")
    if count > 1:
        print("\n1. Ticket Number:", self.ticket1[0], self.ticket1[2], self.ticket1[3])
    if count > 2:
        print("\n2. Ticket Number:", self.ticket2[0], self.ticket2[2], self.ticket2[3])
    if count > 3:
        print("\n3. Ticket Number:", self.ticket3[0], self.ticket3[2], self.ticket3[3])
    if count > 4:
        print("\n4. Ticket Number:", self.ticket4[0], self.ticket4[2], self.ticket4[3])
    if count > 5:
        print("\n5. Ticket Number:", self.ticket5[0], self.ticket5[2], self.ticket5[3])
    print ("\n--------------------------------------------------------")
    print("\n0. Return to Main Menu")
    j = ticketchoice(input("\nWhich ticket would you like to view. Please select an item "))
    if j == 100:
        count = count - 1
        print("-------------------------------------------------------")
        MainMenu(Ticket)
    while j == 0:
        j = ticketchoice(input("Please select a valid number "))
    if j == 1:
        tkv, tc, a, b, c, d, e, f, g, h, trp = self.ticket1[0:11]
    if j == 2:
        tkv, tc, a, b, c, d, e, f, g, h, trp = self.ticket2[0:11]
    if j == 3:
        tkv, tc, a, b, c, d, e, f, g, h, trp = self.ticket3[0:11]
    if j == 4:
        tkv, tc, a, b, c, d, e, f, g, h, trp = self.ticket4[:11]
    if j == 5:
        tkv, tc, a, b, c, d, e, f, g, h, trp = self.ticket5[0:11]

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
        ViewTicket(Ticket)
    if w == 5:
            print("-------------------------------------------------------")
            count = count - 1
            MainMenu(Ticket)

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
                self.ticket1[8] = PrValue
                g = PrValue
        if j == 2 and (u == 1 or u == 2):
                self.ticket2[8] = PrValue
                g = PrValue
        if j == 3 and (u == 1 or u == 2):
                self.ticket3[0] = PrValue
                g = PrValue
        if j == 4 and (u == 1 or u == 2):
                self.ticket[8] = PrValue
                g = PrValue
        if j == 5 and (u == 1 or u == 2):
                self.ticket[8] = PrValue
                g = PrValue
        StValue = h
        Update = 1
        ViewUpdate(Ticket)

    if w == 2 and h == "Open":
        print("\nThis ticket's status is open. Has the ticket been resolved?\n")
        print("1. Yes the ticket has been resolved, close the ticket")
        print("2. Return to ticket folder")

        z = defstatus(input("\nPlease select "))
        while z == 0:
            z = defstatus(input("Please select a valid number \n"))
        if z == 2:
            ViewTicket(Ticket)
        if h == "Open" and z == 1:
            statOv = statOv - 1
            statCv = statCv + 1
            StValue = "Closed"
        if j == 1 and z == 1:
            self.ticket1[9] = StValue
        if j == 2 and z == 1:
            self.ticket2[9] = StValue
        if j == 3 and z == 1:
            self.ticket3[9] = StValue
        if j == 4 and z == 1:
            self.ticket4[9] = StValue
        if j == 5 and z == 1:
            self.ticket5[9] = StValue
        Update = 2
        ViewUpdate(Ticket)

    if w == 2 and h == "Closed":
        print("\nThis ticket's status if closed, would you like to reopen the ticket?\n")
        print("1. Reopen ticket")
        print("2. Return to ticket folder")

        x = defstatus2(input("\nPlease select "))
        while x == 0:
          x = defstatus2(input("Please select a valid number \n"))
        if x == 2:
            ViewTicket(Ticket)
        if h == "Closed" and x == 1:
            statOv = statOv + 1
            statCv = statCv - 1
            StValue = "Open"
        if j == 1 and x == 1:
            self.ticket1[9] = StValue
        if j == 2 and x == 1:
            self.ticket2[9] = StValue
        if j == 3 and x == 1:
            self.ticket3[9] = StValue
        if j == 4 and x == 1:
            self.ticket4[9] = StValue
        if j == 5 and x == 1:
            self.ticket5[9] = StValue
        Update = 3
        ViewUpdate(Ticket)

    if w == 3:
        StValue = h
        trp = input("Add a response: ")
        if j == 1:
            self.ticket1[10] = trp
        if j == 2:
            self.ticket2[10] = trp
        if j == 3:
            self.ticket3[10] = trp
        if j == 4:
            self.ticket4[10] = trp
        if j == 4:
            self.ticket5[10] = trp
        Update = 4
        ViewUpdate(Ticket)
ViewTicket(Ticket)

""" this code generates a ticket update when the priority or status is changed """

def ViewUpdate(self):
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
    ViewTicket(Ticket)

ViewUpdate(Ticket)


