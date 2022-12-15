number_text = input("Please enter some number: ")
number = float(number_text)

if number < 0:
    #if number is negative
    #then save number as negative
    answer = -number
else:
    answer = number
    
print("Number's numeric value is: " + str(answer))
input()