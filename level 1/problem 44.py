import math

def cal(n):
    result=int((n*(3*n-1))/2)
    return result

def Check(n):
    n=abs(n)
    p=(math.sqrt(1+24*n)+1)/6
    return p==int(p)


def find_pentagonal():
    num_list=[]
    for i in range(1,10000):
        num_list.append(cal(i))
    min=999999999
    for i in num_list:
        for j in num_list:
            if Check(i+j) and (Check(i-j) or Check(j-i)):
                if min>abs(i-j):
                    min=abs(i-j)
    return min
print(find_pentagonal())