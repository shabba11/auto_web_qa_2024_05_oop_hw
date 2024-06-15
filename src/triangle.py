from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    """
    Класс для работы с треугольником
    """

    def __init__(self, side_a: int, side_b: int, side_c: int):

        if not isinstance(side_a, int) or not isinstance(side_b, int) or not isinstance(side_b, int):
            raise ValueError("Одна из переменных не является числом (int)")
        elif side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны не могут быть меньше нуля")
        elif side_a != side_b != side_c:
            raise ValueError("Треугольник должен быть правильным с одинаковыми сторонами")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def __str__(self):
        return "Класс для вычисления периметра и площади треугольника"

    @property
    def get_area(self):
        """
        Вычисление площади правильного треугольника
        :return: Площадь правильного треугольника
        """
        return (sqrt(3)/4) * self.side_a ** 2

    @property
    def get_perimeter(self):
        """
        Вычисление периметра правильного треугольника
        :return: Периметр правильного треугольника
        """
        return self.side_a + self.side_b + self.side_c
