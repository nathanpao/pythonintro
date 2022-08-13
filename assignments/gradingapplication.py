print("Enter your grades for the following exams: ")
m1 = int(input("Maths: "))
m2 = int(input("Physics: "))
m3 = int(input("Chemistry: "))
avg = (m1+m2+m3)/3
if m1 < 35 or m2 < 35 or m3 < 35:
    print("Sorry, you did not pass your exam.")
elif avg <= 59:
    print("You got a C.")
elif avg <= 69:
    print("You got a B.")
else:
    print("You got an A.")