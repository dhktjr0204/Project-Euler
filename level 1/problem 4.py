result=[]
for i in range(999,100,-1):
    for j in range(999,100,-1):
        num=str(i*j)
        if len(num)==6:
            a, b, c, d, e, f=num[0],num[1],num[2],num[3],num[4],num[5]
            if a==f and b==e and c==d:
                result.append(int(num))
        elif len(result) ==0:
            a, b, c, d, e=num[0], num[1], num[2], num[3]
            if a==e and b==d:
                result.append(int(num))
            
print(max(result))