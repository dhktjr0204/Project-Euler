def num1(x):
    if x>=0 and x<=10:
        n=[0,3,3,5,4,4,3,5,5,4,3]
        return n[x]
    if x>10 and x<20:
        n=[6,6,8,8,7,7,9,8,8]
        return n[x-11]

def num2(x):
    if x<20:
        return num1(x)
    if x>=20 and x<100:
        n=[6,6,5,5,5,7,6,6]
        return n[(x//10)-2]+num1(x%10)

def num3(x):
    if x<100:
        return num2(x)
    if x>=100:
        a=x//100
        b=x%100
        if b==0:
            return num1(a)+7
        else:
            return num1(a)+num2(b)+10
S=11
for i in range(1,1000):
    S+=num3(i) 

print(S)