import itertools

def is_Prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def make_num_list(num):
    num_list=itertools.permutations(range(1,num+1))
    return num_list

def find_max_num():
    max=0
    cnt=9
    while True:
        num_list=make_num_list(cnt)
        for i in num_list:
            num=int(''.join(map(str,i)))
            if is_Prime(int(num))==True:
                if max<=int(num):
                    max=int(num)
        if max==0:
            cnt-=1
        else:
            break
    return max

print(find_max_num())

