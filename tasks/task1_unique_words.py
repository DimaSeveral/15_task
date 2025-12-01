import re
from collections import Counter
import logging

logger = logging.getLogger(__name__)

def find_unique_words(text: str) -> list[str]:

    if not text.strip():
        return []
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return [word for word, count in word_counts.items() if count == 1]

def run_task1():
    logger.info("Запуск задания 1")
    print("\n=== Задание 1: Уникальные слова ===")
    text = input("Введите текст: ").strip()
    if not text:
        logger.info("Пустой ввод в задании 1")
        print("Текст пуст. Нечего обрабатывать.")
        return
    unique = find_unique_words(text)
    if unique:
        logger.info(f"Найдено {len(unique)} уникальных слов: {unique}")
        print("Уникальные слова:", unique)
    else:
        logger.info('Уникальных слов нет')
        print("В тексте нет уникальных слов.")