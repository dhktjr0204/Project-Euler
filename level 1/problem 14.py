def find_longer(num):
    cnt=0
    while(num!=1):
        if num%2==0:
            num/=2
            cnt+=1
        else:
            num=3*num+1
            cnt+=1
    return cnt

max=0
for i in range(1,1000001):
    count=find_longer(i)
    if max<count:
        max=count
        num=i
print(num)
    