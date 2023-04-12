

TK = 2000


def TicketInput(self):
    global TK
    TK = TK + 1
    self.TK = TK
    self.ticketcreator = input("Ticket creator's name ")
    self.firstname = input("Please enter the client's first name ")
    self.surname = input("Please enter the client's surname ")
    self.staffID = "AB1234"
    self.emailAd = input("Please enter your email ")
    self.category = input("Please enter your category ")
    self.descript = input("Please enter your description ")
    self.priority = input("Enter the priority ")
    self.status = input("What is the status ")
    self.ticketresp = "Not Yey Available"

    self.ticket1 = [self.TK, self.ticketcreator, self.firstname, self.surname, self.staffID, self.emailAd,
                    self.category, self.descript, self.priority, self.status, self.ticketresp]


TicketInput()


def TicketPrint(self):
    print("\n\nYour ticket number is: ", self.ticket1[0])
    print("Ticket creator's name: ", self.ticket1[1])
    print("Your firstname: ", self.ticket1[2])
    print("Your surname: ", self.ticket1[3])
    print("Your StaffID: ", self.ticket1[4])
    print("Your email address is: ", self.ticket1[5])
    print("Ticket category is: ", self.ticket1[6])
    print("Ticket description is: ", self.ticket1[7])
    print("Ticket priority is: ", self.ticket1[8])
    print("Ticket status is: ", self.ticket1[9])
    print("Ticket response is: ", self.ticket1[10])


TicketPrint()