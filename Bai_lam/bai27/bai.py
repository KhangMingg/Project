def ghep_so():
    a = int(input())
    b = int(input())
    rmin = a;
    if rmin > b:
        rmin = b
    rmax = a;
    if rmax < b:
        rmax = b
    ghep = 10 * rmax + rmin
    print(ghep)

if __name__ == '__main__':
    ghep_so()
