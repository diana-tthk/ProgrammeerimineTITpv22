import fbmi

#check if input is numeric and make it a number
def check_input_float(input):
    try:
        float(input)
        return True
    except:
        return False

    #When needed to check if integer
    #if input.isnumeric():
    #    return True
    #else:
    #    print("Palun sisesta number!")

while True:
    height = input("Sisesta kliendi pikkus (meetrides): ")
    if not check_input_float(height):
        continue
    else:
        height = float(height)
        break

while True:    
    weight = input("Sisesta kliendi kaal: ")
    if not check_input_float(weight):
        continue
    else:
        weight = float(weight)
        break

bmi = fbmi.bmi(height, weight)

if bmi < 18:
    print("Klient on alakaaluline")
elif bmi > 18 and bmi < 25:
    print("Kliendi kaal on normis")
else:
    print("Klient on ülekaaluline")

input()