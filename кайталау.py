# Пример использования кайталау оператора
def main():
    while True:
        user_input = input("Введите 'да' или 'нет': ")
        if user_input.lower() == "да":
            print("Вы ввели 'да'.")
            break
        elif user_input.lower() == "нет":
            print("Вы ввели 'нет'. Попробуйте еще раз.")
        else:
            print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")

if __name__ == "__main__":
    main()
