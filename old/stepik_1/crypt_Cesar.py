# функция смещения символов на определенное число влево или в право
def crypt(ch, n, start, finish): 
    if  start <=ord(ch)+n<= finish:
        return(chr(ord(ch)+n))
    elif n > 0:
        return(chr(start - 1  + ord(ch) + n - finish))
    elif n < 0:
        return(chr(finish + 1  + ord(ch) + n - start))
    
# функция шифра Цезаря
def cryptCesar(text, n, start_low, finish_low, start_up, finish_up): 
    res = []
    for ch in text:
        if start_low <=ord(ch)<= finish_low:
            res.append(crypt(ch,n,start_low,finish_low))
        elif start_up <=ord(ch)<= finish_up:
             res.append(crypt(ch,n,start_up,finish_up))
        else:
            res.append(ch)

    return res
# Инициалазируем переменные
language = ''
direct= ''
num = ''

# Вводим данные
while (language != 'ru') and (language != 'en'): # проверяем корректность ввода языка
    language = input('Введите язык текста (ru/en): ')    
while (direct != 'e') and (direct != 'd'): # проверяем корректность ввода направления шифрования
    direct = input('Шифруем или дешифруем? (e/d): ') 
while not(num.isdigit()): # проверяем корректность ввода количества символов для смещения
    num = input('Количество смещаемых сиволов: ')
text = input('Введите текст: ')  

 # формируем корректное число смещения символов в зависимости от языка и направления
if direct == 'd' and language == 'en':   
    num = -(int(num) % 26)
elif direct == 'e' and language == 'en':
    num = int(num) % 26
elif direct == 'd' and language == 'ru':
    num = -(int(num) % 32)
elif direct == 'e' and language == 'ru':
    num = int(num) % 32

# задаем начальные и конечные коды символов в соответствии с выбранным языком
if language == 'en':
    start_low = 97
    finish_low = 122
    start_up = 65
    finish_up = 90
else:
    start_low = 1072
    finish_low = 1103
    start_up = 1040
    finish_up = 1071

# шифруем или дешифруем текст и выводим результат 

result = cryptCesar(text, num, start_low, finish_low, start_up, finish_up)
print (*result, sep='')
