# A = [1, 2, 3, 'ae']
# B = [1, 1, 'b', 6]
# if alpha char exists then it should be treated as 0
# C = A + B if even otherwise 0
# 1) Get output C. With above example C = [2, 0, 0, 6]
# 2) An find out maximum repeated element in C

A = [1, 2, 3, 'ae']
B = [1, 1, 'b', 6]

a = []
b = []
C = []
count = 0
def func_c():

    for i in A:
        if type(i) == int:
            a.append(i)
        else:
            a.append(0)
    

    for i in B:
        if type(i) == int:
            b.append(i)
        
        else:
            b.append(0)
    
    c = [a[i] + b[i] for i in range(len(a))]
    
    for i in c:
        if i != 3:
            C.append(i) 
            
        else:
            C.append(0)

        count = C.count(0)
  
    return C, f"the repeated item is 0 with {count} times "
    
print(func_c())
# Program to find the largest sum of contiguous integers in the array. 
# Example: if the input is (-10, 2, 3, -2, 0, 5, -15), the largest sum is 8
