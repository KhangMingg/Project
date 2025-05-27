number = int(input())
str_num = str(number)
a = int(str_num[0])
b = int(str_num[1])
c = int(str_num[2])

r1 = 100*a + 10*b + c
r2 = 100*a + 10*c + b
r3 = 100*b + 10*c + a
r4 = 100*b + 10*a + c
r5 = 100*c + 10*b + a
r6 = 100*c + 10*a + b

res = r1
if r1 > res:
    res = r1
if r2 > res:
    res = r2
if r3 > res:
    res = r3
if r4 > res:
    res = r4
if r5 > res:
    res = r5
if r6 > res:
    res = r6
print(res)