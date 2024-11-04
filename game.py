from gameparts import Board
from gameparts.exceptions import FieldIndexError


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    # Отрисовать поле в терминале.
    game.display()
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
    # В метод make_move передаются те координаты, которые ввёл пользователь.
    game.make_move(row, column, 'X')
    print('Ход сделан!')
    # Перерисовать поле с учётом сделанного хода.
    game.display()


if __name__ == '__main__':
    main()
