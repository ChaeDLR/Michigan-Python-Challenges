# January challenge
from typing import Callable
from .cases import cases
from .base import rec_result


class TestTempConverter:

    cases: list = cases.get("tempconverter")

    @classmethod
    @rec_result
    def celsius_to_fahrenheit(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """Test celsius to fahrenheit conversion"""
        try:
            _celsius = round(float(_case[0]), 2)
            _fahrenheit = round(float(_case[1]), 2)
        except:
            print(f"\nTest case {_case} value casting failed!")
            print(f"Method: {func.__name__}\n")
            raise

        output: float = round(func(_celsius), 2)
        expected: float = round(_fahrenheit, 2)

        try:
            assert output == expected
        except:
            print(f"\nFailed asserts equals!")
            print(f"Output {output}")
            print(f"Expected: {expected}\n")
            raise

    @classmethod
    @rec_result
    def fahrenheit_to_celsius(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """Test fahrenheit to celsius"""
        try:
            _celsius = round(float(_case[0]), 2)
            _fahrenheit = round(float(_case[1]), 2)
        except:
            print(f"\nTest case {_case} value casting failed!")
            print(f"Method: {func.__name__}\n")
            raise

        output: float = round(func(_fahrenheit), 2)
        expected: float = round(_celsius, 2)

        try:
            assert output == expected
        except:
            print(f"\nFailed asserts equals!")
            print(f"Output {output}")
            print(f"Expected: {expected}\n")
            raise
