# Michigan Python Challenges

### Submitting a challenge
1. Fork then clone this repository.
2. Navigate to the challenges folder and select a challenge.
3. Open the readme.md file in the selected challenge's folder and follow the instructions to complete the challenge.
4. Place your solution file in the corresponding solutions folder.
5. Open a pull request.
---

### Test your challenge functions
1. Import tests from the challenges package
```
from challenges import tests
```
2. Call a static method from the test class of the challenge you are testing and store the return value: tuple[passes: int, fails: int] to get your function's test results.
```
test_result: tuple[int, int] = tests.TestTempConverter.celsius_to_fahrenheit(your_function)
```