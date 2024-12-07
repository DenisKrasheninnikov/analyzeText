from collections import Counter

def analyze_text(text):
    #Разделяем строку на список слов (без учёта регистра)
    words = text.lower().split()
    #Подсчитываем общее кол-во слов в тексте
    word_count = len(words)
    #здесь считаем количество уникальных слов 
    uniq_words = len(set([char for char in words])) 
    #функция для подсчёта частоты уникальных слов в тексте
    word_frequencies = Counter(words)
    #Возвращаем словарь со следующей информацией:
    return f'Анализ текста:\n {text}\n\nОбщее кол-во слов в тексте: {word_count}\nКол-во уникальных слов: {uniq_words}\nЧастота уникальных слов в тексте:\n{word_frequencies}'

print(analyze_text('Это пример текста. Это текст для анализа. Текст.'))



