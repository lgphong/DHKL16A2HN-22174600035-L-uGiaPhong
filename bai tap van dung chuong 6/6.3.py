import threading

def SoChan():
    for i in range(30,50):
        if i % 2 == 0:
            print(' số chẵn :\n',i)

def SoLe():
    for i in range(30,50):
        if i % 2 != 0 :
            print('Số lẻ : \n',i)

if __name__ == '__main__':
    luồng_lẻ = threading.Thread(target = SoChan)
    luồng_chẵn = threading.Thread(target = SoLe)

    luồng_lẻ.start()
    luồng_chẵn.start()

    luồng_lẻ.join()
    luồng_chẵn.join()