
class Ticket:
    # assigning global variables
    tickets = []
    counter = 2000
    var = 0
    switch = 0
    statusO = 0
    statusC = 0

    # __inti__ package created for class Ticket
    def __init__(self, counter, ticketcreator, staffID, emailAd, descript, status, response):
        self.counter = counter
        self.ticketcreator = ticketcreator
        self.staffID = staffID
        self.emailAd = emailAd
        self.descript = descript
        self.status = status
        self.response = response

    # this function prints the inputted values depending on their position in the ticket list
    def Printticket(self):

        print("\n---------------------------------------------------")
        print("Ticket Number: ", self.counter)
        print("Ticket Creator: ", self.ticketcreator)
        print("Client's Staff ID No: ", self.staffID)
        print("Client's Email Address: ", self.emailAd)
        print("Description of the issue: ", self.descript)
        print("Response to ticket:", self.response)
        print("Ticket status: ", self.status)
        print("---------------------------------------------------\n")

    # this function displays the statistics for the tickets created
    @staticmethod
    def TicketStats():
        print("\nNumber of tickets submitted: ", Ticket.counter - 2000)
        print("Number of tickets resolved: ", Ticket.statusC)
        print("Number of open tickets: ", Ticket.statusO)

    # this function enables a response to be updated and closes the ticket afterwards
    def respond(self):

        self.response = input("Add a response: ")
        self.status = "Closed"

        Ticket.statusO = Ticket.statusO - 1
        Ticket.statusC = Ticket.statusC + 1

    # this function informs the user that the ticket is already open
    # or updates the ticket status to open if the ticket was closed
    def reopen(self):

        if self.status == "Open":
            print("\nThis ticket is already open")


        if self.status == "Closed":
            Ticket.statusO = Ticket.statusO + 1
            Ticket.statusC = Ticket.statusC - 1
            print("\nThis ticket has been reopened")
            self.status = "Open"


    # this function enables the user to input all fields.
    # status and response are automatically assigned
    # this function also detects a password change in the description and creates a new one
    @staticmethod
    def TicketInput():

        Ticket.statusO = Ticket.statusO + 1
        Ticket.counter = Ticket.counter + 1
        ticketcreator = input("\nTicket creator's name: ")
        staffID = input("Please enter staff ID: ")
        emailAd = input("Please enter your email: ")
        descript = input("Please enter your description: ")
        status = "Open"
        Ticket.switch = 1
        response = "Not Yet Available"
        print("\nTicket Number", Ticket.counter, "is now open and appears as follows")
        substring = 0
        if len(ticketcreator) > 2 and len(staffID) > 1:
            password = staffID[0:2] + ticketcreator[0:3]

            descriptV = str.lower(descript)

            index = descriptV.find("password")

            if index != -1:
               substring = 1

            index2 = descriptV.find("chang")

            if index2 != -1:
               substring = substring + 1

            if substring == 2:
               response = "Your new password is: ", password
               status = "Closed"
               Ticket.switch = 0
               Ticket.statusO = Ticket.statusO - 1
               Ticket.statusC = Ticket.statusC + 1
        ticket = Ticket(Ticket.counter, ticketcreator, staffID, emailAd, descript, status, response)
        Ticket.tickets.append(ticket)
        ticket.Printticket()

#this function ensures only valid numbers are executed avoiding errors
def menuchoice(v):
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
    if v == "6":
        slc = 6
    if v != "1" and v != "2" and v != "3" and v != "4" and v != "5" and v != "6":
        slc = 0

    return slc

# this is the main class which displays the options for the program and processes the option inputted
class Main():

    x = True
    while x:
        print("\n1. Create a ticket: ")
        print("2. View tickets")
        print("3. Respond to ticket")
        print("4. Reopen a ticket: ")
        print("5. View statistics")
        print("6. Exit Program")

        j = menuchoice(input("\nPlease select an item: "))
        while j == 0:
            j = menuchoice(input("Please select a valid number: "))

        if j == 1:
            Ticket.TicketInput()

        if j == 2 and Ticket.counter > 2000:

            for ticket in Ticket.tickets:
                ticket.Printticket()
        if j == 2 and Ticket.counter == 2000:
                print("\nThere are no active tickets to view")

        if j == 3 and Ticket.counter == 2000:
            print("\nThere are no active tickets to respond to")

        if j == 3 and Ticket.counter > 2000:
            for ticket in Ticket.tickets:
                print(ticket.counter)
            while True:
                number = input("\nEnter a ticket number to add a response: \n")
                if number.isdigit():
                    number = int(number)
                else:
                    print("\nTicket number has to be numeric")
                    continue

                ticketToRespond = None
                for ticket in Ticket.tickets:
                    if ticket.counter == number:
                       ticketToRespond = ticket
                       break

                if ticketToRespond == None:
                    print("\nTicket not found with this ID")
                    continue
                else:
                    break

            if ticketToRespond.status == "Closed":
                print("\nThis ticket is currently closed")
                continue

            ticketToRespond.Printticket()
            ticketToRespond.respond()
            print("\nThis ticket's response has been updated")
            ticketToRespond.Printticket()

        if j == 4 and Ticket.counter == 2000:
            print("\nThere are no active tickets to reopen")

        if j == 4 and Ticket.counter > 2000:
            for ticket in Ticket.tickets:
                print(ticket.counter)

            number = int(input("\nEnter a ticket number to reopen the ticket: "))
            ticketToRespond = None
            for ticket in Ticket.tickets:
                if ticket.counter == number:
                    ticketToRespond = ticket
                    break
            if ticketToRespond != None:
                ticketToRespond.Printticket()
                ticketToRespond.reopen()
            if Ticket.var == 0:
                ticketToRespond.Printticket()

        if j == 5:
            Ticket.TicketStats()

        if j == 6:
            exit()


