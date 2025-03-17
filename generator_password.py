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
                password = password + strok_password + number_password + strok_password2
            
            if os.path.getsize("C:/Users/admin/password_d/password.txt") == 0:
                with open("C:/Users/admin/password_d/password.txt", "w") as f:
                    f.write(f" {name_ak} пароль: {password}")
                    return True
            else:
                with open("C:/Users/admin/password_d/password.txt", "a") as f:
                    f.write(f"1 {name_ak} пароль: {password}" + '\n')
                    return False
                
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
            make_user = int(input())
            if make_user == 1:
                user = input("Введите ак, для которого вы генерируете пароль: ")
                len_p = int(input("Введите длину пароля: "))
                result = generat_password.generated_password(user, len_p)
            
            if make_user == 0:
                break

            if result:
                print("Задача выполнена")
            else:
                print("Что-то пошло не так")
                
            
        except Exception as e:
            return f"Произошла ошибка: {e}"
    
if __name__ == "__main__":
    main()