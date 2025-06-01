import math

def largest_perfect_square_divisor(x):
    res = 1
    temp = x
    # Phân tích thừa số nguyên tố
    for i in range(2, int(math.isqrt(temp)) + 1):
        count = 0
        while temp % i == 0:
            temp //= i
            count += 1
        # Lấy lũy thừa chẵn nhỏ nhất trong count
        res *= i ** (count // 2 * 2)
    # Nếu temp còn lại > 1 thì là số nguyên tố
    # không thể tạo ra ước chính phương mới
    return res

def count_perfect_square_pairs(n):
    cnt_map = {}

    for i in range(1, n + 1):
        f_i = largest_perfect_square_divisor(i)
        val = i // f_i
        cnt_map[val] = cnt_map.get(val, 0) + 1

    result = 0
    for v in cnt_map.values():
        result += v * v

    return result

# Đọc dữ liệu
n = int(input())
print(count_perfect_square_pairs(n))