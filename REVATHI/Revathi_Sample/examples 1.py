# print("======================")
# # this is my own creation using len() method
# s = str(input("enter the string value : "))
# l = len(s)
# print(f"the length value of your given string is : {l} ")
# print('======================')

# print('========== method 2 ============')
# # using for loop method
# # defining a function and passing a parameter str
# def findLen(s):

# # initially count value = 0
#     counter = 0  
# #afetr giving a string name, it will loop through the entire string  
#     for i in s:
# #in the loop for each value it will be iterated ith adding each charecter 
#         counter += 1
# # afetr particular iteration it will be returned the length og given string
#     return counter
 
# s = str(input("enter the string value : "))
# print(findLen(s))

# print('======================')
# print('========= method 3 =============')
# def findLen(s):
#     counter = 0
#     while s[counter:]:
#         counter += 1
#     return counter
 
# s = str(input("enter the string value : "))
# print(findLen(s))
# print('======================')

print('========= method 4 =============')
def findLen(s):
    return sum( 1 for i in s)
s = str(input("enter the string value : "))
print(findLen(s))
print('======================')
