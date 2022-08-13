n = int(input("Enter any number: "))
i = 2
primeFlag = 0
while i <= n:
    if n %i == 0:
        primeFlag += 1;
    i += 1
if primeFlag == 1:
    print("Prime number")
else:
    print("Not a prime number")