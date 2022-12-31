def prime(num):
    if num==2:
        return True
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

sum=0
i=2
for i in range(2,2000001):
    if prime(i):
        sum+=i
    i+=1
print(sum)