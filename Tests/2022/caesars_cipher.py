# February challenge


class TestCaesarCipher:

    # the file directory
    path: str = join(getcwd(), "CaesarsCipher")

    # list[plaintext, key, ciphertext]
    test_cases: list[list[str, int, str]] = []


    def __load_test_cases(self) -> None:
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

        # test bruteforce
        assert plaintext in CaesarsCipher.bruteforce_decrypt(case[2])

        print(f"Test {i} passed!")
        passes += 1
    except:
        print(f"Test {i} failed!")
        fails += 1

print(f"\n{passes} passed.")
print(f"{fails} failed.\n")
####### TEST #######


####### WRITE output to output.csv file #######
with open(join(path, "output.csv"), "w") as output:

    output.write("plaintext, key, ciphertext\n")

    for test in test_cases:

        test[2] = CaesarsCipher.encrypt(test[0], test[1])

        output.write(f"{test[0]}, {test[1]}, {test[2]}\n")
####### WRITE #######
