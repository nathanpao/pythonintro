x=int(input("Enter minimum number: "))
y=int(input("Enter maxmimum number: "))
i=x
if i % 2 == 0: i=x+1
while i<=y:
    print(i)
    i+=2