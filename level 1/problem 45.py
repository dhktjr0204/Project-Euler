import math

def triangle_num():
    triangle_numbers=[]
    for i in range(1,100000):
        num=(i*(i+1))/2
        triangle_numbers.append(int(num))
    return triangle_numbers

def Check(n):
    p=(math.sqrt(1+24*n)+1)/6
    q=(1+math.sqrt(1+8*n))/4
    return p==int(p) and q==int(q)


def cal():
    triangle_numbers=triangle_num()
    num=0
    for i in triangle_numbers:
        if Check(i)==True:
            num=i
        if num>40755:
            return num

print(cal())