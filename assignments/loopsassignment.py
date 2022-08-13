i = int(input("Enter a number: "))
x = 0
while x < i:
    x += 1
    if x % 10 == 0:
        continue
    elif x >= 100:
        break
    print(x)