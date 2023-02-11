import math

def is_triangle(num):
    found=[]
    count=0
    for a in range(3,num+1,3):
        if a in found:
            continue
        for b in range(1,num+1-a):
            c=math.sqrt(a**2+b**2)
            if a+b+c==num:
                found.extend([a,b,c])
                count+=1
    return count


def cal_triangle():
    max_triangle=0
    max_count=0
    for i in range(1,1001):
        count=is_triangle(i)
        if(max_count<count):
            max_count=count
            max_triangle=i
    return max_triangle

print(cal_triangle())

