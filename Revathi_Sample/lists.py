print("=====list based problems===========")

# print("========== sum of individual elements ==============")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# l2 = sum (x for x in l1) 
# print(l2)

# print("======== Mulitply of elements========")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# def multiplyList(l1) :
#     result = 1
#     for x in l1:
#         result = result * x
#     return result

# print(multiplyList(l1))

# print("============ longest and smallest number ====================")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# print(l1)
# l2 = print(max(l1))
# l3 = print(min(l1))

# print("============ sorting elements in increasing order ====================")
# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# print(l1)
# l1.sort()
# print(l1)

# print("========= remove duplicates ==========")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# l3 = list(set(l1))
# print(l1)
# print(f"the result: {l3}")

# print("========= check weather it is empty ==========")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# l2 = []

# if l2 == l1:
#     print("empty")
# else:
#     print("hi")

# print("========= copy of a list ==========")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]

# l2 = l1.copy()
# l3 =[]
# for i in l1:
#     l3.append(i)
# print(l1,l2,l3)

def Splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'Even'
    else:
        return my_string[0]

names = ['Andy', 'eve', 'sally']
print(list(map(Splicer,names)))
