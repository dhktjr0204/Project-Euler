import itertools

num_list=itertools.permutations('1234567890',10)
div_list=[2,3,5,7,11,13,17]
def cal_num(num):
    if len(''.join(map(str,num)))==9:
        return False
    for i in range(0,7):
        number=num[i+1]+num[i+2]+num[i+3]
        if int(number)%div_list[i]!=0:
            return False
    return True

def is_insteresting_num():
    sum=0
    for i in num_list:
        if cal_num(i)==True:
            sum+=int(''.join(map(str,i)))
    return sum

print(is_insteresting_num())

