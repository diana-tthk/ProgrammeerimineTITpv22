i = 1
count = 0

while i <= 10:
    print("The number we examine is: ", i)
    if i % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

    square = i * i
    if square % 2 == 0:
        print("It's square ", square, " is even number")
    else:
        print("It's square ", square, " is odd number")

    if square % 3 == 0:
        count += 1
    print("---------------------------")
    # i = i + 1
    i += 1

print("Squares that can be divided by 3: ", count)
input()