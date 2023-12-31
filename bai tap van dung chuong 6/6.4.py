import threading
import math
def GiaiThua(number,result_dict):
    result = math.factorial(number)
    result_dict[number] = result

if __name__ == '__main__':
    Số_nguyên  = int(input('Nhập vào số nguyên : '))
    result = {}
    threads = []

    for i in range(1,Số_nguyên+1):
        thread = threading.Thread(target = GiaiThua , args = (i,result))
        threads.append(thread)
        thread.start()

    for thread in threads :
        thread.join()
    
    for num in result.items():
        print("Giai thừa của số bạn nhập là :\n",result)
