import random
import os

class Password:
    alfavit = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    number = "1234567890"
    specical_simvol = "!#$&"

    #гененируем пароль и сохраняем в файл
    def generated_password(self, name_ak ,len_password):
        try:
            alfavit = "QWERTYUIOPASDFGHJKLZXCVBNM"
            numbers = "1234567890"
            alfavit_simvol = "qwertyuiopasdfghjklzxcvbnm"
            password = ""

            for i in range(len_password):
                strok_password = random.choice(alfavit)
                number_password = random.choice(numbers)
                strok_password2 = random.choice(alfavit_simvol)
                password += strok_password + number_password + strok_password2
            
            with open(f"C:/Users/admin/password_d/password_{name_ak}.txt", "w") as f:
                f.write(f" {name_ak} пароль: {password}" + '\n')
                return True
                
        except Exception as e:
            return e
        
    def see_password(self, name_ak):
        try:
            with open(f"C:/Users/admin/password_d/password_{name_ak}.txt", "r") as f:
                result = f.readlines()
                for line in result:
                    print(line)

        except Exception as e:
            return e



def main():
    generat_password = Password()
    print()
    print("Генератор паролей запущен")
    print("Выберите ниже цифру и напишите её для выполнение команды: ")
    while True:
        try:
            print("Выберите ниже цифру и напишите её для выполнение команды: ")
            print("0: завершить программу")
            print("1: сгенерировать новый пароль и сохранить его")
            print("2 : просмотреть пароль ак")
            make_user = int(input())
            if make_user == 1:
                user = input("Введите ак, для которого вы генерируете пароль: ")
                len_p = int(input("Введите длину пароля: "))
                result = generat_password.generated_password(user, len_p)
                print("Задача выполнена")
            
            if make_user == 0:
                break
            
            if make_user == 2:
                name_ak = input("Введите ак для просмотра его пароля: ")
                generat_password.see_password(name_ak)
                print("Задача Выполнена")
                
            
        except Exception as e:
            return f"Произошла ошибка: {e}"
    
if __name__ == "__main__":
    main()