n = int(input())
mod = 998244353
ans = 0
for _ in range(n):
    ans = (ans * 10 + 1) % mod
print(ans)