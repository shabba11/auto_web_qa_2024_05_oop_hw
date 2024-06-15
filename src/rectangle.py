from src.figure import Figure


class Rectangle(Figure):
    """
    Класс для работы с прямоугольником
    """
    def __init__(self, side_a: int, side_b: int):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны прямоугольника не должны быть <= 0")
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return "Класс для вычисления периметра и площади прямоугольника"

    @property
    def get_area(self):
        """
        Вычисоение площади прямоугольника
        :return: Площадь прямоугольника
        """
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        """
        Вычисление периметра прямоугольника
        :return: Периметр прямоугольника
        """
        return (self.side_a + self.side_b) * 2
