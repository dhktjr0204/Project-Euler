def is_palin(num):
    str_num=str(num)
    if str_num==str_num[::-1]:
        return True
    return False


def get_palindrome():
    result=0
    for i in range(1,1000001):
        binary_num=bin(i)[2:]
        if is_palin(i)==True and is_palin(binary_num)==True:
                result+=i
    return result

print(get_palindrome())