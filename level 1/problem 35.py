from collections import deque

def make_prime(num):
    num_list=list(str(num))
    prime_deque=deque(num_list)
    rotate_num=0
    for i in range(len(prime_deque)): 
        prime_deque.rotate()
        rotate_num=int(''.join(prime_deque))
        if check_prime(rotate_num)==False:
            return False
    return True


def check_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def prime():
    cnt=0
    for i in range(2,1000001):
        if make_prime(i):
            cnt+=1
    return cnt

print(prime())