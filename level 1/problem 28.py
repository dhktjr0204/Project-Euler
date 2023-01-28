def sum(result, num, last_num):
    for i in range(1,5):
        result=result+last_num+(num*i*2)
    last_num=last_num+num*4*2
    if num==500:
        return result
    return sum(result, num+1,last_num)

print(sum(1,1,1))
