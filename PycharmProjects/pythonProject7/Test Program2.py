class Ticket:
    tickets = []
    counter=2001
    def __init__(self, TK, ticketcreator, firstname, surname, staffID, emailAd, category, descript, priority, status,
                 ticketresp):
        self.TK = TK
        self.ticketcreator = ticketcreator
        self.firstname = firstname
        self.surname = surname
        self.staffID = staffID
        self.emailAd = emailAd
        self.category = category
        self.descript = descript
        self.priority = priority
        self.status = status
        self.ticketresp = ticketresp
        Ticket.tickets.append(self)

    def printtciket(self):
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




class Main():
    def Main():
        
    def printTicketStats():


    def TicketInput(self):
        TK=Ticket.counter
        ticketcreator = input("Ticket creator's name ")
        firstname = input("Please enter the client's first name ")
        surname = input("Please enter the client's surname ")
        staffID = "AB1234"
        emailAd = input("Please enter your email ")
        category = input("Please enter your category ")
        descript = input("Please enter your description ")
        priority = input("Enter the priority ")
        status = input("What is the status ")
        ticketresp = "Not Yey Available"

        ticket1 = Ticket(TK, ticketcreator, firstname, surname, staffID, emailAd, category, descript, priority, status,
                         ticketresp)
        Ticket.counter=Ticket.counter+1
        ticket1.printtciket()




