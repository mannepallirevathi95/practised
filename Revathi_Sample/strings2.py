print("======= length of string ======")

# ------- method #1 ---------- using "for-loop"

# def string_len(str):

#     counter = 0

#     for i in str:
#         counter += 1

#     return counter

# str = str(input("enter the string: "))

# print(string_len(str))

# ------- method #2 ---------- using "while-loop"

# def string_len(str):

#     counter = 0

#     while str[counter:]:
#         counter += 1

#     return counter

# str = str(input("enter the string: "))

# print(string_len(str))

# ------- method #3 ---------- using "join and count"

# def findLen(str):

#     if not str:
#         return 0

#     else:
#         some_random_str = 'py'
#         return ((some_random_str).join(str)).count(some_random_str) + 1

 
# str = str(input("enter the string: "))

# print(findLen(str))

# ------- method #4 ---------- using "reduce and lambda"

# import functools
 
# def findLen(string):

#     return functools.reduce(lambda x,y : x+1, string, 0)

# string = str(input("enter the string: "))

# print(findLen(string))

# ------- method #5 ---------- using "sum()"

def str_len(str):
    return sum(1 for i in str)

str = str(input("enter the string: "))

print(str_len(str))
