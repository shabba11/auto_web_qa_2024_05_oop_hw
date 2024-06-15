from src.figure import Figure
from math import pi


class Circle(Figure):
    """
    Класс для работы с кругом
    """

    def __init__(self, radius: int):
        if radius <= 0:
            raise ValueError("Радиус круга не может быть <= 0")
        self.radius = radius

    def __str__(self):
        return "Класс для вычисления периметра и площади круга"

    @property
    def get_area(self):
        """
        Вычисление площади круга
        :return: Площадь круга
        """
        return pi * (self.radius ** 2)

    @property
    def get_perimeter(self):
        """
        Вычисление периметра круга
        :return: Периметр круга
        """
        return 2 * pi * self.radius
