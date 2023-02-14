# print("======= method 1 ========")
# # count() : returns the number of occurrences 
# s = str(input("enter the sentence to be counted :"))
# print(s.count("a"))

# print("========== sum of individual elements ==============")

# l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
# l2 = sum (x for x in l1) 
# print(l2)

# print("============== multiplication of individual elements ==================")
l1 = [int(x) for x in input("enter the numbers and maitain a space between them :  ").split()]
def multiplyList(l1) :
   result = 1
   for x in l1:
        result = result * x
   return result

print(multiplyList(l1))

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



