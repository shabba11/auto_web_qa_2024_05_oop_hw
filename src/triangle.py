from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    """
    Класс для работы с треугольником

    Args:
        side_a: Сторона А треугольника
        side_b: Сторона Б треугольника
        side_c: Сторона С треугольника

    """

    def __init__(self, side_a: int, side_b: int, side_c: int):

        if (not (str(side_a).isnumeric() or isinstance(side_a, float))
                or not (str(side_b).isnumeric() or isinstance(side_b, float))
                or not (str(side_c).isnumeric() or isinstance(side_c, float))
                or isinstance(side_a, str)
                or isinstance(side_b, str)
                or isinstance(side_c, str)):
            raise ValueError("Одна из переменных не является числом (int)")
        elif side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны не могут быть меньше нуля")
        elif side_a + side_b <= side_c or side_b + side_c <= side_a or side_a + side_c <= side_b:
            raise ValueError("Треугольник существует только тогда, когда сумма двух его сторон больше третьей")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def __str__(self):
        return (f"Класс для вычисления периметра и площади треугольника по сторонам {self.side_a}, {self.side_b} и "
                f"{self.side_c}")

    @property
    def get_area(self):
        """
        Вычисление площади треугольника
        Return: Площадь треугольника
        """

        p = self.get_perimeter / 2

        return sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    @property
    def get_perimeter(self):
        """
        Вычисление периметра правильного треугольника
        Return: Периметр правильного треугольника
        """
        return self.side_a + self.side_b + self.side_c
