'''
print("Finding the area and perimeter of a square \n")

x = int(input("please enter the length of the side :   "))

square_area = x**2
square_perimeter = 4*x

print(f"The area of the square with side {x} is {square_area} , and the perimeter is {square_perimeter}")


print("=====================================================================")

print("Finding the area and perimeter of a rectangle \n")

l = int(input("please enter the length of the rectangle :  "))

b = int(input("please enter the breadth of the rectangle :  "))

rect_area = l*b
rect_perimeter = 2*(l + b)

print(f"The area of the rectangle with length {l} and breadth {b} is {rect_area} , and the perimeter is {rect_perimeter}")

print("======================================================================")

print("Finding the area and perimeter of a triangle \n")

a = int(input("please enter the adjacent value of  the triangle :   "))

b = int(input("please enter the base value of  the triangle :   "))

c = int(input("please enter the hypotenuse value of  the triangle :   "))

h = int(input("please enter the height value of the triangle :   "))

tri_area = 0.5*(b * h)
tri_perimeter = a + b + c

print(f"The area of the triangle with base {b} and height {h} is {tri_area} , and the perimeter is {tri_perimeter}")

print("======================================================================")

print("Finding the area and perimeter of a parellelogram \n")

d1 = int(input("please enter the diameter D1 value :  "))

d2 = int(input("please enter the diameter D2 value :  "))
 
a = int(input(" please enter any one side S1 of the parellelogram :  "))

b = int(input("please enter another side S2 of the parellelogram :  "))

parell_area = 0.5*(d1 + d2)
parell_perimeter = 2*(a + b)

print(f"The area of the parellelogram with diameter D1 {d1} and diameter D2 {d2} is {parell_area} , and the perimeter is {parell_perimeter}")

print("======================================================================")

print("Finding the area and perimeter of a rhombus \n")

p  = int(input("enter the diagonal value d1 :  "))

q = int(input("enter the another diagonal value d2 :  "))

a = int(input("enter any side of  the rhombus :  "))

rho_area = 0.5*(p * q)
rho_perimeter = 4*a

print(f"The area of the rhombus with diagona d1 {p} and diagonal d2 {q} is {rho_area} , and the perimeter is {rho_perimeter}")

print("======================================================================")

print("Finding the area and perimeter of a circle \n")

r = int(input("enter the radius of circle :  "))

crcl_area = 2*3.14*(r**r)
crcl_perimeter = 2*3.14*r

print(f"The area of the circle with radius {r} is {crcl_area} , and the perimeter is {crcl_perimeter}")

print("======================================================================")

print("Finding the area and perimeter of a semicircle \n")

r = int(input("enter the radius of semicircle :  "))

semicrcl_area = 1.57*(r**r)
semicrcl_perimeter = (3.14*r) + (2*r)

print(f"The area of the semicircle with radius {r} is {semicrcl_area} , and the perimeter is {semicrcl_perimeter}")

print("======================================================================")

print("Finding the area and perimeter of a trapezium \n")

a = int(input("enter the value of A:  "))
b = int(input("enter the value of B:  "))
c = int(input("enter the value of C:  "))
d = int(input("enter the value of D:  "))
h = int(input("enter the value of height :  "))

tra_area = 0.5*(a + b)*h
tra_perimeter = a+b+c+d

print(f"The area of the trapezium  is {tra_area} , and the perimeter is {tra_perimeter}")

print("======================================================================")

print("Finding the area and perimeter of a cone \n")

r = int(input("enter the value of radius, r :  "))

l = int(input("enter the value of slant height of the cone, l :  "))
l
circumference_cone = 2*3.14*r
total_surface_area = 3.14*r*(r + l)

print(f"The area of the cone  is {total_surface_area} , and the perimeter is {circumference_cone}")

print("======================================================================")

print("Finding the area and perimeter of a cube \n")

a = int(input("enter the value of side, a :  "))

surface_area = 6*a*2
cube_perimeter = 12*a

print(f"The area of the cone  is {surface_area} , and the perimeter is {cube_perimeter}")

print("======================================================================")

def Splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'Even'
    else:
        return my_string[0]

names = ['Andy', 'eve', 'sally']
print(list(map(Splicer,names)))

def Sqr(nums):
    return nums ** 2

my_nums = [1, 2, 3, 4]
print(list(map(Sqr,my_nums)))

#print("======= fibonocci seq ========")
# n = input("enter the value: ")
# def Fibonocci():
#     a, b = 0, 1
#     while a < 10:
#         print(a)
#         a, b = b, a+b

# print(Fibonocci())

# print("===== prime nums ======")
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equal', x, '*', n//x)
#     else:
#         print(n, "is a prime number")
'''




