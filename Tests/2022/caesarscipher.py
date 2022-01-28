# February challenge
from typing import Callable
from ..cases import caesarscipher as cases


class TestCaesarCipher:
    @classmethod
    def encrypt(cls, encrypt_: Callable) -> tuple[int, int]:
        """test encrypt callable"""
        passes = 0
        fails = 0

        for i, case in enumerate(cases, 1):
            try:
                assert encrypt_(case[0], case[1]) == case[2]
                print(f"Test {i} passed!")
                passes += 1
            except:
                print(f"Test {i} failed!")
                fails += 1

        print(f"\n{passes} passed.")
        print(f"{fails} failed.\n")
        return (passes, fails)

    @classmethod
    def decrypt(cls, decrypt_: Callable) -> tuple[int, int]:
        """test decrypt callable"""
        passes = 0
        fails = 0

        for i, case in enumerate(cases, 1):
            # remove spaces from test cases plain text
            plaintext: str = "".join(case[0].split(" "))
            try:
                assert decrypt_(case[2], case[1]) == plaintext
                print(f"Test {i} passed!")
                passes += 1
            except:
                print(f"Test {i} failed!")
                fails += 1

        print(f"\n{passes} passed.")
        print(f"{fails} failed.\n")
        return (passes, fails)

    @classmethod
    def bruteforce(cls, bruteforce_: Callable) -> int:
        """test decrypt callable"""

        for case in cases:
            # remove spaces from test cases plain text
            plaintext: str = "".join(case[0].split(" "))
            try:
                assert plaintext in bruteforce_(case[2])
                print(f"Test passed!")
                return 1
            except:
                print(f"Test failed!")
                return 0
