
class TestBase:

    # the file directory
    path: str = getcwd()

    def __init__(self, **kwargs) -> None:

        for k in kwargs:
            self.__setattr__(k, kwargs[k])

    def _load_test_cases(self, path_: str) -> None:
        ####### READ test cases file #######
        with open(join(self.path, path_), "r") as testcases_:

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
