from cmath import sqrt
from math import pow, sqrt

#using pow function from math library
a = pow(2, 89) + pow(5, 70)
print(pow(a, 2))


#without pow function
a = 2 ** 89 + 5 ** 70
print(a ** 2)

#with sqrt function
print(6 + sqrt(sqrt(6 * 5 + 12)))

#working with text values
print("""
   _____
  / ____|
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
""")

print("Hello," + "An" + "na")

#You cannot add text with number
#So this one will not work:
#print("nr." + 1)
#Instead use:
print("nr." + "1")
print("nr." + str(1+3))

#print same text several times
print("Hello! " * 3)

print(len("hello"))

#other use of count function
print("hello".count("l"))

print("Hello".upper())
print(" jfif ".strip() + "text")

#functions can be combined
print("Hello".replace("e", "y").upper())

input()