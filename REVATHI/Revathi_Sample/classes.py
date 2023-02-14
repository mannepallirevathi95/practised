print("====== classes and objects =======")

print("===== #1 - my dog details ======")

class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = 'spitz', name = 'coco', spots = False)

print(my_dog.Dog())

print("===== #2 - my pen details ======")

class Pen():
    def __init__(self, name, type, color ):
        self.name = name
        self.type = type
        self.color = color

my_pen = Pen(name = 'ocean', type = 'gel', color = 'black' )

print(my_pen.type)

print("===== #3 - my book details ======")

class Books():
    def __init__(self, name, lines, long ):
        self.name = name
        self.lines = lines
        self.long = long

my_book = Books(name = 'classmate', lines = True, long = False )

print(my_book.long)

print("===== #4 - my bag details ======")

class Bag():
    def __init__(self, name, color, type):
        self.name = name
        self.color = color 
        self.type = type

my_bag = Bag(name = 'Fur jaden', type = 'laptop bag', color = 'black')

print(my_bag.name)

print("===== #5 - my dress details ======")

class Dress():
    def __init__(self, color, type):
        self.color = color 
        self.type = type

my_dress = Dress(type = 'long gown', color = 'blue')

print(my_dress.type)

print("===== #6 - my hairband details ======")

class Hair_band():
    def __init__(self, color, type, size):
        self.color = color 
        self.type = type
        self.size = size

my_hairband = Hair_band(type = 'satin', color = 'blue', size = 'small')

print(my_hairband.type)

print("===== #7 - my water bottle details ======")

class Water_bottle():
    def __init__(self, color, water, small):
        self.color = color 
        self.water = water
        self.small = small

my_water = Water_bottle(water = True, color = 'blue', small = False)

print(my_water.color)

print("===== #8 - my cabin details ======")

class Cabin():
    def __init__(self, number, type, boring):
        self.number = number
        self.type = type
        self.boring = boring

my_cabin = Cabin(boring = True, number = '251', type = 'square')

print(my_cabin.number)

print("===== #9 - my employee details ======")

class Emp():
    def __init__(self, name, id, team):
        self.name = name
        self.id = id
        self.team = team

my_emp = Emp(name = 'Revathi', id = '413', team = 'T06')

print(my_emp.id)

print("===== #10 - my story details ======")

class Story():
    def __init__(self, name, actor, year):
        self.name = name
        self.actor = actor
        self.year = year

my_stry = Story(name = 'Frozen', actor = 'Elsa and Anna', year = '2020')

print(my_stry.year)

print("===== area and perimeter ======")

print("===== #11 - square ======")

class Square():
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    def perimeter(self):
        return self.side * 4

square = Square(2)
print(square.area())

print("===== #12 - rectangle ======")

class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)

rectangle = Rectangle(2 , 3)
print(rectangle.area())

print("===== #13 - triangle ======")

class Triangle():
    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        return 0.5 * (self.b * self.height)
    def perimeter(self):
        return self.a + self.b + self.c

triangle = Triangle(1, 2, 3, 2)
print(triangle.perimeter())

print("===== #14 - parellelogram ======")

class Parellelogram():
    def __init__(self, D1, D2, S1, S2):
        self.D1 = D1 
        self.D2 = D2  
        self.S1 = S1 
        self.S2 = S2 

    def area(self):
        return 0.5 * (self.D1 + self.D2)
    def perimeter(self):
        return 2 * (self.S1 + self.S2)

parellelogram = Parellelogram(4, 4, 2, 2)
print(parellelogram.area())

print("===== #15 - rhombus ======")

class Rhombus():
    def __init__(self, D1, D2, S):
        self.D1 = D1 
        self.D2 = D2  
        self.S = S 

    def area(self):
        return 0.5 * (self.D1 * self.D2)
    def perimeter(self):
        return 4 * self.S

rhombus = Rhombus(2, 2, 3)
print(rhombus.area())
        


# class Dog:
    
#     # Class Object Attribute
#     species = 'mammal'
    
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name

# sam = Dog('Lab','Sam')
# sam.name

class Product():
    def __init__(self, product_id, product_name, brand, color, RAM):
        self.product_id = product_id 
        self.product_name = product_name  
        self.brand = brand
        self.color = color
        self.RAM = RAM

    def get_data(self):
        print(self.product_name, self.product_id, self.color)
    

laptop = Product()
print(laptop.get_data())