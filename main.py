import time

def infinite_timer():
    count = 0
    while True:
        print(f"Таймер работает... Время прошло: {count} секунд")
        count += 1

def main():
    multiplier = float(input("Введите множитель для секунд: "))
    while True:
        start_time = time.time()
        infinite_timer()
        elapsed_time = time.time() - start_time
        time.sleep(1 * multiplier - elapsed_time)

if __name__ == "__main__":
    main()
