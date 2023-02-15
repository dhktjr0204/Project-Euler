def make_num_list(range_num):
    num_list=''
    num=1
    while len(num_list)<range_num:
        num_list+=str(num)
        num+=1
    return num_list

def get_num():
    num_list=make_num_list(1000000)
    n=1
    result=1
    while n<=1000000:
        result*=int(num_list[n-1])
        n*=10
    return result

print(get_num())