# Read User Input

number1 = int(input())
number2 = int(input())
operator = input()

if operator == "+" or operator == "-" or operator == "*":
    result = 0
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2

    if result % 2 == 0:
        type_number = "even"
    else:
        type_number = "odd"
    print(f"{number1} {operator} {number2} = {result} - {type_number}")

if operator == "/" and number2 != 0:
    result = number1 / number2
    print(f"{number1} / {number2} = {result:.2f}")

elif operator == "%" and number2 != 0:
    result = number1 % number2
    print(f"{number1} % {number2} = {result}")

elif operator == "/" or operator == "%" and number2 == 0:
    print(f"Cannot divide {number1} by zero")