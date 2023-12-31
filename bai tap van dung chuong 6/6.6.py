import threading

mức_ngưỡng = 20

shared_lock = threading.Lock()
số_hiện_tại = 0

def SoChan():
    global số_hiện_tại
    while số_hiện_tại <= mức_ngưỡng:
        if số_hiện_tại % 2 == 0:
            with shared_lock:
                print(f"Even: {số_hiện_tại}")
                số_hiện_tại += 1

def SoLe():
    global số_hiện_tại
    while số_hiện_tại <= mức_ngưỡng:
        if số_hiện_tại % 2 != 0:
            with shared_lock:
                print(f"Odd: {số_hiện_tại}")
                số_hiện_tại += 1

if __name__ == "__main__":
    luồng_lẻ = threading.Thread(target=SoChan)
    luồng_chẵn = threading.Thread(target=SoLe)

    luồng_lẻ.start()
    luồng_chẵn.start()

    luồng_lẻ.join()
    luồng_chẵn.join()
