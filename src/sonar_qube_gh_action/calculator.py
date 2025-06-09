class Calculator:
    def sum(self, num_1: int, num_2: int) -> int:
        return num_1 + num_2

    def subtract(self, num_1: int, num_2: int) -> int:
        return num_1 - num_2

    def multiply(self, num_1: int, num_2: int) -> int:
        return num_1 * num_2

    def divide(self, num_1: int, num_2: int) -> float:
        if num_2 == 0:
            raise ValueError("Cannot divide by zero")
        return num_1 / num_2

    def exponent(self, base: int, exponent: int) -> float:
        return float(base**exponent)

    def modulus(self, num_1: int, num_2: int) -> int:
        if num_2 == 0:
            raise ValueError("Cannot perform modulus by zero")
        return num_1 % num_2

    def square_root(self, num: int) -> float:
        if num < 0:
            raise ValueError("Cannot compute square root of negative number")
        return num**0.5

    def absolute(self, num: int) -> int:
        return abs(num)

    def factorial(self, num: int) -> int:
        if num < 0:
            raise ValueError("Cannot compute factorial of negative number")
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
