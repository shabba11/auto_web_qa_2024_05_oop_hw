from src.figure import Figure


class Rectangle(Figure):
    """
    Класс для работы с прямоугольником

    Args:
        side_a: Сторона А прямоугольника
        side_b: Сторона Б прямоугольника

    """
    def __init__(self, side_a: int, side_b: int):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны прямоугольника не должны быть <= 0")
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f"Класс для вычисления периметра и площади прямоугольника по сторонам {self.side_a} и {self.side_b}"

    @property
    def get_area(self):
        """
        Вычисление площади прямоугольника
        Return: Площадь прямоугольника
        """
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        """
        Вычисление периметра прямоугольника
        Return: Периметр прямоугольника
        """
        return (self.side_a + self.side_b) * 2
