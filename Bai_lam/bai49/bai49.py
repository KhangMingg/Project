n = int(input())
a = int(input())
b = int(input())

p = 0
for x in range(0, n//a +1):
    for y in range(0, n//b +1):
        if a*x + b*y == n:
            print(x, y)
            p = 1
if p == 0:
    print(-1)
