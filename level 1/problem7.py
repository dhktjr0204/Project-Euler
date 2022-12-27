def prime(number):
    if number<2:
        return False

    if number==2:
        return True

    if number%2==0:
        return False

    for i in range(3,int(number**0.5)+1):
        if number%i==0:
            return False
    return True

i=2
cnt=0
while True:
    if prime(i):
        cnt+=1
        if cnt==10001:
            break
    i+=1

print(i)