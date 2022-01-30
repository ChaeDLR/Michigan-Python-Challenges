"""
Chae DeLaRosa
Shift cipher (Caesar's Cipher)
"""


class CaesarsCipher:

    # all the characters the cipher will encrypt
    # all other characters will be skipped
    __characters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    # class method decorator allows the method to be called without needing
    # an instance of the class. ex. CaesarsCipher.encrypt(plaintext, key)
    @classmethod
    def encrypt(cls, plaintext: str, key: int) -> str:
        """encrypt plain text by shifting the index of each character by the key"""

        # abbreviate the key if it is larger than the characters string
        while key >= len(cls.__characters):
            key -= len(cls.__characters)

        # empty string to add the encrypted chars to
        cipher_text: str = ""

        # for each character in the text
        for pt_char in plaintext:
            # if the character is in the characters string
            if pt_char in cls.__characters:
                # add the key to the index of the plain text char
                # to get the index of the cipher text char
                index: int = cls.__characters.find(pt_char) + key

                # if the index goes past the end of the characters list
                if index >= len(cls.__characters):
                    # subtract length to loop the shift
                    index -= len(cls.__characters)

                # add the new char to the end of the cipher text string
                cipher_text = cipher_text.__add__(cls.__characters[index])

        return cipher_text

    @classmethod
    def decrypt(cls, ciphertext: str, key: int) -> str:
        """decrypt the given ciphertext"""

        # abbreviate the key if it is larger than the characters string
        while key >= len(cls.__characters):
            key -= len(cls.__characters)

        plain_text: str = ""

        for ct_char in ciphertext:

            if ct_char in cls.__characters:

                index: int = cls.__characters.find(ct_char) - key

                if index < 0:
                    index += len(cls.__characters)

                plain_text = plain_text.__add__(cls.__characters[index])

        return plain_text

    @classmethod
    def bruteforce_decrypt(cls, ciphertext: str) -> list[str]:
        """Brute force a cipher text. Return a list of all possible solutions"""
        solutions: list[str] = []
        for i in range(1, len(cls.__characters)):
            solutions.append(cls.decrypt(ciphertext, i))
        return solutions


if __name__ == "__main__":
    from challenges.tests import TestCaesarsCipher

    encrypt_results: tuple = TestCaesarsCipher.encrypt(CaesarsCipher.encrypt)

    print(f"Encryption results: {encrypt_results}")
