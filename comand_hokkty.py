import random

class Game:

    def __init__(self, num_start, num_end):
        self.numbers = [i for i in range(num_start, num_end)]
        self.number = random.choice(self.numbers)
        self.count = 0


    def gam(self, x):
        try:
            if x == self.number:
                self.count = 0
                print(f"Ты угадал число, {self.number}")
                return True
            else:
                if x > self.number:
                    self.count += 1
                    print(f"Загаданное число меньше, количество неудачных попыток: {self.count}")
                
                if x < self.number:
                    self.count += 1
                    print(f"Загаданное число больше, количество неудачных попыток: {self.count}")
        except Exception as e:
            return e


def main():
    try:
        print("Введите диапозон выбора рандомного числа:")
        num_start = int(input("Начало: "))
        num_end = int(input("Конец: "))
        games = Game(num_start, num_end)
        while True:
            x = int(input("Введите число: "))
            if x > num_start and x < num_end:
                y = games.gam(x)
                if y:
                    break
            else:
                print(F"Введите число от {num_start} до {num_end}")

    except Exception as e:
        return e

if __name__ == "__main__":
    main()
