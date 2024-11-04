from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def main():
    # Создать игровое поле - объект класса Board.
    # Запускается бесконечный цикл.
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Это флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    # Отрисовать поле в терминале.
    game.display()

    # Тут запускается основной цикл игры.
    while running:

        print(f'Ход делают {current_player}')

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
                if game.board[row][column] != ' ':
                    # Вот тут выбрасывается новое исключение.
                    raise CellOccupiedError
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
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break
        # Теперь для установки значения на поле само значение берётся
        # из переменной current_player.
        game.make_move(row, column, current_player)
        game.display()
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением будет O,
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
