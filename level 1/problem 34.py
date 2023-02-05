import math

def factorial(num):
    sum=0
    num_list=list(str(num))
    for i in num_list:
        sum+=math.factorial(int(i))
    return sum

def find_num():
    sum=0
    for i in range(10,100001):
        if i==factorial(i):
            sum+=i
    return sum

print(find_num())
