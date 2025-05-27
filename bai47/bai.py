from math import sqrt

n = int(input())
res = 0
for i in range (1 , n+1):
    if sqrt(i).is_integer():
        res += 1
print(res)