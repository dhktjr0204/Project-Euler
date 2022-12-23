import math
LCM=1
for i in range(1,21):
    GCD=math.gcd(i,LCM)
    LCM=int(i*LCM/GCD)

print(LCM)