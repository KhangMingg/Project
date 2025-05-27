n = int(input())

if n > 10000000:
    print("NONE")
    exit(0)

a = 500
b = 200
c = 100

def solve():
    p = 0
    for x in range(0, n//a + 1):
        for y in range(0, n//b+ 1):
            for z in range(0, n//c + 1):
                if a*x + b*y + c*z == n:
                    p = 1
                    print(x, y, z)
    if p == 0:
        print("NONE")
if __name__ == '__main__':
    solve()

