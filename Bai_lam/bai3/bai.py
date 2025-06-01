str = input()
char = 0
ans = 0
for char in str:
    if char.isdigit():
        ans += int(char)
print(ans)
