n = int(input())
p = 0
for i in range(1, n+1):
    if n % i == 0:
        p += 1
print(p)