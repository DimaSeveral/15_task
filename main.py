import logging
from tasks import task1_unique_words, task2_longest_word, task4_big_numbers

logging.basicConfig(
    level = logging.INFO,
        format = '%(asctime)s - %(levelname)s - %(message)s',
        handlers = [logging.FileHandler("app.log", encoding= 'utf-8')]
)
logger = logging.getLogger(__name__)

def main_menu():
    logger.info("Запуск главного меню")
    while True:
        print("\n" + "="*50)
        print("Главное меню")
        print("1. Задание 1: Уникальные слова")
        print("2. Задание 2: Самое длинное слово")
        print("3. Задание 4: Большие числа")
        print("4. Выход")
        choice = input("Выберите задание (1-4): ").strip()
        
        if choice == '1':
            logger.info("Выбрано задание 1. Уникальне слова.")
            task1_unique_words.run_task1()
        elif choice == '2':
            logger.info("Выбрано задание 2. Самое длинное слово.")
            task2_longest_word.run_task2()
        elif choice == '3':
            logger.info("Выбранно задание 4. Большие числа.")
            task4_big_numbers.run_task4()
        elif choice == '4':
            logger.info("Выбрано <<Выход из программы>>.")
            print("Выход из программы.")
            break
        else:
            logger.warning(f"Неверный выбор в мею. {choice}")
            print("Неверный выбор.")

if __name__ == "__main__":
    main_menu()