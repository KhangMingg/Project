from math import sqrt
def diem_va_dg_tron():
    x1 = float(input())
    x2 = float(input())
    y1 = float(input())
    y2 = float(input())
    r = float(input())
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if d < r:
        print("IN")
    else:
        print("OUT")
if __name__ == "__main__":
    diem_va_dg_tron()