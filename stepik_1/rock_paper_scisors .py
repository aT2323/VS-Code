throw = ['каменьножницы', 'ножницыбумага', 'бумагакамень']

Timur = input()
Ruslan = input()

if Timur == Ruslan:
    print('ничья')
elif Timur+Ruslan in throw:
    print('Тимур')
else:
    print('Руслан')