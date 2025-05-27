import sys
import math
sys.stdin = open("bai1.inp","r")
sys.stdout = open("bai1.out","w")
u = input()
x1, y1, x2, y2 = map(float, u.split())
print(f"{(math.sqrt((((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))))):.3f}")
