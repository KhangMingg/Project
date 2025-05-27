import math

def get_divisors(n):
    """
    Tìm và trả về một danh sách các ước số dương của n, đã được sắp xếp.
    """
    if n <= 0:
        return []
    divs = set() # Dùng set để tự loại bỏ trùng lặp khi n là số chính phương
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))

def is_special(n):
    """
    Kiểm tra xem số n (n >= 2) có phải là số đặc biệt hay không.
    Số đặc biệt có ít nhất một cặp ước liên tiếp (u, u+1).
    """
    # Số nhỏ hơn 2 không thể có 2 ước dương liên tiếp
    if n < 2:
        return False

    # Duyệt các khả năng cho ước nhỏ hơn trong cặp (u)
    # Không cần duyệt hết đến n, vì nếu u và u+1 là ước thì u phải nhỏ hơn n
    # Dừng sớm hơn cũng được, ví dụ đến n//2 + 1, nhưng đến n cũng không sai
    for u in range(1, n):
        # Kiểm tra xem u có phải là ước không
        if n % u == 0:
            # Nếu u là ước, kiểm tra xem u+1 có là ước không
            if (u + 1) <= n and n % (u + 1) == 0:
                # Tìm thấy cặp ước liên tiếp u và u+1
                return True
        # Nếu u > n // 2 thì u + 1 cũng sẽ > n // 2, khả năng tìm được ước giảm
        # nhưng cứ để vòng lặp chạy đến n-1 cho chắc chắn và đơn giản
        # Ví dụ: n=6, u=2 -> 6%2==0, 6%(2+1)==6%3==0 -> True

    # Không tìm thấy cặp ước liên tiếp nào
    return False

# --- Chương trình chính ---
try:
    # 1. Đọc số lượng các số cần kiểm tra
    num_count_str = input() #"Nhập số lượng số nguyên cần kiểm tra: "
    num_count = int(num_count_str)

    if num_count < 0:
        print("Số lượng không thể âm.")
    else:
        results_to_print = [] # Lưu kết quả cho từng số để in cuối cùng

        # 2. Đọc từng số và xử lý
        for _ in range(num_count):
            try:
                num_str = input() # "Nhập số tiếp theo: "
                num = int(num_str)

                # 3. Kiểm tra xem số có đặc biệt không
                if is_special(num):
                    # 4a. Nếu đặc biệt, lấy danh sách ước
                    divisors = get_divisors(num)
                    # Chuyển list các số nguyên thành list các chuỗi để join
                    divisors_str_list = [str(d) for d in divisors]
                    # Nối các chuỗi lại bằng dấu cách
                    result_line = " ".join(divisors_str_list)
                    results_to_print.append(result_line)
                else:
                    # 4b. Nếu không đặc biệt, thêm -1
                    results_to_print.append("-1")

            except ValueError:
                # Xử lý nếu người dùng nhập không phải số nguyên
                print(f"Lỗi: '{num_str}' không phải là số nguyên hợp lệ. Bỏ qua.")
                # Có thể thêm một giá trị lỗi vào results_to_print nếu muốn
                # results_to_print.append("Lỗi Input")

        # 5. In tất cả kết quả đã lưu
        for line in results_to_print:
            print(line)

except ValueError:
    print("Lỗi: Dòng đầu tiên phải là một số nguyên chỉ số lượng.")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")