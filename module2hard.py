def find_pairs(dividend):
    pairs = []
    for i in range(1, dividend):
        for j in range(1, dividend):
            if (i + j) <= dividend and dividend % (i + j) == 0:
                pairs.append((i, j))
    return pairs
for number in range(3, 21):
    print(f'Для числа {number} подходящие пары: {find_pairs(number)}')
