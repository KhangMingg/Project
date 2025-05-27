from math import sqrt
import sys 

sys.stdin = open("bai.inp", "r")
sys.stdout = open("bai.out", "w")

u = input()
a, b, c = map(float, u.split())

print(f"{a + b + c:.3f}")
p = ( a + b + c ) / 2

print(f"{sqrt(p*(p - a)*(p - b)*(p - c)):.3f}")