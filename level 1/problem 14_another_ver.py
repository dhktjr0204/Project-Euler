dictionary=dict()
for i in range(1,1000001):
    num=i
    cnt=0
    while True:
        if i==1:
            cnt+=1
            break
        if i in dictionary:
            cnt=cnt+dictionary[i]
            break
        if i%2==0:
            i=i/2
        else:
            i=3*i+1
        cnt+=1
    dictionary[num]=cnt

print(max(dictionary,key=dictionary.get))