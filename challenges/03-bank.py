# print("Welcome to Chase bank.")
# print("Have a nice day!")

balance = 100
deposit = 1000

# def transaction(direction, num):
#     if direction == 'deposit':
#         deposit_amount = input('How much?')
#         balance += int(deposit_amount)
#         print(balance)
#     elif direction == 'withdraw':
#         withdraw_amount = input('How much?')
#         balance -= int(withdraw_amount)
#         print(balance)
#     else:
#         print(balance)
    

print(balance)
direction = input('What would you like to do? (deposit, withdraw, check_balance)\n')
if direction == 'deposit':
    deposit_amount = input('How much?')
    balance += int(deposit_amount)
    print(balance)
elif direction == 'withdraw':
    withdraw_amount = input('How much?')
    balance -= int(withdraw_amount)
    print(balance)
else:
    print('your balance is', balance)
# print('Your current balance is')
# transaction(direction)