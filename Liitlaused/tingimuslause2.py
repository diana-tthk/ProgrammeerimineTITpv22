number = int(input("Please enter some number: "))

if number != 0:
    print ("Number is not 0")
else:
    print("Number is 0")

if number >= 0 and number <= 9:
    print("This is a one-digit number")
elif number > 9 and number < 100:
    print("This is a two-digit number")
elif number >= 100 and number <= 999:
    print("This is a three-digit number")
else:
    print("This is a multidigit number")

input()