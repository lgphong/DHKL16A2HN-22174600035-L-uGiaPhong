class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def next(self):
        months_with_days = {
            1: 31,  
            2: 28,  
            3: 31,  
            4: 30,  
            5: 31, 
            6: 30,  
            7: 31,  
            8: 31,  
            9: 30,  
            10: 31, 
            11: 30,  
            12: 31   
        }
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            months_with_days[2] = 29  

        if self.day < months_with_days[self.month]:
            self.day += 1
        else:
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

date1 = Date()
print("Ngày ban đầu:")
date1.display()
date1.next()
print("Ngày tiếp theo:")
date1.display()
