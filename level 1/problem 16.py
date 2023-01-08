cnt=0
index=1000
result=1
valid_index=[]
sum=0
while index!=0:
    if index%2!=0:
        index=int(index/2)
        valid_index.append(2**cnt)
    else:
        index=int(index/2)
    cnt+=1
    
    

for i in valid_index:
    result*=2**i

for i in str(result):
    sum+=int(i)

print(sum)
