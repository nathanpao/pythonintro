id = 333
firstName = "Blue"
lastName = "     Bear"
ssn = "333-69-1337"
hasInsurance = True
billingAmount = "42069"
print(type(billingAmount))
billingAmount = float(billingAmount)
print(type(billingAmount))

print(id, firstName, lastName.lstrip(), ssn, hasInsurance, billingAmount, ssn[7:len(ssn)])