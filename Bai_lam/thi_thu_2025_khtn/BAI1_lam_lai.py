S1 = int(input())
V1 = int(input())
S2 = int(input())
V2 = int(input())

if V1 == V2:
    if S1 == S2:
        print(0)
    else:
        print(-1)
else:
    t = (S2 - S1) / (V1 - V2)
    if t >= 0:
        print(int(t))  # in phần nguyên của thời gian
    else:
        print(-1)