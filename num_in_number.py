def num_in_number():
    """
    Проверка количества вхождения цифры 'num' в числа от 0 до 'number'.
    'num' = [0, 9], 'number' > 0
    """

    count = 0
    num = int(input('Введите натуральное число num: '))
    number = int(input('Введите натуральное число number: '))
    for i in range(number + 1):
        i = str(i)
        for j in i:
            if j == str(num):
                count += 1
    print('В числах от 0 до {0} содержится {1} цифр {2}'.format(number, count, num))

num_in_number()
