import time
start_time = time.time()

from math import sqrt

def uoc_cua_so(n):
    divs = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))

def so_dac_biet(n):
    for u in range(1, n):
        if n % u == 0:
            if (u + 1) <= n and n % (u + 1)  == 0:
                return True
    return False
so_luong = int(input())

ket_qua = []
for _ in range(so_luong):
    so_can_ktra = int(input())
    if so_dac_biet(so_can_ktra):
        uoc = uoc_cua_so(so_can_ktra)
        uoc_str = [str(d) for d in uoc]
        ket_qua_dong = " ".join(uoc_str)
        ket_qua.append(ket_qua_dong)
    else:
        ket_qua.append("-1")

for line in ket_qua:
    print(line)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Thời gian chạy: {elapsed_time:.6f} giây")