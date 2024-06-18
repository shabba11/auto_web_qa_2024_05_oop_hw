import pytest

from src.square import Square


class TestSquare:
    """
    Тестирование квадрата
    """

    @pytest.mark.parametrize("side_a, result",
                             [(1, 1),
                              (3, 9),
                              (5.5, 30.25)],
                             ids=['side_a = 1', 'side_b = 3', 'side_a = 5.5'])
    def test_square_get_area_positive(self, side_a, result):
        """
        Вычисление площади квадрата. Позитивный тест
        """

        square = Square(side_a=side_a)

        assert square.get_area == result

    @pytest.mark.parametrize("side_a, result",
                             [(1, 4),
                              (3, 12),
                              (5.5, 22)],
                             ids=['side_a = 1', 'side_b = 3', 'side_a = 5.5'])
    def test_square_get_perimeter_positive(self, side_a, result):
        """
        Вычисление периметра квадрата. Позитивный тест
        """

        square = Square(side_a=side_a)

        assert square.get_perimeter == result

    @pytest.mark.parametrize("side_a",
                             [0, -1],
                             ids=['side_a = 0', 'side_a = -1'])
    def test_square_error_side_less_then_zero(self, side_a):
        """
        Ошибка: Стороны прямоугольника не должны быть <= 0. Негативный тест
        """

        with pytest.raises(ValueError):
            Square(side_a=side_a)
