class InvalidPasswordExcpetion(Exception):
    def __init__(self, message):
        self.msg = message

str = input("Enter a password of at least 8 characters: ")
try:
    if len(str) < 8:
        raise InvalidPasswordExcpetion("You have entered an invalid password")
except InvalidPasswordExcpetion as obj:
    print(obj)
else:
    print("You have entered a valid password")