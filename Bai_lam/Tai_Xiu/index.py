import random

def tai_xiu():
    balance = 50000
    print(" ")
    print("Chào mừng đến với bet69, nhà đực đến từ châu âu")
    print("Trò chơi: Tài Xỉu")
    print("Luật chơi: điền số tiền cược (chia hết cho 1000) và điền tài hay xỉu để cược")

    vong = 0
    while True:
        vong += 1
        print(" ")
        print(f"_____ Vòng {vong} _____")
        print(f"Số tiền bạn đang có: {balance}")

        if balance < 1000:
            print("Không còn khả năng chơi tiếp!")
            break

        tien_cuoc = int(input("Bạn muốn cược số tiền? (chia hết cho 1000):  "))
        tai_hay_xiu = input("Bạn muốn cược tài hay xỉu? (nhập không dấu không viết hoa): ")

        if tai_hay_xiu not in ["tai", "xiu"]:
            print("Đặt cược không hợp lệ, vui lòng nhập tai hoặc xiu để cược")
        if tien_cuoc <999:
            print()
            continue

        so_trung_thuong = random.randint(1, 2)

        if tai_hay_xiu == "tai":
            if so_trung_thuong == 1:
                balance += tien_cuoc
                print(f"Bạn đã đoán đúng và nhận được {tien_cuoc}")
            else:
                balance -= tien_cuoc
                print(f"Bạn đã đoán sai và mất {tien_cuoc}")
        if tai_hay_xiu == "xiu":
            if so_trung_thuong == 2:
                balance += tien_cuoc
                print(f"Bạn đã đoán đúng và nhận được {tien_cuoc}")
            else:
                balance -= tien_cuoc
                print(f"Bạn đã đoán sai và mất {tien_cuoc}")

        if balance < 1000:
            print(" ")
            print("Bạn không còn khả năng chơi tiếp!")
            break
    print(" ")
    print("Cờ bạc ít th, hết tiền r")

if __name__ == "__main__":
    tai_xiu()
