import sys
accBalance = sys.argv
#Inputted parameter is 10000

a = int(input("Enter transaction method: "))


if a == 1:
    print("Your balance is $", int(accBalance[1]))
elif a == 2:
    withdraw = int(input("Enter withdrawal amount: "))
    accBalance = int(accBalance[1]) - withdraw
    print("Your balance is $", accBalance)
elif a == 3:
    deposit = int(input("Enter cash deposit amount: "))
    accBalance = int(accBalance[1]) + deposit
    print("Your balance is $", accBalance)
elif a == 4:
    deposit = int(input("Enter check deposit amount: "))
    accBalance = int(accBalance[1]) + deposit
    print("Your balance is $", accBalance)
else:
    print("This transaction method is invalid.")