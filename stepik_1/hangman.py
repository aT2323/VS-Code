from random import *
word_list = ['дверь', 'холодильник', 'пальто', 'дрель','стена', 'муха', 'вертолет','ковер', 'дневник', 'виселица', 'лестница', 'камень', 'смерть']

#берем рандомное слово из списка слов выше и возвращаем его в верхнем регистре
def get_word():
    return choice(word_list).upper()

# функция печати слова и его длины
def print_word_len(word):
    print('Текущее слово:', word, 'длина слова:', len(word))

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    print(stages[tries])

# функция игры
def play(word):
   
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    # тело функции
    print('Привет. Я хочу сыграть с тобой в игру.\nСкоро здесь будешь ты...')
    display_hangman(tries)
    print('У тебя еть 6 попыток. чтобы угадать слово, которое я загадал.\nЕсли не сможешь - ты останешься висеть здесь навсегда.\nИтак, начнем....')
    print_word_len(word_completion)
    while (not guessed) and (tries != 0):
        attempt = input().upper()
        while (not attempt.isalpha()) or (attempt.upper() in  guessed_letters) or (attempt.upper() in  guessed_words):
            print('Ты ИЗДЕВАЕШЬСЯ? Введи новую БУКВУ или новое СЛОВО, если ты так уверен в себе')
            attempt = input()
        if attempt == word:
            print('Да ты СЧАСТЛИВЧИК! Поздравляю, сегодня тыбудешь жить....НАВЕРНО....')
            guessed = True
        elif attempt in word and len(attempt) == 1:
            guessed_letters.append(attempt)
            temp = list(word_completion)
            for i in range (len(word)):
                if word[i] == attempt:
                    temp[i] = attempt
            word_completion = ''.join(temp)
            print_word_len(word_completion)
            if  not '_' in word_completion:
                print('Ты все таки смог... Что ж, возможно, я найду другой способ добраться до ТЕБЯ!')
                guessed = True
            else:
                print('ПОЗДРАВЛЯЮ! ТЫ СТАЛ НА ШАГ БЛИЖЕ... ОКРЫЛЯЕТ, НЕПРАВДА ЛИ?')
                print_word_len(word_completion)
        elif not (attempt in word) and len(attempt) == 1:
                print('Ох, какая прелесть... Скоро ты будешь МОЙ')
                tries -=1
                display_hangman(tries)
                print_word_len(word_completion)
                guessed_letters.append(attempt)
        elif len(attempt) > 1 and attempt != word:
            guessed_words.append(attempt)
            print('ПОРАЗИТЕЛЬНЫЙ...ГЛУПЕЦ. Ты бездумно пытаешься УГАДАТЬ. Что ж, мне НРАВИТСЯ твое тело, парящее наз землей, ХА-ХА-ХА')
            tries -=1
            display_hangman(tries)
            print_word_len(word_completion)

    print('Что ж, я загадал слово - ', word)
    print()
    if guessed:
        print('Ты можешь идти')
    else:
        print('Он не игрок и не романтик,\nИ в мимолётной тишине,\nЗавязывает крепкий бантик,\nНет, не на кедах - на СЕБЕ.\n(ХРУСТ ЛОМАЮЩЕЙСЯ ШЕИ)')
while True:    
    word = get_word()
    play(word)
    rp = input('Хочешь испытать удачу еще раз?(y/n)')
    if rp =='y':
        continue
    else:
        print('Пока, червь')
        break

