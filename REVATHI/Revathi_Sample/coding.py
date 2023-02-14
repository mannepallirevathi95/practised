# print("======= #1 : first 20 odd and even numbers from ======")

# my_list = [int(x) for x in range(1, 101)]

# for i in my_list:
#     while i <= 20:

#         if i % 2 == 0:
#             print("even :", i)
#         else:
#             print("odd:", i)
        
#         break 
# print("..........................................................")

#print("..........................................................")      

# print("======= #2 : program to find avg, sum, multiplication, highest, lowest, middle elements  ======")


# li = [10, 23, 32, 45, 25, 68, 89, 110]

# print(".....addition.....")
# S = sum(li)
# print(f"the addition of the list is:{S}")

# print("......max and min....")
# mini = min(li)
# maxi = max(li)
# print(f"the min and max value of the list is:{mini}, {maxi}")

# print(".....average .....")
# avg = sum(li)/len(li)
# print(f"the average of the list is:{avg}")

# print("..... multiplication.....")
# multi = 1

# for i in li:
#   multi *= i
# print("the multiplication of the list is {} : ".format(multi))

# print(".....middle terms....")

# print("mid value is ",li[int(len(li)/2)])
#print("..........................................................")

#print("..........................................................")
# print("======== #3 Factorial of a number using recursion =========")

#print("====== factorial ==============") 
  
# def factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*factorial(n-1)
# num = int(input("enter the value : "))
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", factorial(num))
# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
# from multiprocessing import Value


# print("..........................................................")

# print("..........................................................")

# print("===========#4 binary search ===============")

# def binary_search(arr, x):
# 	low = 0
# 	high = len(arr) - 1
# 	mid = 0

# 	while low <= high:

# 		mid = (high + low) // 2

# 		# If x is greater, ignore left half
# 		if arr[mid] < x:
# 			low = mid + 1

# 		# If x is smaller, ignore right half
# 		elif arr[mid] > x:
# 			high = mid - 1

# 		# means x is present at mid
# 		else:
# 			return mid

# 	# If we reach here, then the element was not present
# 	return -1


# # Test array
# arr = [ 2, 3, 4, 10, 40 ]
# x = 10

# # Function call
# result = binary_search(arr, x)

# if result != -1:
# 	print("Element is present at index", str(result))
# else:
# 	print("Element is not present in array")

# print("..........................................................")

# print("..........................................................")

# print("=========== #5 string actions ============ ")

# print("a .Algorithm to find length of string")

# string = "Hello world Iam revathi"

# print("Size of string: ", len(string))

# print("b. Get dictionary with char as key and its count as value")

# string_input = "hello all iam working as an employee "

# words = string_input.split()

# dictionary = {}
# for word in words:
#     if (word[0] not in dictionary.keys()):

#         dictionary[word[0]] = []
#         dictionary[word[0]].append(word)

#     else:
#         if (word not in dictionary[word[0]]):
#             dictionary[word[0]].append(word)

# print(dictionary)

# print("c. Find vowels,consonants count in dictionary format")

# string = input("Enter a string: ")

# resultant = string.lower()

# vowels = "aeiou"

# count = {x:sum([1 for char in resultant if char == x]) for x in vowels}

# print(count)

# print("d. Find special character count")

# def char_count(s):

#     spe_char = 0

#     for i in range(len(s)):

#             spe_char += 1

#     print('Special characters here are:', spe_char)

# str = "Hello@%^*World&^%#@"

# char_count(str)

# print("..........................................................")

# print("..........................................................")


# print("..........................................................")

# print("..........................................................")

# print("======== #7 Product Latop(HP,Dell,Lenovo, Apple =========")

# class Product:

#     def __init__(self,product_id,product_name,product_brand,product_price,product_color,produc_ram):

#         self.product_id=product_id

#         self.product_name=product_name

#         self.product_brand=product_brand

#         self.product_price=product_price

#         self.product_color=product_color

#         self.product_ram=produc_ram

#     def get_details(self):

#         if( hp.product_price > dell.product_price and hp.product_price > lenovo.product_price):

#             print("7.1.Hp has the highest price:", hp.product_price)

#         elif(dell.product_price > hp.product_price and dell.product_price > lenovo.product_price):

#             print("7.1.Dell has the highest price:", dell.product_price)
#         else:

#             print("7.1.Lenovo hasthe highest price:", lenovo.product_price)

#         if (hp.product_price < dell.product_price and hp.product_price < lenovo.product_price):

#             print("7.2.Hp has the lowest price:", hp.product_price)

#         elif (dell.product_price < hp.product_price and dell.product_price < lenovo.product_price):

#             print("7.2.Dell has the lowest price:", dell.product_price)
#         else:

#             print("7.2.Lenovo has the lowest price:", lenovo.product_price)

#         if (hp.product_ram > dell.product_ram and hp.product_ram > lenovo.product_ram):

#             print("7.3.Hp has the highest Ram:", hp.product_ram)

#         elif (dell.product_ram > hp.product_ram and dell.product_ram > lenovo.product_ram):

#             print("7.3.Dell has the highest Ram:", dell.product_ram)
#         else:

#             print("7.3.Lenovo has the highest Ram:", lenovo.product_ram)

#         if (hp.product_ram < dell.product_ram and hp.product_ram < lenovo.product_ram):

#             print("7.4.Hp has the lowest Ram:", hp.product_ram)

#         elif (dell.product_ram < hp.product_ram and dell.product_ram < lenovo.product_ram):

#             print("7.4.Dell has the lowest Ram:", dell.product_ram)
#         else:
#             print("7.4.Lenovo has the lowest Ram:", lenovo.product_ram)


# hp=Product(1234,'HP','hp',10000,'grey',64)
# dell=Product(1345,'Dell','dell',40000,'black',85)
# lenovo=Product(1456,'Lenovo','lenovo',50000,'black',97)
# hp.get_details()
# dell.get_details()
# lenovo.get_details()


# 3. Prepare Programs for below questions
# 	1. Prepare state and assign North South West East 
# 	    north = []
# 		south = ['Andhra Prades', 'Telangana', 'Karnataka','Tamil Nadu', 'Kerala']
# 		west = []
# 		east = []
# 	2. Prepare dictionary with key as state name and value as "list of districts"

# 	1. Prepare state and assign North South West East

# india = ["assam", "andhra pradesh", "odisha", "punjab", "delhi", "gujarat", "karnataka", "haryana", "rajasthan", "himachal pradesh", "uttarakhand", "jharkhand", "chattisgarh", "kerala", "tamilnadu", "madhya pradesh", "west bengal", "bihar", "maharastra", "uttar pradesh", "chandigarh", "telangana", "jammu and kashmir", "tripura", "meghalaya", "goa", "arunachal pradesh", "manipur", "mizoram", "sikkim"]
# indian_north = ["jammu and kashmir", "himachal pradesh", "punjab", " uttarakhand", "haryana", "delhi", "rajasthan", "uttar pradesh", "chandigarh"]
# indian_south = ["andhra", "karnataka", "kerala", "tamilnadu","telangana"]
# indian_east = ["arunachal", "assam", "manipur", "meghalaya", "mizoram", "nagaland", "sikkim", "tripura"]
# indian_west = ["goa", "gujarat", "maharastra"]
# print(f"north states are : {indian_north}\nsouth states : {indian_south}")

# # 	2. Prepare dictionary with key as state name and value as "list of districts"

# india_states_south = {"AndhraPradesh" : ["Anantapur" , "Chittoor", "East Godavari", "Guntur", "Nellore", "Visakhapatnam",  "West Godavari."], "Tamilnadu": ['chennai', 'coimbatore', 'pondicherry'],"Telangana":['Adilabad', 'Bhadradri Kothagudem', 'Hyderabad', 'Jagtial', 'Jangaon', 'Karimnagar', 'Khammam'],"Karnataka":['kolar','banglore', 'raichur'], "kerala":['Kannur', 'Kasaragod', 'Kollam']}

# for item in india_states_south.items():
#     print(item)
def new_decorator(original_func):

    def wrap_func():

        print('before original func')

        original_func()

        print("after original func")

    return wrap_func



@new_decorator
def func_needs_decorator():
    print('i want to be decorated')

print(func_needs_decorator())