from sympy import factorint

check=0
num=10

while check<4:
    if len(factorint(num))==4:
        check+=1
    else:
        check=0
    num+=1

print(num-4)
    