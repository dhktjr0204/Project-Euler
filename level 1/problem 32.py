import itertools

num_list=itertools.permutations('123456789',9)

result_set=set()
for num in num_list:
    first_num=int(num[0])
    second_num=int(num[1]+num[2]+num[3]+num[4])
    result_num=int(num[5]+num[6]+num[7]+num[8])
    if first_num*second_num==result_num:
        result_set.add(result_num)
    first_num=int(num[0]+num[1])
    second_num=int(num[2]+num[3]+num[4])
    result_num=int(num[5]+num[6]+num[7]+num[8])
    if first_num*second_num==result_num:
        result_set.add(result_num)


print(sum(result_set))