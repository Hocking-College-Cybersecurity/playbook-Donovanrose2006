symbol=input("Enter math type (+, -, *, /):")
number= float(input("Enter first number: "))
number2= float(input("Enter second number: "))
# User input stops here.
if symbol =='+':
    answer = number + number2
elif symbol == '-':
    answer = number - number2
elif symbol == '*':
    answer = number * number2
elif symbol == '/':
    if number2 == 0:
        answer = 'Error: Division by zero'
    else:
        answer = number / number2
else:
    answer = "Invalid Operator"
print(answer)
