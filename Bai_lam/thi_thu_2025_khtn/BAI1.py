from time import time
time_start = time()


n = int(input())

min_x = 10**6
max_x = -1
min_y = 10**6
max_y = -1

def Lay_diem_x_va_y():

    global min_x, max_x, min_y, max_y

    for _ in range(1, n + 1):
        point = input()
        x, y = map(int, point.split())

        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    chieu_dai = max_x - min_x
    chieu_cao = max_y - min_y
    dien_tich = chieu_dai * chieu_cao
    return dien_tich

print(Lay_diem_x_va_y())

time_end = time()
execution_time = time_end - time_start
print(f"Execution time: {execution_time:.3f} seconds")
