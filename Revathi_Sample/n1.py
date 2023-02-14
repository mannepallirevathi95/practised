# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(id(l1))
# x = 10
# x = 20 
# print(x is x )
print("===== fibinocci series =====")
def Fibonocci():
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a+b
print(Fibonocci())

# print("===== tables =====")

# num = int(input("enter the number:  "))
# def tables(num):
#      for i in range(1, 11):
#          print(num, "x", i, "=", num * i)
# tables(num)