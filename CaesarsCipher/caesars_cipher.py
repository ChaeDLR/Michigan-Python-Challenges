from os import getcwd
from os.path import join


# Chae DeLaRosa
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
                    index -=  len(cls.__characters)

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


# read test cases file and test the class's encrypt and decrypt methods
if __name__ == "__main__":

    # the file directory
    path: str = join(getcwd(), "CaesarsCipher")

    # list[plaintext, key, ciphertext]
    test_cases: list[list[str, int, str]] = []


    ####### READ test cases file #######
    with open(join(path, "test_cases.csv"), "r") as testcases_:

        lines = testcases_.readlines()

        for line in lines[1:]:

            line_prts: list[str] = line.split(",")

            test_cases.append(
                    [
                line_prts[0].strip(),
                int(line_prts[1].strip()),
                line_prts[2].strip()
                ]
            )
    ####### READ #######


    ####### TEST #######
    print("\n TEST CASE ITEMS")
    print("------------------")
    for item in test_cases:
        print(item)
    print("")

    passes: int = 0
    fails: int = 0
    print(f"testing...\n")
    for i, case in enumerate(test_cases, 1):
        try:
            # test encryption method
            assert CaesarsCipher.encrypt(case[0], case[1]) == case[2]

            # remove spaces from test cases plain text
            plaintext: str =  "".join(case[0].split(" "))

            # test decryption method
            assert CaesarsCipher.decrypt(case[2], case[1]) == plaintext

            print(f"Test {i} passed!")
            passes += 1
        except:
            print(f"Test {i} failed!")
            fails += 1

    print(f"\n{passes} passed.")
    print(f"{fails} failed.")
    ####### TEST #######


    ####### WRITE output to output.csv file #######
    # test_cases.append(
    #     ["Caesars Cipher", 177, ""]
    # )
    with open(join(path, "output.csv"), "w") as output:

        output.write("plaintext, key, ciphertext\n")

        for test in test_cases:

            test[2] = CaesarsCipher.encrypt(test[0], test[1])

            output.write(f"{test[0]}, {test[1]}, {test[2]}\n")
    ####### WRITE #######
