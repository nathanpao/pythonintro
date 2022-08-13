class Product:

    def __init__(self):
        self.name = 'iPhone'
        self.description = 'It is awesome'
        self.price = 700

    def __del__(self):
        print("Inside the desctructor")

    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)


p1 = Product()
p1.display()
p1 = None

p2 = Product()
p2.display()
p2 = None

