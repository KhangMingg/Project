def so_chan(a):
    if a % 2 == 0:
        return True
    else:
        return False

a = float(input())
b = float(input())
c = float(input())
d = float(input())

res = 0
if a % 2 == 0 and (res < a):
    res = a
if b % 2 == 0 and (res < b):
    res = b
if c % 2 == 0 and (res < c):
    res = c
if d % 2 == 0 and (res < d):
    res = d
if res > 0:
    print(res)
else:
    print("NONE")

