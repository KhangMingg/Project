s = input()
s1 = "".join(reversed(s))

def solve():
    if s1 == s:
        return True
    else:
        return False

print(solve())
