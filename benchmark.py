import time

while True:
    rangee = input("Enter counting range (can't be smaller than 500): ")
    try:
        num = int(rangee)
        print(f"Counting range: {num}")
        if num < 500:
            raise ValueError
        break
    except ValueError:
        print("Bigger than 500 expected, please try again!")

def count():
    for i in range(1, num):
        print(i)
        
if __name__ == "__main__":
    print("Start counting now...")
    start_time = time.time()
    count()
    end_time = time.time()
    elapsed_time = end_time - start_time
    num_per_sec = num / elapsed_time
    print(f"Counting done! time consumed: {elapsed_time:.2f} seconds")
    print(f"Overall counting speed: {round(num_per_sec, 1)} per second")