def ask_for_int():
    while True:
        try:
            print(int(input("provide a num : ")))
        except:
            print("An exception occurred")
        else:
            print("ok! ok!")
            break
        finally:
            print("good bye!")

ask_for_int()

# my_list = [1, 2, 3, 4, '5']

# try:
#     for i in my_list:
#         print(i**2)
# except:
#     print(f"oh hello revathi what is this '{i}'?")

# try:
#     x = int(input("enter the value of x as non-zero: "))
#     y = int(input("enter the value of y as non-zero: ")) 
#     z = x / y
#     print(z)
# except:
#     print("i told you not to enter in defferent way")
# finally:
#     print("YOU LOST THE LAST CHANCE")
#     print("BYE!!!!!.....") 