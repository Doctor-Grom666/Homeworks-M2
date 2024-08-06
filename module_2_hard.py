n = int(input('Введите число от 3 до 20: '))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
result = []

for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)

print('Пароль:', ''.join(map(str, result)))
