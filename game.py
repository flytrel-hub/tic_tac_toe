from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    # Создать игровое поле - объект класса Board.
    # Запускается бесконечный цикл.
    game = Board()
    # Отрисовать поле в терминале.
    game.display()
    while True:
        try:
            # Тут пользователь вводит координаты ячейки.
            row = int(input('Введите номер строки: '))
            # Если введённое значение меньше нуля или больше или равно
            # field_size (это значение равно трём, оно хранится в модуле
            # parts.py)..
            if row < 0 or row >= game.field_size:
                # ...выбросить исключение FieldIndexError.
                raise FieldIndexError
            column = int(input('Введите номер столбца: '))
            # Если введённое значение меньше нуля или больше или равно
            # field_size (это значение равно трём, оно хранится в модуле
            # parts.py)..
            if column < 0 or column >= game.field_size:
                # ...выбросить исключение FieldIndexError.
                raise FieldIndexError
        except FieldIndexError:
            # ...выводятся сообщения...
            print(
                'Значение должно быть неотрицательным и меньше '
                f'{game.field_size}.'
            )
            print('Пожалуйста, введите значения для строки и столбца заново.')
            # ...и цикл начинает свою работу сначала,
            # предоставляя пользователю ещё одну попытку ввести данные.
            continue
        else:
            # ...значит, введённые значения прошли все проверки
            # и могут быть использованы в дальнейшем.
            # Цикл прерывается.
            break
            # В метод make_move передаются те координаты, которые ввёл пользователь.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()


if __name__ == '__main__':
    main()
