result=0
for i in range(2,1000000):
    sum=0
    for j in str(i):
        sum+=int(j)**5
    
    if i==sum:
        result+=sum

print(result)