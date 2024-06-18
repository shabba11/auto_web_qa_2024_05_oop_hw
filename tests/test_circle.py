import pytest

from src.circle import Circle


class TestCircle:
    """
    Тестирование круга.
    """

    @pytest.mark.parametrize("radius, result",
                             [(15, 706.858347057703425),
                              (1, 3.141592653589793),
                              (3.5, 38.484510006474964)],
                             ids=['radius = 15', 'radius = 1', 'radius = 3.5'])
    def test_circle_get_area_positive(self, radius, result):
        """
        Вычисление площади круга. Позитивный тест
        """

        circle = Circle(radius=radius)

        assert circle.get_area == result

    @pytest.mark.parametrize("radius, result",
                             [(15, 94.24777960769379),
                              (1, 6.283185307179586),
                              (3.5, 21.991148575128551)],
                             ids=['radius = 15', 'radius = 1', 'radius = 3.5'])
    def test_circle_get_perimeter_positive(self, radius, result):
        """
        Вычисление периметра круга. Позитивный тест
        """

        circle = Circle(radius=radius)

        assert circle.get_perimeter == result

    @pytest.mark.parametrize("radius",
                             [0, -1],
                             ids=['radius = 0', 'radius = -1'])
    def test_circle_error_radius_less_then_zero(self, radius):
        """
        Ошибка: "Радиус круга не может быть <= 0". Негативный тест
        """

        with pytest.raises(ValueError):
            Circle(radius=radius)

    @pytest.mark.parametrize(
        "radius",
        [True, False, 'test', '12', None],
        ids=['radius = True', 'radius = False', 'radius = "test"', 'radius = "12"', 'radius = None'])
    def test_circle_error_radius_is_not_int_or_float(self, radius):
        """
        Ошибка: "Радиус не является числом". Негативный тест
        """

        with pytest.raises(ValueError):
            Circle(radius=radius)
