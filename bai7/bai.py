from math import sqrt
import sys

def distance_points(ax, ay, bx, by):
    return sqrt(pow(bx - ax, 2) + pow(by - ay, 2))

sys.stdin = open("bai.inp", "r")
sys.stdout = open("bai.out", "w")

u = input()
x1, y1, x2, y2, x3, y3  = map(float, u.split())

print(f"{sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)):.3f}") # distance jame, john
print(f"{sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2)):.3f}") # distance jame, amy  
print(f"{sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2)):.3f}") # distance john, amy

dab = distance_points(x1, y1, x2, y2)
dbc = distance_points(x2, y2, x3, y3)
dac = distance_points(x1, y1, x3, y3)
print("d_AB = {:.3f}".format(dab))
print("d_BC = {:.3f}".format(dbc))
print("d_AC = {:.3f}".format(dac))
