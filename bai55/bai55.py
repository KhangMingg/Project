def tim_snt():
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    if s == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input())

    if n < 1:
        print("False")
        exit()

    print(tim_snt())
