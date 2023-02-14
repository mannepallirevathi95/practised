# for i in range(10,200):
#     print(i)



# h = [x for x in range(1, 21) if x % 2 == 0 or x%5 == 0]
# print(h)


# print the numbers till 200
# print the multiples of both 3 and 5 in those 200
# if the number is multiple of 3, print fizz instead of the number
# if the number is a multiple of 5, print Buzz instead of the number
# if the number is a multiple of both 3 and 5, print fizz buzz.

#1,2,fizz,4,Buzz,6,7,8,Fizz,Buzz,11,Fizz,13,14,Fizzbuzz.

#for i in range(201):
#    print(i)


#print("\n\n\n")
#print("=====================++++++++++++++=====================")
#print("\n\n\n")

#for i in range(1,201):
#    if(i % 3 == 0 and i % 5 == 0):
#       print("fizz buzz")
#    elif(i % 3 == 0):
#        print("fizz")
#    elif(i % 5 == 0):
#        print("buzz")
#    else:
#        print(i)

#from typing_extensions import Self
#from unicodedata import name


from math import factorial


class rupa:
    def __init__(self):
       self.name = "rupavali"
       self.age = 23
       self.marks = 100

class Puma:
    def __init__(self, name, age, marks):
       self.name = name
       self.age = age
       self.marks = marks

puma_daughter = Puma("revathi", 25, 300)


# instrance variables and instance method
# class Student:
#     # this is special method called constructer
#     def __init__(self):
#         self.name = 'vishnu'
#         self.age = 20
#         self.marks = 900
#     #this is an instance method.
#     def talk(self):
#         print('hi,Iam' , self.name)
#         print('my age is', self.age)
#         print('my marks are', self.marks)

# # create an instance to student class.
# s1 = Student()

# # call the method using the instance
# s1.talk()
# #print("====== factorial ==============")  
# def factorial(n):
#     if n == 0:
#         result = 1

#     else:
#         result = n*factorial(n-1)

# for i in range(1, 11):
#     print(i, factorial(i))
print("====== str rev loop ============")
string = str(input("enter the string: "))

reverse = ''

for i in range(len(string), 0, -1):
   reverse += string[i-1]

print('The reverse string is', reverse)
