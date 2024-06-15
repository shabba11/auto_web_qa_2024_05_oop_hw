from abc import ABC, abstractmethod


class Figure(ABC):
    """
    Описание методов фигуры и складывание площадей фигур
    """

    def __str__(self):
        return "Класс для описания методов фигуры и складывание площадей фигур"

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("В метод add_area должен передаваться класс Figure")
        return self.get_area + other_figure.get_area
