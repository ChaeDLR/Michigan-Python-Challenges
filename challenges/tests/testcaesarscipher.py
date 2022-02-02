# February challenge
from typing import Callable
from .cases import cases
from .base import rec_result


class TestCaesarsCipher:

    cases: list = cases.get("caesarscipher")

    @classmethod
    @rec_result
    def encrypt(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """test encrypt callable"""
        try:
            key: int = int(_case[1])
        except:
            print(f"Test case {_case[1]} convertion failed!")
            print(f"Method: {func.__name__}")
            raise ValueError

        assert func(_case[0], key) == _case[2]

    @classmethod
    @rec_result
    def decrypt(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """test decrypt callable"""
        # remove spaces from test cases plain text
        try:
            key: int = int(_case[1])
        except:
            print(f"Test case {_case[1]} convertion failed!")
            print(f"Method: {func.__name__}")
            raise ValueError

        plaintext: str = "".join(_case[0].split(" "))
        assert func(_case[2], key) == plaintext

    @classmethod
    @rec_result
    def bruteforce(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """test decrypt callable"""
        # remove spaces from test cases plain text
        plaintext: str = "".join(_case[0].split(" "))
        assert plaintext in func(_case[2])
