# print("======= count strings ========")
# # count() : returns the number of occurrences 
# s = str(input("enter the string :"))
# print(s.count("a"))

# print("========== sum of individual elements ==============")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# l2 = sum (x for x in l1) 
# print(l2)

# print("============== multiplication of individual elements ==================")
# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# def multiplyList(l1) :
#    result = 1
#    for x in l1:
#         result = result * x
#    return result

# print(multiplyList(l1))

# print("=============== max and min value =================")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# print(l1)
# l2 = print(max(l1))
# l3 = print(min(l1))
# print("================================")
# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# print(l1)
# l2 = set(l1)
# print([l2])


l1 = input("enter the sentence and maitain a space between them :  ").split()
def front_back(l1):
        print(l1[-1] + l1[1:-1] + l1[0])

print(front_back(l1))



