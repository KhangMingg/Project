a = int(input())
b = int(input())
c = int(input())
d = int(input())
v = int(input())

def p(a, v, c):
    p = a - v * c
    return p

def q(a, v, d):
    q = a - v * d
    return q

q_ans = q(a, c, v)
p_ans = p(a, v, d)

if p_ans == 0:
    print("NONE")
    exit()

one = "-1"
int_one = float(one)

print(f"-{q_ans}/{p_ans}")

