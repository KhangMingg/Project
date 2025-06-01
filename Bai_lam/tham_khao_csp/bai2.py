n, p = map(int, input().split())
a = list(map(int, input().split()))
a.sort()  # Sắp xếp mảng để áp dụng two pointers

count = 0
left = 0
right = n -1

while left < right:
    if a[left] + a[right] <= p:
        count += right - left
        left +=1
    else:
        right -= 1
print(count)


