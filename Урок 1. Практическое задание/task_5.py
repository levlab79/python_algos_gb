"""
Задание 5.

Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""

class PlatesStack:
    def __init__(self, max_one_stack):
        self.max_one_stack = 7
        self._main_stack = [[]]

    def __str__(self):
        '''Выводим на экран стопки тарелок.'''
        return_list = []
        # Проходим по уровням, начиная сверху.
        for level in range(self.max_one_stack + 1):
            # Проверяем не закончились ли тарелки в стопке.
            if level < self.max_one_stack:
                # Проходим по каждой стопке.
                for one_stack in self._main_stack:
                    # Проверяем есть ли на этом уровне в данной стопке тарелки.
                    if len(one_stack) >= self.max_one_stack - level:
                        return_list.append(f' [  {one_stack[self.max_one_stack - level - 1]:^3}  ]' + ' ' * 7)
                return_list.append('\n')
            else:
                # Рисуем под каждой стопкой подставку.
                for one_stack in self._main_stack:
                    return_list.append('\\[=======]/' + ' ' * 6)
        return ''.join(return_list)

    def add_plate(self, new_plate):
        '''Добавляем тарелку в стопки.'''
        # Проверяем осталось ли еще место в последней стопке.
        if len(self._main_stack[-1]) == self.max_one_stack:
            # Добавляем тарелку в новую стопку, т.к. последняя заполнена.
            self._main_stack.append([new_plate])
        else:
            # Добавляем тарелку в последнюю стопку.
            self._main_stack[-1].append(new_plate)


# Создаем стопки тарелок (максимальное значение в каждой стопке - 7).
our_plates = PlatesStack(max_one_stack=7)
# Добавляем тарелки.
for one_plates in range(25):
    # Тарелки представлены в виде целых чисел.
    our_plates.add_plate(one_plates + 1)

# Выводим на экран наши тарелки.
print(our_plates)
