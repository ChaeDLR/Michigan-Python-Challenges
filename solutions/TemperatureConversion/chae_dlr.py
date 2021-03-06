"""
Chae DeLaRosa
Temperature converter challenge
"""


def celsius(fahrenheit: float) -> float:
    """
    Convert a float representing temperature in fahrenheit
    to one representing temperature in celsius
    """
    return round((fahrenheit - 32) / 1.8, 2)


def fahrenheit(celsius: float) -> float:
    """
    Convert a float representing temperature in celsius
    to one representing temperature in fahrenheit
    """
    return round(celsius * 1.8 + 32, 2)


def prompt_temperature() -> float:
    """
    Get a valid float representing temperature from the console
    return None if the user enters an exit code
    """
    while 1:
        print("Enter a temperature.")

        users_input = input()

        try:
            return float(users_input)

        except:
            if users_input in ["esc", "exit", "quit"]:
                return

            print("\nError: Invalid input.")
            print("Enter a float value.\n")


# if this file in the start point of the running python program
if __name__ == "__main__":
    import sys

    # cmd line args
    if "test" in sys.argv:
        from challenges import tests

        # test celsius to fahrenheit conversion
        to_celsius_result: tuple[
            int, int
        ] = tests.TestTempConverter.celsius_to_fahrenheit(fahrenheit)
        print(f"\nCelsius to fahrenheit results = {to_celsius_result}")
        print(f"Passes: {to_celsius_result[0]}")
        print(f"Fails: {to_celsius_result[1]}")

        # test fahrenheit to celsius conversion
        to_fahrenheit_result: tuple[
            int, int
        ] = tests.TestTempConverter.fahrenheit_to_celsius(celsius)
        print(f"\Fahrenheit to celsius results = {to_fahrenheit_result}")
        print(f"Passes: {to_fahrenheit_result[0]}")
        print(f"Fails: {to_fahrenheit_result[1]}")

    # console program
    else:

        print("\n-- Temperature converter --")

        while 1:
            print("Select conversion.")
            print("1. Fahrenheit to celsius")
            print("2. Celsius to fahrenheit\n")

            # wait for the user to submit input
            # attempt to cast input to a int
            users_input: str = input().lower()

            ####### First menu option. Fahrenheit to celsius. #######
            if users_input in ["1", "1.", "fahrenheit"]:
                print("Enter temperature in fahrenheit to convert to celsius.")

                temp: float = prompt_temperature()

                # temp == None if the user entered an exit code
                if temp == None:
                    # set users_input to any escape key
                    users_input = "esc"
                    break

                print(f"\n{temp} fahrenheit equals {celsius(temp)} celsius.\n")
                continue

            ####### Second menu option. Celsius to fahrenheit. #######
            elif users_input in ["2", "2.", "celsius"]:
                print("Enter temperature in celsius to convert to fahrenheit.")

                temp: float = prompt_temperature()

                if temp == None:
                    users_input = "esc"
                    break

                print(f"\n{temp} celsius equals {fahrenheit(temp)} fahrenheit.\n")
                continue

            if users_input in ["esc", "exit", "quit"]:
                break

            print("\nError: Invalid input.")
            print("Select a menu option.\n")
