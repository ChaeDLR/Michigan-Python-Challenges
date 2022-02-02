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
        for line in lines:
            line = line.rstrip("\n")
            line_prts: list[str] = line.split(",")

            case = []
            for prt in line_prts:
                prt = prt.strip()
                case.append(prt)

            test_cases.append(case)
    return test_cases
