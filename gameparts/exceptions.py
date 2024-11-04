class FieldIndexError(IndexError):
    """Класс, который переопределяет исключение."""

    def __str__(self):
        return 'Введено значение за границами игрового поля'
