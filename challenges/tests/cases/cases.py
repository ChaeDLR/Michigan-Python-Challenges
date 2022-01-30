import os
from os import listdir, path

data_path: str = path.join(os.getcwd(), os.path.abspath(f"challenges/tests/cases/data"))


def get(filename: str) -> list:
    """
    Return a list containing lists of test case data retrieved from
    the file in the data folder that matches filename: str
    """
    test_cases: list = []
    with open(path.join(data_path, f"{filename}.csv"), "r") as testcases_:

        lines = testcases_.readlines()
        for line in lines[1:]:
            # TODO: Need to fix newline slicing
            line.strip()
            print(line[:-1])
            line = line[:-1] if line[-1:] == "\n" else line
            line_prts: list[str] = line.split(",")

            case = []
            for prt in line_prts:
                case.append(prt)

            test_cases.append(case)
    return test_cases
