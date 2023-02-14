from math import factorial


print("============== functions based examples ==================")

# print("======== paalindrome or not =========== ")

# p = str(input("enter palindrome value :  "))
# def Palindrome(p):
#     if p == p[::-1]:
#         print("yes it is a palindrome")

#     else:
#         print("this is not a palindrome!!")

#     return p

# print(Palindrome(p))

# print("======== even and odd =========== ")

# num = int(input("enter the range :  "))
# p = [x for x in range(num)]
# def Even_odd(p):
#     for i in p:
#         if i % 2  == 0:
#             print("E = ",i)
#         else:
#             print("O = ",i)
        

# print(Even_odd(p))

# print("======== prime numbers =========== ")

# num = int(input("Enter the input Range : "))
# def Prime_nums():
#     for x in range(1,num):
#         for i in range(2,x):
#             if (x % i == 0):
#                 break
#         else:
#             print(x)

# print(Prime_nums())

#print("======== factorial of number =========== ")

# number = int(input("enter the num : "))
# def Factorial(n):
#     if (n == 1 or n == 0):
#         return 1
#     else:
#         return n * factorial(n - 1)
    

# print(Factorial(number))

#print("======== multi =========== ")
# num = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

# def Multi_func(num):
#     print(tuple(num))
#     print(set(num))
#     return num
# print(Multi_func(num))

#print("======== cube and square =========== ")

# num = int(input("enter the number : "))
# x =  num ** 2
# y = num ** 3

# def Cube_square(num):
#     if num > 0:
#         return f"given num : {num}\nsquare is : {x}\ncube is : {y}"

#     else:
#         return num
# print(Cube_square(num))

#print("======== table format =========== ")

# num = int(input("enter the number:  "))
# def Tables(num):
#     for i in range(1, 11):
#         print(num, "x", i, "=", num * i)

# print(Tables(num))

#print("======== max of three =========== ")

# n = [int(x) for x in input("enter the only 3 no.s and maitain a space between them :  ").split()]

# def Max_of_three(n):

#     if len(n) == 3:
#         return max(n)
#     elif len(n) < 3:
#         print("try again")
#     else:
#         print("limit extented")

# print(Max_of_three(n))

#print("======== fibonacci series =========== ")

# def Fib_seq(n):
    
#     if n <= 1:
#         return n
#     else:
#         return (Fib_seq(n-1) + Fib_seq(n-2))

# term = int(input("enter how many terms you need: "))

# if term <= 0:
#     print("negative values are not allowed")
# else:
#     print("Fibonacci series:")
    
#     for i in range(term):

#         print(Fib_seq(i))

# print("======== sum of all elements =========== ")

# list = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

# def Sum_of(list):

#     total = 0

#     for i in range(0, len(list)):

#         total = total + list[i]

#     return f"the sum of all elements in list is : {total}"

# print(Sum_of(list))

# print("======== multiply all elements  =========== ")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
 
# def multiplyList(l1) :
#     result = 1
#     for x in l1:
#         result = result * x
#     return result

# print(multiplyList(l1))

# print("======== string reverse  =========== ")

# s = str(input("enter the string: "))

# def String_rev(s):
#     string = "".join(reversed(s))
#     return f"your main string is: {s} and the reversed string is: {string}"

# print(String_rev(s)) 

# print("======== check number =========== ")

# num = int(input("enter the range: "))

# list = [x for x in range(1,num)]

# print(list)

# def Num_check():

#     number = input("now enter the value that you want to check : ")

#     for number in list:
#         return True
#     else: 
#         return False

# print(Num_check())

#print("======== calculation of upper and lower case =========== ")

# letter = str(input("its better give a word or a string: "))

# u = letter.upper()
# l = letter.lower()

# def Up_low(letter):
     
#    return f"upper case : {u}\nlower case : {l}"

# print(Up_low(letter))

#print("======== return unique elements of the list =========== ")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

# def Unique():

#     return set(l1)
# print(Unique())

#print("======== even nums from given list =========== ")

# l1 = int(input("enter the number :  "))

# e = [x for x in range(l1) if x % 2 == 0]

# def Even_nums():

#    return f"now the even list is :\n{e}\n"

# print(Even_nums())

#print("======== pascal triangle =========== ")

# n = int(input("enter the limit in digits: "))

# def Pascal():
      
#     for i in range(n):
    
#         print(' '*(n-i), end='')
 
    
#         print(' '.join(map(str, str(11**i))))

# print(Pascal())

#print("======== group of strings =========== ")

# string = str(input("enter the string to be displayed : ")).split()

# def Group_by():

#     return string

# print(Group_by())

#print("======== Panagram =========== ")

# import string
  
# def ispangram(str):

#     alphabet = "abcdefghijklmnopqrstuvwxyz"

#     for char in alphabet:

#         if char not in str.lower():

#             return False
  
#     return True
      
# string = str(input("enter the sentence: "))

# if(ispangram(string) == True):

#     print("Yes")

# else:

#     print("No")

# print("======== Match the dictnories =========== ")

# dict_one = {'a': 1, 'b': 2, 'c': 3}
# dict_two = {'a': 1, 'b': 2}

# for key in dict_one:
    
#     if key in dict_two:

#         val1 = dict_one[key]
#         val2 = dict_two[key]
        
#         print('{},{}'.format(val1, val2))

# print("========= len string loop ==========")

# def findLen(str):
#     counter = 0   
#     for i in str:
#         counter += 1
#     return counter
 
 
# str = str(input("enter the string: "))
# print(findLen(str))

# print("======== tic-tac-toe ========")

# game_list = [1, 2, 3]

# def display_game(game_list):
#     print("here is the current list : ")
#     print(game_list)

# display_game(game_list)

# def position_choice():
#     choice = "wrong"
#     while choice not in [1, 2, 3]

