print('Добро пожаловать в игру Азбука!')
gamer = {'name': input('Как вас зовут?\n'),
         'age': int(input('Сколько тебе лет?\n')),
         'sex': input('Укажите свой пол М или Ж \n'),
         'pet_name': input('Укажите имя своего питомца \n'),
         'love': input('Вы любите играть в игры? Да или Нет \n'),
         }

if gamer['love'] == 'Да':
    gamer['love'] = bool(1)
if gamer['love'] == 'Нет':
    gamer['love'] = bool(0)
if gamer['age'] < 18:
    print('Тебе нельзя играть, ты слишком маленький')
    exit(0)
elif gamer['age'] > 90:
    sure = input('Игра для вас может быть утомительной, вы Уверены, что хотите играть? Да или Нет')
    if sure == 'Нет':
        print('До свидания', gamer['name'])
        exit(0)
    else:
        sure = input('Вы уверены? Да или Нет')
        if sure == 'Нет':
            print('До свидания', gamer['name'])
            exit(0)

else:
    print('Добро пожаловать в Игру', gamer['name'])

print('Я могу сказать каких букв Алфавита нет в твоем имени')
i = 0

name = list(gamer['name'].lower())
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
