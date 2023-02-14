print("========== sum of individual elements ==============")

# method ---- 01---- using "sum()"

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# l2 = sum (x for x in l1) 
# print(l2)

# method ----- 02------- using "for loop"

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

# print(l1)

# total = 0

# for i in range(0,len(l1)):

#     total = total + l1[i]

# print("the sum of all elements in list are : ",total)

# method ---- 03 ------ using "while loop"

# total = 0
# ele = 0

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

# while(ele < len(l1)):

#     total = total + l1[ele]

#     ele += 1

# print("the sum of all elements in list are : ", total)

# method ----- 04 ----- using "recursive way"

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

# def summing(list, size):
#     if (size == 0):
#         return 0
#     else:
#         return list[size - 1] + summing(list, size - 1)

# total = summing(l1, len(l1))

# print("the sum of all elements in list are : ", total)

# method ---- 05 ---- using "ennumerate"

l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

s = 0

for i,a in enumerate(l1):
    s += a
print(s)
