from math import sqrt
def can_bac_hai():
    a = float(input())
    b = float(input())
    c = float(input())
    delta = b*b - 4*a*c
    if delta < 0:
        print("PT vo nghiem")
    if delta == 0:
        x = -b / 2*a
        print(f"PT co nghiem kep x = {x} ")
    elif delta > 0:
        x1 = (-b + sqrt(delta)) / 2*a
        x2 = (-b - sqrt(delta)) / 2*a
        print(f"PT co hai nghiem phan biet: \n x1 = {round(x1, 2)} \n x2 = {round(x2, 2)}")

if __name__ == '__main__':
    can_bac_hai()