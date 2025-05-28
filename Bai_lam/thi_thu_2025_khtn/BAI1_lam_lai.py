n = int(input())

x_min = 10**7
x_max = -1
y_min = 10**7
y_max = -1

for _ in range (1, n+1):

    point = input()
    x,y = map(int, point.split())

    x_min = min(x_min, x)
    x_max = max(x_max, x)
    y_min = min(y_min, y)
    y_max = max(y_max, y)

chieu_cao = y_max - y_min
chieu_dai = x_max - x_min
dien_tich = chieu_dai * chieu_cao

print(dien_tich)

