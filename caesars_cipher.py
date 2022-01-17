import os
# Chae DeLaRosa
class CaesarsCipher:

    __characters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __clean_text(text: str, characters: str) -> str:
        """remove any characters the cipher does not work with"""
        text: str = text.upper()
        for i in range(len(text)):
            if not text[i] in characters:
                text = text.replace(text[i], ".")

        text_parts: list[str] = text.split(".")
        text: str = ""
        for part in text_parts:
            if part != ".":
                text = text.__add__(part)
        return text

    @classmethod
    def encrypt(cls, plaintext: str, key: int) -> str:
        """encrypt a message by shifting the index by key"""
        plain_text: str = cls.__clean_text(plaintext, cls.__characters)
        cipher_text: str = ""

        for pt_char in plain_text:
            index: int = cls.__characters.find(pt_char) + key

            while index >= len(cls.__characters):
                index -= len(cls.__characters)

            cipher_text = cipher_text.__add__(cls.__characters[index])

        return cipher_text

    @classmethod
    def decrypt(cls, ciphertext: str, key: int) -> str:
        """decrypt the given ciphertext"""
        cipher_text: str = cls.__clean_text(ciphertext, cls.__characters)
        plain_text: str = ""

        for ct_char in cipher_text:
            index: int = cls.__characters.find(ct_char) - key

            while index < 0:
                index += len(cls.__characters)

            plain_text = plain_text.__add__(cls.__characters[index])

        return plain_text


if __name__ == "__main__":
    # list[ tuple[ message, key, cipher_text ] ]
    test_cases: list[list[str, int, str]] = [
        ["hello world", 12, "TQXXAIADXP"],
        ["the quick brown fox jumps over the lazy dog", 3, "WKHTXLFNEURZQIRAMXPSVRYHUWKHODCBGRJ"],
        ["Michigan Python", 6, "SOINOMGTVEZNUT"],
        ["Python", 7, "WFAOVU"]
    ]

    with open(os.path.abspath(os.path.join(os.getcwd(), "test_cases.csv")), "w") as output:
        output.write("plaintext, key, ciphertext\n")
        for test in test_cases:
            test[2] = CaesarsCipher.encrypt(test[0], test[1])

            output.write(f"{test[0]}, {test[1]}, {test[2]}\n")
