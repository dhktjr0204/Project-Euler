def square_sum(num):
    return sum(i**2 for i in range(1,num+1))

def sum_square(num):
    return sum(i for i in range(1,num+1))**2

def calc(num):
    return sum_square(num)-square_sum(num)

print(calc(100))