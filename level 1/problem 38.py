def is_pandigital(num_list):    
    pandigital_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return all(num in num_list for num in pandigital_list)


def cal_pandigital():
    max_num=0
    for num in range(2,100000):
        result_str=''
        result_str_list=[]
        n=1
        while len(result_str)<9:
            result_num=num*n
            result_str_list.append(str(result_num))
            result_str=''.join(result_str_list)
            n+=1

        if len(result_str)==9:
            result_str_list=list(result_str)
            if is_pandigital(result_str_list) and int(result_str)>max_num:
                max_num=int(result_str)
    return max_num

print(cal_pandigital())