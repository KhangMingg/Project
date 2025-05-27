from math import sqrt
from time import time

start_time = time()

"""
Body
"""

def dist_from_0_0(a, b):
    """
    Hàm này tính khoảng cách của một điểm so với 0 0
    """
    return sqrt((a - 0) ** 2 + (b - 0) ** 2)

def solve():
    """
    Hàm này chứa code chính trong bài
    """
    n = int(input()) #thay bằng int(input()) khi còn 5p cuối
    luu_vao_string = []

    for i in range (1, n+1):
        u = input() #thay bằng input() khi còn 5p cuối
        part = u.split()
        cord_x = int(part[0])
        cord_y = int(part[1])
        dist = dist_from_0_0(cord_x, cord_y)
        luu_vao_string.append(dist)
    luu_vao_string.sort(reverse=True)
    try:
        if len(luu_vao_string) < 2:
            so_lon_thu_hai = luu_vao_string[0]
        else:
            so_lon_thu_hai = luu_vao_string[1]
    except Exception:
        exit(0)

    return so_lon_thu_hai


"""
End of body
"""

print(f"{solve():.2f}")

end_time = time()
excution_time = end_time - start_time

print(f"Code chạy trong:{excution_time:.5f}")
