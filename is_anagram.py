def is_anagram():
    """
    Проверяет, являются ли слово1 и слово2 анаграмами.
    """
    from collections import Counter
    word1 = str(input('Введите слово1: '))
    word2 = str(input('Введите слово2: '))
    def sanitize(text):
        return (ch.lower() for ch in text.lower() if ch.isalpha())

    if Counter(sanitize(word1)) == Counter(sanitize(word2)):
        print('Слово {1} является анаграмой слова {0}'.format(word1, word2))
    else:
        print('Слово {1} не является анаграмой слова {0}'.format(word1, word2))

is_anagram()
