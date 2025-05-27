from math import sqrt

def dien_tich(u, v, z):
    p = (u+v+z) / 2
    tam = sqrt(p*(p-u)*(p-v)*(p-z))
    return tam

def tam_giac(u, v, z):
    if (u + v > z and u + z > v and v + z > u):
        return True
    else:
        return False

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
d1 = sqrt((x2-x1)**2 + (y2-y1)**2)
d2 = sqrt((x2-x3)**2 + (y2-y3)**2)
d3 = sqrt((x1-x3)**2 + (y1-y3)**2)

if tam_giac(d1, d2, d3):
    s = dien_tich(d1, d2, d3)
    print(f"{s:.2f}")
else:
    print("NONE")
