print("Welcome to MyWay Sandwich. Pick three toppings from the following: \nOnions, Lettuce, Tomato, Olives, Peppers, Tomatoes \nEnter your toppings below.")
s1=input("Topping 1: ")
s2=input("Topping 2: ")
s3=input("Topping 3: ")
s4=int(input("Enter how many sandwiches: "))
print("Your toppings are: {0}, {1}, and {2}.".format(s1, s2, s3))
print("You ordered", s4, "sandwiches.")
print("Total: $",s4*5)