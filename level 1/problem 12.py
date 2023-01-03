def find_factor(num):
    cnt=1
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            cnt+=1
    return cnt*2
n=0
while True:
    n+=1
    sum=int(n*(n+1)/2)
    if find_factor(sum)>=500:
        print(sum)
        break
