#bmi = weight in kg/(height in meters * height in meters)
def calculateBMI(height, weight=70):
    heightInMeters = height * 0.4536
    bmi = weight / (heightInMeters * heightInMeters)
    return bmi
print(calculateBMI(5.8,70))
print(calculateBMI(6.8,100))
print(calculateBMI(5.6,70))
print(calculateBMI(5.2))