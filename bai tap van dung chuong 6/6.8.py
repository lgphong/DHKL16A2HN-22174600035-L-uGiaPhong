import threading
import random

# Khai báo biến chia sẻ giữa các luồng
shared_lock = threading.Lock()
tổng_phần_tử = 0

def calculate_partial_sum(list_con):
    global tổng_phần_tử
    tổng_phần = sum(list_con)

    with shared_lock:
        tổng_phần_tử += tổng_phần

if __name__ ==  '__main__':
    list = [random.randint(0, 10) for _ in range(100)]
    số_luồng = 5
    kích_cỡ_list_con = len(list) // số_luồng
    sublists = [list[i:i + kích_cỡ_list_con] for i in range(0, len(list), kích_cỡ_list_con)]

    # Tạo và bắt đầu các luồng
    threads = []
    for sublist in sublists:
        thread = threading.Thread(target=calculate_partial_sum, args=(sublist,))
        threads.append(thread)
        thread.start()

    # Đợi tất cả các luồng hoàn thành
    for thread in threads:
        thread.join()

    # In tổng của tất cả các phần tử trong list
    print(f"Tổng của các phần tử trong list: {tổng_phần_tử}")
