import random

class Game2:

    def __init__(self, name_game):
        self.name_game = name_game
    
    def contin_game(self, result):
        game_arr = ["камень", "ножницы", "бумага"]

        result = random.choice(game_arr)
        if result == self.name_game:
            return "Ничья"
        else:
            if self.name_game == "камень" and result == "бумага":
                print(self.name_game)
                print(result)
                return False
            else:
                print(self.name_game)
                print(result)
                return True

            if self.name_game == "ножницы" and result == "камень":
                print(self.name_game)
                print(result)
                return False
            else:
                print(self.name_game)
                print(result)
                return True
            
            if self.name_game == "бумага" and result == "ножницы":
                print(self.name_game)
                print(result)
                return False
            else:
                print(self.name_game)
                print(result)
                return True


def main():
    print("Игра запущена")
    numbers = "1234567890"
    game_arr = ["камень", "ножницы", "бумага"]
    print()

    while True:
        print("Напишите что вы выбрали: камень, ножницы, бумага")
        print("Напишите стоп если хотите завершить игру")
        
        user_game = input()
        result = random.choice(game_arr)
        prov = 0

        for i in user_game:

            if i in numbers:
                prov = True
                break
        
        if prov:
            print("Числа не принимаются!")
            continue

        if user_game == "стоп":
            print()
            print("Игра остановлена")
            break

        game = Game2(user_game)
        res = game.contin_game(result)

        if res:
            print("Вы выиграли!")
        else:
            print("Вы проиграли")
            
if __name__ == "__main__":
    main()