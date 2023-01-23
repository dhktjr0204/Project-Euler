num1=1
num2=1
cnt=3
while True:
    num3=num1+num2
    num1=num2
    num2=num3
    if len(str(num3))>=1000:
        print(cnt)
        break
    cnt+=1

