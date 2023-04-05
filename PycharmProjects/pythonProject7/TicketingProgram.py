class Ticket:

    def __init__(self, firstname, surname, staffID, emailAd, category, descript, priority, status):

        self.firstname = firstname
        self.surname = surname
        self.staffID = staffID
        self.emailAd = emailAd
        self.category = category
        self.descript = descript
        self.priority = priority
        self.status = status

    def printTicket(self):





def category(v):
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


def priority(v):
    if v == "1":
        slc = "HIGH"
    if v == "2":
        slc = "MEDIUM"
    if v == "3":
        slc = "LOW"
    if v != "1" and v != "2" and v != "3":
        slc = 0

    return slc

def status(v):
    if v == "1":
        slc = "Open"
    if v == "2":
        slc = "Closed"
    if v == "3":
        slc = "Reopened"
    if v != "1" and v != "2" and v != "3":
        slc = 0

    return slc
input("Press enter to create a ticket")

firstname = input("Please enter your first name ")
surname = input("Please enter your surname ")
staffID = input("Please enter your staff ID ")
emailAd = input("please enter you email address ")
print("Identify a category that pertains to your enquiry")
print("1. Software")
print("2. Hardware")
print("3. Network")
print("4. Virus Infection")
print("5. Other")

x = category(input("Please select "))

while x == 0:
    x = category(input("Please select a valid number "))

descript = input("Please enter a description of the issue: ")

print("Please choose a priority level for the ticket: ")

print("1. High")
print("2. Medium")
print("3. Low")

y = priority(input("Please select "))
while y == 0:
    y = priority(input("Please select a valid number "))

print("Please choose the ticket status")

print("1. Open")
print("2. Closed")
print("3. Reopened")

z = status(input("please select "))

while z == 0:
    z = status(input("Please select a valid number "))

Ticket.__init__()

#print("Thank you", firstname, "your ticket appears as follows\n")
#print("Your Name: ", firstname, surname)
#print("Your Staff ID No: ", staffID)
#print("Your email address: ", emailAd)
#print("Your ticket category is: ", x)
#print("Description of issue: ", descript)
#print("Ticket Priority: ", y)
#print("Ticket Status: ", z)
