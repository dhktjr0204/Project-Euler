import math

num=math.factorial(100)
sum=0

for i in str(num)[::]:
    sum+=int(i)
print(sum)