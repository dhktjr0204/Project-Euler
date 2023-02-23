import math

def is_Prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def Prime():
    prime=[]
    for i in range(2,100000):
        if is_Prime(i)==True:
            prime.append(i)
    return prime
prime_list=Prime()

def Check(i):
    if i in prime_list:
        return False
    x=1
    while x*x*2+1<i:
        if i-x*x*2 in prime_list:
            return False
        x+=1
    return True

def is_not_gold():
    for i in range(3,100000,2):
        if Check(i): 
            return i

print(is_not_gold())