def oddeven(n):

    if int(n) == 0:
        equate = "Even"
    if int(n) == 1:
        equate = "Odd"
    if int(n) == 2:
        equate = "Three"



    return equate

x = oddeven(input("Enter a number: "))

print(x)
myint = int(123)

print(myint)

mystr = ("HelloWorld")
print(mystr)

x = mystr.swapcase()
print(x)