from src.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс для работы с квадратом
    """
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError("Стороны квадрата не могут быть <= 0")
        super().__init__(side_a=side_a, side_b=side_a)

    def __str__(self):
        return "Класс для вычисления периметра и площади квадрата"
