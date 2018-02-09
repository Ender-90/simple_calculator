# Hey, it's my first project in Python
# It's just a simple calculator that adds, subtracts and multiplicates two numbers.
# Enjoy! =)

from sys import exit

name = input("Please enter your name: ")
print("Hello {0}, nice to see you here!".format(name))

first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

operation = int(input("""Choose an operation:
1 <- add numbers
2 <- substract second number from first
3 <- substract first number from second
4 <- multiplicate numbers"""))

if operation == 1:
    result = first_number + second_number
elif operation == 2:
    result = first_number - second_number
elif operation == 3:
    result = second_number - first_number
elif operation == 4:
    result = first_number * second_number
else:
    print("I don't recognise the operation!")
    exit()

print("Result of the operation is {}".format(result))

exit()