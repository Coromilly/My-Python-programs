def count_letters():
    """
    Программа подсчитывает количество каждого символа в строке S.
    """

    s = (str(input('Введите строку S: ')))

    while s:
        i = s[0]
        print('Количество символов {0} в строке S равно {1}'.format(i, str(s.count(i))))
        s = s.replace(i, '')


count_letters()