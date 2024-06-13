# функция смещения123 символов на определенное число влево или в право
def crypt(ch, n, start, finish): 
    if  start <=ord(ch)+n<= finish:
        return(chr(ord(ch)+n))
    elif n > 0:
        return(chr(start - 1  + ord(ch) + n - finish))
    elif n < 0:
        return(chr(finish + 1  + ord(ch) + n - start))
    
# функция шифра Цезаря
def cryptCesar(ch, n, start_low, finish_low, start_up, finish_up): 
    if start_low <=ord(ch)<= finish_low:
        return (crypt(ch,n,start_low,finish_low))
    elif start_up <=ord(ch)<= finish_up:
        return(crypt(ch,n,start_up,finish_up))
    else:
        return(ch)

    return res
# Инициалазируем переменные

text = input().split()  

start_low = 97
finish_low = 122
start_up = 65
finish_up = 90

# шифруем или дешифруем текст и выводим результат 
s= []
ln = []
count = 0

# считаем длину СЛОВА в каждом элементе массива (там со знаками препинания)
for i in range(len(text)): 
    for ch in text[i]:
        if ch.isalpha():
            count += 1
    ln.append(count)
    count = 0

# шифруем каждый элемент массива на длину слова
for i in range(len(text)):
    for ch in text[i]:
        s.append(cryptCesar(ch, ln[i], start_low, finish_low, start_up, finish_up))
    s.append(' ')
print (*s, sep = '')

