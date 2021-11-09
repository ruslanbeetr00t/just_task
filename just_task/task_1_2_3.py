#https://tproger.ru/problems/python-3-exercises-for-beginners-geekbrains/
#Задача 1
a = [1, 1, 2, 3, 4, 5, 8, 13, 21, 34, 55, 89]
for number in a:
    if number < 5:
        print(number)

# книга Свейгарт розділ 3 задача 13 (варіант for)
for i in range(10):
    print(i+1)

# книга Свейгарт розділ 3 задача 13 (варіант while)
i = 0
while i < 10:
    i = i + 1
    print('цикл', i, 'викононо стільки разів')

# книга Свейгарт розділ 3 практична робота послідовність Коллатца.

def collatz():
    try:
        number = int(input('add number:- '))
        if number % 2 == 0:
            print('це парне чісло.')
        elif number % 2 == 1:
            print('це не парне чісло.')
    except ValueError:
        print('Помилка вводу данних')
        return collatz()


collatz()