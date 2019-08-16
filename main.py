import random

print('Добро пожаловать в игру Азбука!')
gamer = {'name': {'quest': 'Назовите свое имя', 'answer': None},
         'age': {'quest': 'Сколько тебе лет?', 'answer': None},
         'sex': {'quest': 'Укажите пол М или Ж', 'answer': None},
         'pet_name': {'quest': 'Имя твоего питомца', 'answer': None},
         'love': {'quest': 'Ты любишь играть в игры? Да или Нет', 'answer': None},
         }

for quest in gamer:
    while True:
        temp = input(gamer[quest]['quest'] + '\n')
        if temp == 'exit':
            exit(0)

        if quest == 'age':
            if not temp.isdigit():
                continue
            temp = int(temp)
            if temp < 18:
                print('Вы слишком молоды, До свидания', gamer['name']['answer'])
                exit(0)

        if quest == 'sex':
            temp = temp.upper()
            if not (temp == 'Ж' or temp == 'М'):
                continue

        if quest == 'love':
            temp = temp.title()
            if temp == 'Да':
                temp = True
            elif temp == 'Нет':
                temp = False
            else:
                continue

        gamer[quest]['answer'] = temp
        break

print('Добро пожаловать в Игру', gamer['name']['answer'])

print('Я могу сказать каких букв Алфавита нет в твоем имени')
i = 0

name = list(gamer['name']['answer'].lower())
while i < 32:
    count = 0
    j = 0
    while j < len(name):
        if name[j] == chr(1072 + i):
            count += 1
        j += 1

    if count == 0:
        print(chr(1072 + i))
    i += 1

print('Я задумал 16 чисел от 1 - 16 и расположил их в произвольном порядке в строке. Скажи мне Где какое.')
hide_numbers = ['|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|', '|*|',
                '|*|', '|*|', ]
numbers = [1, 9, 5, 4, 11, 2, 13, 16, 8, 10, 3, 15, 14, 6, 7, 12]
ask_numbers = [1, 9, 5, 4, 11, 2, 13, 16, 8, 10, 3, 15, 14, 6, 7, 12]
count = 0

while True:
    quest_number = random.choice(ask_numbers)
    while True:
        print(hide_numbers)
        index_answer = int(input(f'где число {quest_number} \n'))
        if quest_number == numbers[index_answer - 1]:
            i = 0
            for char in hide_numbers:
                if i == numbers.index(quest_number):
                    hide_numbers[i] = f'|{quest_number}|'
                    ask_numbers.remove(quest_number)
                    if len(ask_numbers) == 0:
                        print(f'Поздравляю вы выиграли, вы потратили {count} попыток')
                        exit(0)
                    quest_number = random.choice(ask_numbers)
                    break
                i += 1
        else:
            print("Попробуйте еще")
            count += 1


