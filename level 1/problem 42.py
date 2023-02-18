import re

def words():
    f=open("C:/Users/정지원/OneDrive/문서/파이썬/words.txt","rt")
    words=f.readline()
    words_arr=re.findall('\w+', words)
    return words_arr

def cal_triangle_num(num):
    result=0.5*num*(num+1)
    return result

def alphabet_to_num():
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_dict={}
    cnt=1
    for i in alphabet:
        alpha_dict[i]=cnt
        cnt+=1
    return alpha_dict

def re_word():
    word_arr=words()
    alpha_dict=alphabet_to_num()
    n=1
    result=0
    for word in word_arr:
        sum=0
        cnt=0
        triangle_num=0
        for i in word:
            sum+=alpha_dict[i]
        while triangle_num<=sum:
            triangle_num=cal_triangle_num(cnt)
            if sum==triangle_num:
                result+=1
                break
            cnt+=1
        n+=1
    return result

print(re_word())