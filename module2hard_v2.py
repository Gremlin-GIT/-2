def generate_password(n):
    password = ''
    pairs = []
    for i in range(1, 21):
        for j in range(i + 1, 21):
            pair_sum = i + j
            if n % pair_sum == 0:
                pairs.append((i, j))
    for pair in pairs:
        password += f"{pair[0]}{pair[1]}"
    return password
for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - {result}")