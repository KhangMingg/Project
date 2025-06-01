a = int(input("a = "))
b = int(input("b = "))
mostpoint = 0
if a > b:
    if a - 1 > b:
        mostpoint = a - 1 + b
    else: mostpoint = a + b
elif a < b:
    if b - 1 > a:
        mostpoint = b - 1 + a
    else: mostpoint = b + a
print(mostpoint)
