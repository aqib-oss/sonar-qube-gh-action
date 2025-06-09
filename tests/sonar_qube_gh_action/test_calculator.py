import pytest

from sonar_qube_gh_action.calculator import Calculator


def test_sum():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.sum(4, 3)

    # Assert
    assert result == 7


def test_subtract():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.subtract(10, 4)

    # Assert
    assert result == 6


def test_multiply():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.multiply(3, 5)

    # Assert
    assert result == 15


def test_divide():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.divide(10, 2)

    # Assert
    assert result == 5.0


def test_divide_by_zero():
    # Arrange
    calculator: Calculator = Calculator()

    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)


def test_divide_negative_numbers():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.divide(-10, -2)

    # Assert
    assert result == 5.0


def test_divide_negative_and_positive_numbers():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.divide(-10, 2)

    # Assert
    assert result == -5.0


def test_divide_positive_and_negative_numbers():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.divide(10, -2)

    # Assert
    assert result == -5.0


def test_exponent():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.exponent(2, 3)

    # Assert
    assert result == 8.0


def test_exponent_negative_base():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.exponent(-2, 3)

    # Assert
    assert result == -8.0


def test_exponent_negative_exponent():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.exponent(2, -3)

    # Assert
    assert result == 0.125  # 1/8


def test_exponent_zero_exponent():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.exponent(2, 0)

    # Assert
    assert result == 1.0  # Any number to the power of 0 is 1


def test_exponent_zero_base():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.exponent(0, 5)

    # Assert
    assert result == 0.0  # 0 raised to any positive power is 0


def test_exponent_zero_base_zero_exponent():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.exponent(0, 0)

    # Assert
    assert result == 1.0  # 0 raised to the power of 0 is conventionally defined as 1


def test_modulus():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.modulus(10, 3)

    # Assert
    assert result == 1


def test_modulus_zero_divisor():
    # Arrange
    calculator: Calculator = Calculator()

    # Act & Assert
    with pytest.raises(ValueError, match="Cannot perform modulus by zero"):
        calculator.modulus(10, 0)


def test_square_root():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: float = calculator.square_root(16)

    # Assert
    assert result == 4.0


def test_square_root_negative_number():
    # Arrange
    calculator: Calculator = Calculator()

    # Act & Assert
    with pytest.raises(
        ValueError, match="Cannot compute square root of negative number"
    ):
        calculator.square_root(-16)


def test_absolute():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.absolute(-5)

    # Assert
    assert result == 5


def test_factorial():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.factorial(5)

    # Assert
    assert result == 120  # 5! = 5 * 4 * 3 * 2 * 1 = 120


def test_factorial_zero():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.factorial(0)

    # Assert
    assert result == 1  # 0! is defined as 1


def test_factorial_negative():
    # Arrange
    calculator: Calculator = Calculator()

    # Act & Assert
    with pytest.raises(ValueError, match="Cannot compute factorial of negative number"):
        calculator.factorial(-5)


def test_factorial_one():
    # Arrange
    calculator: Calculator = Calculator()

    # Act
    result: int = calculator.factorial(1)

    # Assert
    assert result == 1  # 1! is defined as 1
