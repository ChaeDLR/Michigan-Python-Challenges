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
        assert func(_case[0], _case[1]) == _case[2]

    @classmethod
    @rec_result
    def decrypt(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """test decrypt callable"""
        # remove spaces from test cases plain text
        plaintext: str = "".join(_case[0].split(" "))
        assert func(_case[2], _case[1]) == plaintext

    @classmethod
    @rec_result
    def bruteforce(cls, func: Callable, _case=[]) -> tuple[int, int]:
        """test decrypt callable"""
        # remove spaces from test cases plain text
        plaintext: str = "".join(_case[0].split(" "))
        assert plaintext in func(_case[2])
