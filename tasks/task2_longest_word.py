import re
import logging

logger = logging.getLogger(__name__)

def find_longest_words(text: str) -> tuple[list[str], int]:
    
    if not text.strip():
        return [], 0
    words = re.findall(r'\b\w+\b', text)
    if not words:
        return [], 0
    max_len = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_len]
    seen = set()
    unique_longest = []
    for w in longest:
        if w not in seen:
            unique_longest.append(w)
            seen.add(w)
    return unique_longest, max_len

def run_task2():
    logger.info("Запуск задания 2")
    print("\n=== Задание 2: Самое длинное слово ===")
    text = input("Введите текст: ").strip()
    if not text:
        logger.warning("Пустой ввод задания 2")
        print("Текст пуст. Нечего обрабатывать.")
        return
    longest_words, length = find_longest_words(text)
    if longest_words:
        logger.info(f"Самые длинные слова: {longest_words}, длина = {length}")
        print(f"Самое длинное слово(а): {longest_words}")
        print(f"Длина: {length}")
    else:
        logger.info("Нет слов в задании 2")
        print("Не найдено ни одного слова.")