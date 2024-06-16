import pytest

from src.triangle import Triangle


class TestTriangle:
    """
    Тестирование треугольника
    """

    @pytest.mark.parametrize("side_a, side_b, side_c, result",
                             [(3, 4, 5, 6),
                              (5, 6, 7, 14.696938456699069),
                              (5.5, 5, 1.5, 3.6742346141747673)],
                             ids=['sides = 1, 4, 3', 'sides = 5, 6, 7', 'sides = 5.5, 3, 1.5'])
    def test_triangle_get_area_positive(self, side_a, side_b, side_c, result):
        """
        Вычисление площади треугольника. Позитивный тест
        """

        triangle = Triangle(side_a=side_a, side_b=side_b, side_c=side_c)
        area = triangle.get_area

        assert area == result

    @pytest.mark.parametrize("side_a, side_b, side_c, result",
                             [(3, 4, 5, 12),
                              (5, 6, 7, 18),
                              (5.5, 5, 1.5, 12)],
                             ids=['sides = 1, 4, 3', 'sides = 5, 6, 7', 'sides = 5.5, 3, 1.5'])
    def test_triangle_get_perimeter_positive(self, side_a, side_b, side_c, result):
        """
        Вычисление периметра треугольника. Позитивный тест
        """

        triangle = Triangle(side_a=side_a, side_b=side_b, side_c=side_c)
        perimeter = triangle.get_perimeter

        assert perimeter == result

    @pytest.mark.parametrize("side_a, side_b, side_c",
                             [(True, 4, 5),
                              (5, False, 7),
                              (None, 5, 3),
                              ('test', 1, 2),
                              ('13', 2, 1)],
                             ids=['sides = True, 4, 5', 'sides = 5, False, 7', 'sides = None, 5, 3',
                                  'sides = "test", 1, 2', 'sides = "13", 2, 1'])
    def test_triangle_error_side_is_not_int_or_float(self, side_a, side_b, side_c):
        """
        Ошибка: "Одна из переменных не является числом". Негативный тест
        """

        with pytest.raises(ValueError):
            Triangle(side_a=side_a, side_b=side_b, side_c=side_c)

    @pytest.mark.parametrize("side_a, side_b, side_c",
                             [(-1, 4, 5),
                              (5, 0, 7),
                              (2, 5, -1)],
                             ids=['sides = -1, 4, 5', 'sides = 5, 0, 7', 'sides = 2, 5, -1'])
    def test_triangle_error_side_is_less_then_zero(self, side_a, side_b, side_c):
        """
        Ошибка: "Стороны не могут быть меньше нуля". Негативный тест
        """

        with pytest.raises(ValueError):
            Triangle(side_a=side_a, side_b=side_b, side_c=side_c)

    def test_triangle_error_two_side_not_less_then_other_side(self):
        """
        Ошибка: "Треугольник существует только тогда, когда сумма двух его сторон больше третьей". Негативный тест
        """

        with pytest.raises(ValueError):
            Triangle(side_a=4, side_b=1, side_c=2)
