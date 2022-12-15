a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Please enter operation (+,*,/,-) ")

#Выполнить математиеское действие в зависимости от выбранной операции
if operation == "+":
    #print(a, " + ", b, " = ", a + b)
    print(f"{a} + {b} = ", a + b)
elif operation == "-":
    print(f"{a} - {b} = ", a - b)
elif operation == "*":
    print(f"{a} * {b} = ", a * b)
elif operation == "/":
    print(f"{a} / {b} = ", a / b)
#Если ни один из прошлых вариантов не подошел, значит пользователь ввел неверный оператор
else:
    print("Please enter correct operator: +, -, *, /")

input("Press Enter to exit")
