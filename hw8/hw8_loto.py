#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
#TODO:
        self._title = ' ' + 'Карточка компьютера' + ' '
        self._name = 'Компьютер'
 
        @property
        def name(self):
            return self._name
 
class Game(Card):
    def __init__(self):
        Card.__init__(self, rows_amount=3, cols_amount=9, nums_per_row=5, max_num=90)
        self._do = ['1', '2', 'exit']
        self._menu = '1 - играть с компьютером\n2 - играть с другом\nexit - выйти из игры'
        self._unit1 = None
        self._unit2 = None
 
 
    def _init_game(self):
        answer = ''
        while answer not in self._do:
            print(self._menu)
            answer = input()
        if answer == '1':
            self._init_game_pve()
        elif answer == '2':
            self._init_game_pvp()
        else:
            exit()
 
    def _create_cards(self):
        self._unit1.create_card()
        self._unit2.create_card()
 
    def _init_game_pve(self):
        self._unit1 = PlayerCard()
        self._unit2 = ComputerCard()
        self._create_cards()
 
    def _init_game_pvp(self):
        self._unit1 = PlayerCard()
        self._unit2 = PlayerCard()
        self._create_cards()
 
    def _get_random_num(self):
        random_numbers = random.sample(range(1, self._max_num + 1), self._max_num)
        for i in random_numbers:
            yield i, self._max_num - random_numbers.index(i) - 1
 
    def _check_answer(self, unit, num, answer):
        if answer == 'exit':
            print('Приходите еще поиграть')
            exit()
        elif answer != 'da' and answer != 'net':
            self._check_answer(unit, num, input('Зачеркнуть цифру? (da/net)'))
        elif answer == 'y' and unit.check_num(num):
            unit.modify_card(num)
            return 0
        elif answer == 'n' and not unit.check_num(num):
            return 0
        elif answer == 'y' and not unit.check_num(num):
            print('{} нет на вашей карточке.'.format(num), end=' ')
            return 1
        elif answer == 'n' and unit.check_num(num):
            print('{} на вашей карточке.'.format(num), end=' ')
            return 1
        else:
            print('Что-то пошло не так', answer)
            return 1
 
    def _clean(self):
        del self._unit1
        del self._unit2
 
    def _lets_play(self):
        num_generator = self._get_random_num()
        gen_res = next(num_generator)
        num = gen_res[0]
        left = gen_res[1]
 
        while self._unit1.nums and self._unit2.nums:
            print(self._unit1)
            print(self._unit2)
 
            print('Новый бочонок: {} (осталось {})'.format(num, left))
            print('Ходит {}'.format(self._unit1.name))
 
            if self._check_answer(self._unit1, num, input('Зачеркнуть цифру? (da/net)')):
                if type(self._unit2) == PlayerCard:
                    return '{}, к сожалению, вы проиграли.\nПоздравляем, {}! Вы победили'.format(self._unit1.name, self._unit2.name)
                else:
                    return '{}, к сожалению, вы проиграли.'.format(self._unit1.name)
            if type(self._unit2) == PlayerCard:
                print('Ходит {}'.format(self._unit2.name))
                if self._check_answer(self._unit2, num, input('Зачеркнуть цифру? (y/n)')):
                    return '{}, к сожалению, вы проиграли.\nПоздравляем, {}! Вы победили'.format(self._unit2.name, self._unit1.name)
            else:
                if self._unit2.check_num(num):
                    self._unit2.modify_card(num)
 
            gen_res = next(num_generator)
            num = gen_res[0]
            left = gen_res[1]
 
        if not self._unit1.nums and not self._unit2.nums:
            return 'Ничья!'
        elif self._unit2.nums:
            return 'Поздравляем, {}, вы победили!'.format(self._unit1.name)
        else:
            if type(self._unit2) == PlayerCard:
                return 'Поздравляем, {}, вы победили!'.format(self._unit2.name)
            else:
                return 'Компьютер успел первым. Попробуйте еще раз.'
 
    def main(self):
        while True:
            answer = input('Сыграем? (da/net)')
            if answer == 'da':
                self._init_game()
                print(self._lets_play())
                self._clean()
            elif answer == 'net':
                print('До свидания!')
                return
 
if __name__ == '__main__':
    game = Game()
    game.main()
