from typing import Callable

def rec_result(test_method: Callable) -> tuple[int, int]:
    """
        This is a decorator for test methods.
        It takes care of
            printing,
            keeping track of fails and passes,
            and returning the results
    """

    def test_callable(cls, callable):

        print(f"\nTesting {callable.__name__} callable.\n")

        passes: int = 0
        fails: int = 0

        for i in range(1, len(cls.cases) + 1):

            print(f"Testing case {i}: {cls.cases[i-1]}")

            try:
                test_method(cls, callable, _case=cls.cases[i-1])
                print(f"Test {i} passed.")
                passes += 1
            except:
                print(f"Test {i} failed.")
                fails += 1

        return (passes, fails)
    return test_callable
