import math

def perms(n, list):
##list로부터 n번째의 수열 리스트를 찾는다
    if n==0:
        return list

    l=len(list) ##리스트 길이
    
    n= n %math.factorial(l)
    #q는 몫(정해진 요소), r는 나머지(아직 남아있는 순열의 양)
    q,r=divmod(n, math.factorial(l-1))
    
    return [list[q]]+perms(r,list[:q]+list[q+1:])


print("".join(perms(999999,list('0123456789'))))
