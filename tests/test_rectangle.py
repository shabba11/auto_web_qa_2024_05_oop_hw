import pytest

from src.rectangle import Rectangle


class TestRectangle:
    """
    Тестирование прямоугольника
    """

    @pytest.mark.parametrize("side_a, side_b, result",
                             [(1, 4, 4),
                              (2, 6, 12),
                              (5.5, 3, 16.5)],
                             ids=['side_a = 1, side_b = 4', 'side_a = 2, side_b = 6', 'side_a = 5.5, side_b = 3'])
    def test_rectangle_get_area_positive(self, side_a, side_b, result):
        """
        Вычисление площади прямоугольника. Позитивный тест
        """

        rectangle = Rectangle(side_a=side_a, side_b=side_b)

        assert rectangle.get_area == result

    @pytest.mark.parametrize("side_a, side_b, result",
                             [(1, 4, 10),
                              (2, 6, 16),
                              (5.5, 3, 17)],
                             ids=['side_a = 1, side_b = 4', 'side_a = 2, side_b = 6', 'side_a = 5.5, side_b = 3'])
    def test_rectangle_get_perimeter_positive(self, side_a, side_b, result):
        """
        Вычисление периметра прямоугольника. Позитивный тест
        """

        rectangle = Rectangle(side_a=side_a, side_b=side_b)

        assert rectangle.get_perimeter == result

    @pytest.mark.parametrize("side_a, side_b",
                             [(1, 0),
                              (-2, 2)],
                             ids=['side_a = 1, side_b = 0', 'side_a = -2, side_b = 2'])
    def test_rectangle_error_side_less_then_zero(self, side_a, side_b):
        """
        Ошибка: Стороны прямоугольника не должны быть <= 0. Негативный тест
        """

        with pytest.raises(ValueError):
            Rectangle(side_a=side_a, side_b=side_b)
