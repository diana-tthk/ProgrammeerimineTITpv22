from random import randint
count = 0
#generate random number
number = randint(1, 999)
guess = int(input("Guess my number from 1 to 999"))
count += 1
while guess != number:
    if guess > number:
        print("My number is smaller")
    else:
        print("My number is bigger")

    guess = int(input("Guess my number from 1 to 999"))
    count += 1

print("You have guessed! Well done!")
print("You have used ", count, " attempts")
input()