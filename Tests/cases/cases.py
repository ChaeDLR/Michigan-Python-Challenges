from os import listdir

cases: dict[str, list] = {}

for file in listdir("./data"):

    test_cases: list = []

    with open(f"./data/{file}", "r") as testcases_:

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

    cases[file[:-4]] = test_cases
