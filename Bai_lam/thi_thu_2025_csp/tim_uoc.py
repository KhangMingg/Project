from math import isqrt

n = int(input())

def has_consecutive_divisors(x):
    divisors = []
    for i in range(1, isqrt(n) + 1):
        if x % i == 0:
            divisors.append(i)

    return divisors

for i in range (n):
    u = int(input())
    ans = has_consecutive_divisors(n)
    print(ans)
