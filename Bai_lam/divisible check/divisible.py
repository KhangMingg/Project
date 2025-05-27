import sys

sys.stdin = open("input.inp", "r")
sys.stdout = open("output.out", "w")
u = input()
a, b = map(float, u.split())

if a % b == 0:
    print(f"{int(a)} is divisible by {int(b)}")
    exit()
else:
    print(f"{int(a)} is not divisible by {int(b)}")
    exit()

