max_prime=600851475143
i=2

while i < max_prime:
    if max_prime % i ==0:
        max_prime /= i
    else:
        i += 1


print(max_prime)