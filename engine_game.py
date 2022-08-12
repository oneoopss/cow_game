from random import randint
from termcolor import colored, cprint

_win = False
_attempt = 0 # Подсчет попыток
dict_game = {
    'Бык':0,
    'Корова':0
}
rand_list = []


def random():
    '''Комп. загадывает число'''
    global _attempt
    if _attempt ==0:
        cprint('''Добро пожаловать в Быки и Коровы! Суть проста: \n
        Компьютер загадывает число из 4 разных цифр от 0 до 9, например, 1234\n
        Игроку необходимо угадать это число. Быки подскажут, если число стоит на правильной позиции,\n
        Коровы - если цифра есть в числе, загаданном комьютере.\n
        Чтобы получить подсказку, отправьте свой вариант числа с ! в конце, удачи!
        ''',color='green')
    _attempt += 1
    while len(rand_list)<4:
        x = randint(0,9)
        if str(x) not in rand_list:
            rand_list.append(str(x))

    # print('Число загадано', rand_list)


def user_choice():
    '''Прием данных от пользователя и ответ'''
    
    choice = list(input('Введите число: '))

    global dict_game
    dict_game = {
        'Бык':0,
        'Корова':0
    }
    for i in range(len(rand_list)):
        if choice[i] in rand_list: 
            dict_game['Корова'] += 1      
        if choice[i]==rand_list[i]:
            dict_game['Бык']+=1
            dict_game['Корова']-=1
    
    cprint (f'После полученного ответа, в вашем стоиле набралось {dict_game["Бык"]} быков и {dict_game["Корова"]} коров',color='red') 
    if len(choice)==5:
        if choice[4] == '!':
            hint(choice)

    
def quit():
    '''Выход из игры'''
    
    if dict_game['Бык'] == 4:
        global _win
        _win = True 
        cprint('Вы победили',color='yellow')
        cprint(f'Вы справились с задачей за {_attempt} ходов',color='cyan')


def hint(choice):
    """Подсказка: указать, какие цифры стоят правильно"""
    global dict_game
    if dict_game['Бык']!=0:
        cprint(f'Правильно расставлены следующие цифры: ',color='cyan')
        for i in range(4):
            if list(choice)[i] == rand_list[i]:
                cprint(f'Цифра {choice[i]} стоит на своём месте',color='green')


    else:
        cprint('Для получения подсказки необходимо найти хотя бы одного быка!',color='yellow')


def restart():
    global _win
    global _attempt
    global rand_list
    if _win == True:
        restart_ = input('Отправьте +, если хотите попробовать ещё: ')
        if restart_ == '+':
            _win = False
            _attempt = 0
            rand_list = []
            
        else: 
            return