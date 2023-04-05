
import random
descript = "password change"
firstname = "Sarah"
surname = "Cooper"
ticketcreator = "DAVid"

number = random.randint(1000,9999)

number = str(number)

descriptV = str.lower(descript)
index = descriptV.find("password")

if index != -1:
    substring = 1

index2 = descriptV.find("change")

if index2 != -1:
    substring = substring + 1

if substring == 2:

    password = firstname[0] + surname [0] + ticketcreator[0 , 1 , 2] + number
    print("Your request for a change of password has been detected\nYour new password is: ", password)