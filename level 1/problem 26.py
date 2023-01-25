def reptend(d):
    rems,quot=[],''
    r=1
    while r>0:
        rems.append(r)
        q,r=divmod(r*10,d)
        quot=quot+str(q)
        if r in rems:
            pos=rems.index(r)
            return quot[pos:]
    return ''


max=''
num=0
for i in range(1,1001):
    r=reptend(i)
    if len(r)>len(max):
        max=r
        num=i

print(num)