def multiples(n):
    a, b = 3, 5
    result = []
    for _ in range(0, n):
        if sum(result) < n:
            result += a, b
            a += 3
            b += 5
        else:
            break
    return sorted(result) 

print(multiples(1000))
