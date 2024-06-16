import pytest

from src.triangle import Triangle
from src.square import Square


class TestFigure:
    """
    Тестирование класса Figure
    """

    def test_figure_add_area_positive(self):
        """
        Складывание площадей фигур. Позитивный тест
        """

        triangle = Triangle(side_a=3, side_b=4, side_c=5)
        square = Square(side_a=5)
        sum_area = square.add_area(triangle)

        assert sum_area == 31

    def test_figure_error_class(self):
        """
        Ошибка: "В метод add_area должен передаваться класс Figure". Негативный тест
        """

        square = Square(side_a=5)

        with pytest.raises(ValueError):
            square.add_area(2)
