n = int(input())

def solve(n):
    p = 0
    for i in range(1, n + 1):
        if n % i == 0:
            p += i
    print(p)

solve(n)