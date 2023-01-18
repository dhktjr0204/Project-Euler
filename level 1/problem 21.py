import math
num_list=dict()
pair_list=[]
result=0
for i in range(1,10001):
    sum=1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            sum+=j+i/j
    num_list[i]=sum

for i in range(1,10001):
    for j in range(1,10001):
        if i==num_list.get(j) and j==num_list.get(i) and i!=j:
            result+=i

print(result)