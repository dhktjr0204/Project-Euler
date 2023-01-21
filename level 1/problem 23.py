def sum_divisor(n):
    sum=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i==n**0.5:
                sum-=i
            sum+=i+n/i
    return sum

def find_overnum():
    num_list=[]
    for i in range(12,28123):
        if sum_divisor(i)>i:
            num_list.append(i)
    return num_list

list=find_overnum()
total=set()
for i in list:
    for j in list:
        if i+j<28123:
            total.add(i+j)
result=sum(range(1,28123))-sum(total)
print(result)


