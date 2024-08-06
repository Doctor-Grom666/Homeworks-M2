numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    for j in range(i):
        if j == 0 or j == 1:
            continue
        elif i % j == 0:
            is_prime = False
            break
    if is_prime and i != 1:
        primes.append(i)
    elif not is_prime and i != 1:
        not_primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
