def is_Prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def Check():
    for i in range(1000,3330):
        if is_Prime(i):
            p2=i+3330
            p3=i+6660
            if set(list(str(i)))==set(list(str(p2)))==set(list(str(p3))) and i!=1487:
                if is_Prime(p2) and is_Prime(p3):
                    return str(i)+str(p2)+str(p3)
                    
print(Check())
