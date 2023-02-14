# '''
# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# # def mul_List(l1) :
# #    result = 1
# #    for x in l1:
# #         result = result * x
# #    return(result)
# # print(mul_List(l1))
# # class File:
# #     def __init__(self, filename, mode):
# #         self.filename = filename
# #         self.mode = mode

# #     def __enter__(self):
# #         print(f'Opening the file {self.filename}.')
# #         self.__file = open(self.filename, self.mode)
# #         return self.__file

# #     def __exit__(self, exc_type, exc_value, exc_traceback):
# #         print(f'Closing the file {self.filename}.')
# #         if not self.__file.closed:
# #             self.__file.close()

# #         return False


# # with File('data.txt', 'r') as f:
# #     print(int(next(f)))

# Programs:
# ----------
# - Between 1 to 100
#     1. Print all numbers  
#     2. Print even numbers
#     3. Print odd numbers 
#     4. Print all prime numbers
#     5. Print numbers with power of 2 (1 2 4 8 16 32 64)
#     6. Print all numbers which are divisible by 5 and 7 
#     7. Print all numbers which are divisible by 4 or 6
#     8. Print first 14 odd numbers 
#     9. Print first 23 even numbers
#    10. Print first 6 numbers which are divisible by 4 and 6 
#    11. Print all numbers except divisible by 9
#    12. Write for loop to explain all data structures.
  
# number = [int(x) for x in range(1, 101)]

# print("===== #1 all numbers printing ======")

# print(number)

# print("===== #2 all even numbers printing ======")

# evens = []
# for i in number:
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)

# print("===== #3 all odd numbers printing ======")

# odds = []
# for i in number:
#     if i % 2 != 0:
#         odds.append(i)
# print(odds)

# print("===== #4 all prime numbers printing ======")

# primes = []

# for num in range(1, 101):

#     for i in range(2,num):

#         if (num % i == 0):
#             break

#     else:
#         primes.append(num)

# print(primes)

# print("===== #5 all square numbers printing ======")

# squares = []

# for i in number:
#     squares.append(i**2)

# print(squares)

# print("===== #6 all numbers which are divisable by 5 and 7 printing ======")

# for i in number:

#     if i % 5 == 0 and i % 7 == 0:

#         print(i)

# print("===== #7 all numbers which are divisable by 4 and 6 printing ======")

# for i in number:

#     if i % 4 == 0 and i % 6 == 0:

#         print(i)

# print("===== #8 first 14 odd numbers printing ======")

# for i in number:

#     while i <= 14:

#         if i % 2 != 0:
#             print("odd :", i)
        
        
#         break

# print("===== #9 first 23 even numbers printing ======")

# for i in number:

#     while i <= 23:

#         if i % 2 == 0:
#             print("even :", i)
        
        
#         break

# print("===== #10 first 6 numbers which are divisable by 4 and 6 printing ======")

# limit = []

# for i in number:

#     if i % 4 == 0 and i % 6 == 0:

#         limit.append(i)

# print(limit[0:6])

# print("===== #11 all numbers printing except divisible by 9 ======")

# non_9_divisables = []

# for i in number:

#     if i % 9 == 0:
#         continue
#     non_9_divisables.append(i)

# print(non_9_divisables)

# print("===== #13 loops ======")

# 3. Prepare Programs for below questions
# 	1. Prepare state and assign North South West East 
# 	    north = []
# 		south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
# 		west = []
# 		east = []
# 	2. Prepare dictionary with key as state name and value as "list of districts"

# # Andhra_Pradesh = {"North" : "n", "South" : "s", "East" : "e", "West" : 'w'}
# # Telangana = {"North" : "n", "South" : "s", "East" : "e", "West" : 'w'}
# # Karnataka = {"North" : "n", "South" : "s", "East" : "e", "West" : 'w'}
# # Tamil_nadu = {"North" : "n", "South" : "s", "East" : "e", "West" : 'w'}
# # Kerala = {"North" : "n", "South" : "s", "East" : "e", "West" : 'w'}
# # list_of_districts = []

# india = {"AndhraPradesh" : ["Nellore","Chittoor",], "Telangana": [],"Tamilnadu":[],"Karnataka":[], "kerala":[]}
# print(india["AndhraPradesh"])
# '''

# #list1 = [1,2,3,'vn2',[5,6,7,['pyspark',['sql',['dm']]]]]
# #write a python program to print 6 and SQL.
# # list1 = [1,2,3,'vn2',[5,6,7,['pyspark',['sql',['dm']]]]]

# # one = list1[4][1]
# # two = list1[4][3][1][0]
# # two_o = two.upper()

# # print(f"the first value given to be printed is: {one}\nand\nthe second thing is:{two_o}")

# # list_one = [[1,2,3],[4,5,6],[7,8,9]]
# # l1 = list_one[0]
# # l2 = list_one[1]
# # l3 = list_one[2]
# # new_line = [print(f"{l1}\n{l2}\n{l3}")]
# # print(new_line)
# # list1 = [5,12,7,10,15,20,9] 
# # #  
# # x = list1[0] + list1[-2]
# # y = list1[3] + list1[4]
# print("---------8.Employee Hike Details----------")
# #Create employee class
# # class Employee:
# #     def __init__(self,eid,name,sal,exp,rating):
# #         self.eid=eid
# #         self.name=name
# #         self.sal=sal
# #         self.exp=exp
# #         self.rating=rating
# #     def get_hike(self):
# #         print("Salary is:",self.sal)
# #         average=(self.exp+self.rating)/2
# #         if(average<2):
# #             hike=self.sal+(10*self.sal/100)
# #             print("After hike total salary is:",hike)
# #         elif average>=2 or average<5:
# #             hike =self.sal+(20 * self.sal / 100)
# #             print("After hike total salary is:",hike)
# #         elif average>=5 or average<8:
# #             hike = self.sal + (30 * self.sal / 100)
# #             print("After hike total salary is:",hike)
# # get_emp=Employee(404,'Sireesha',30000,3,8)
# # get_emp.get_hike()
# #out2 = [['A','Laptop',2], ['A', 'Mouse',1], ['A','Headset',1], ['B','Laptop',1],['B','Headset',1]]



inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A','Headset'],['B','Headset'] ]

l1 = []
for item in inp:
    l1.append([item, inp.count(item)])
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)