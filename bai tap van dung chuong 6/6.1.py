import threading

def InTenLuong():
    tên_luồng = threading.current_thread().name
    print(f"Tên luồng: {tên_luồng}")

số_luồng = 5

các_luồng = []

for i in range(số_luồng):
    thread = threading.Thread(target=InTenLuong, name=f"Thread-{i+1}")
    các_luồng.append(thread)
    thread.start()

for thread in các_luồng:
    thread.join()

print("Tất cả các luông đã kết thúc !!!")
