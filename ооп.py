class Calculate:
    
    def __init__(self):
        self.result = 0

    #сложение
    def add(self, a, b):
        self.result = a + b
        return self.result

    # вычитание
    def subtrack(self, a, b):
        self.result = a - b
        return self.result
    
    #умножение
    def multiplay(self, a, b):
        self.result = a * b
        return self.result
    
    #деление
    def devided(self, a, b):
        try:
            self.result = a / b
        except ZeroDivisionError:
            return "На ноль делить нельзя!"

    #возведение в степень   
    def power(self, a, b):
        if b > 0 and a == 0:
            return "Нельзя возвести 0 в отрицательную степень"
        else:
            self.result = a ** b
            return self.result
    
    #корень
    def sqaury(self, a):
        if a == 0:
            return "Нельзя вычислить корень из 0"
        else:
            self.result = a ** 0.5
            return self.result
    
    #очищает результат 
    def clear(self):
        self.result = 0
        return self.result


def main():
    cal = Calculate()
    while True:
        
        print("Меню калькулятора")
        print("Выберите число, для выполнение действия:")
        print("1 - сложить")
        print("2 - вычесть")
        print("3 - умножить")
        print("4 - делить")
        print("5 - возведение в степень")
        print("6 - извлечь корень числа")
        print("7 - очистить результат")
        print("8 - завершить работу")

        x = int(input())

        if x == 1:
            a = int(input("Введите число: "))
            b = int(input("Введите число: "))
            print(cal.add(a, b))
        
        if x == 2:
            a = int(input("Введите число: "))
            b = int(input("Введите число: "))
            print(cal.subtrack(a, b))

        if x == 3:
            a = int(input("Введите число: "))
            b = int(input("Введите число: "))
            print(cal.multiplay(a, b))

        if x == 4:
            a = int(input("Введите число: "))
            b = int(input("Введите число: "))
            print(cal.devided(a, b))
        
        if x == 5:
            a = int(input("Введите число: "))
            b = int(input("Введите число: "))
            print(cal.power(a, b))

        if x == 6:
            a = int(input("Введите число: "))
            print(cal.sqaury(a))
        
        if x == 7:
            cal.clear()
            print("результат очищен")

        if x == 8:
            break


if __name__ == "__main__":
    main()




    