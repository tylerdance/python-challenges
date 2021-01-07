# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

operator = input('What calculation would you like to do? (add, sub, multiply, div)')
num1 = input('What is number 1?')
num2 = input('What is number 2?')

print(operator)
print(num1)
print(num2)

def calculate(operator, num1, num2):
    if operator == 'add':
        print(num1 + num2)
    elif operator == 'subtract':
        print(num1 - num2)
    elif operator == 'multiply':
        print(num1 * num2)
    elif operator == 'divide':
        print(num1 / num2)
    else:
        print('select an operator though')
calculate(operator, int(num1), int(num2))


