def cha_het():
    n = int(input())
    if n % 3 == 0 and n % 5 != 0:
        print("True")
    else:
        print("False")

if __name__ == '__main__':
    cha_het()