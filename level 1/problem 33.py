from fractions import Fraction

exception_list=['11','22','33','44','55','66','77','88','99']

result=1
for deno in range(11,99):
    for nume in range(10,98):
        if nume>=deno or nume in exception_list or deno in exception_list:
            continue
        deno_list=list(str(deno))
        nume_list=list(str(nume))
        for i in deno_list:
            if i in nume_list and i!='0':
                nume_list.remove(i)
                deno_list.remove(i)
                try:
                    if nume/deno==int(nume_list[0])/int(deno_list[0]):
                        result*=int(nume_list[0])/int(deno_list[0])
                        
                except ZeroDivisionError as e:
                    pass         
print(Fraction(result).limit_denominator().denominator)       



