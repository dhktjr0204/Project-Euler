def is_prime(num):  
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def delete_num(num):
    str_num=str(num)
    for i in range(len(str_num)):
        left_delete_num=int(str_num[i:])
        right_delete_num=int(str_num[:i+1])
        if is_prime(left_delete_num)==False or is_prime(right_delete_num)==False:
            return False
    return True
    

result=0
cnt=0
for i in range(10,1000000000):
    if delete_num(i)==True:
        result+=i
        cnt+=1
        if cnt==11:
            break
        
print(result)