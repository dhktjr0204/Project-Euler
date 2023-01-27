def isPrime(num):
    for i in range(2, int(abs(num**0.5))+1):
        if num%i==0:
            return False
    return True


def fun(a,b):
    n=0
    result=[]
    while True:
        fun=n**2+a*n+b
        if isPrime(fun)==False:
            break
        result.append(n)
        n+=1
    return result

max_a=0
max_b=0
max_result=[]
for i in range(-999,1000):
    for j in range(-999,1000):
        result=fun(i,j)
        if len(result)>len(max_result):
            max_result=result
            max_a=i
            max_b=j

print(max_a*max_b)