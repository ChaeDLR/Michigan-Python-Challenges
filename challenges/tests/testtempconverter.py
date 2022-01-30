# January challenge
from typing import Callable
from .cases import cases
from .base import rec_result


class TestTempConverter:

    cases: list = cases.get("tempconverter")

    @classmethod
    @rec_result
    def celsius(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """Test celsius to fahrenheit conversion"""
        try:
            celsius = float(_case[0])
            fahrenheit = float(_case[1])
        except:
            print(f"Test case {_case} convertion failed!")
            print(f"Method: {func.__name__}")
            raise ValueError

        assert round(func(celsius), 2) == round(fahrenheit, 2)
